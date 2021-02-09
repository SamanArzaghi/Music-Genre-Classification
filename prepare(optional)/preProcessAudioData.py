# To better understand the code, please read the following article
# https://www.researchgate.net/publication/347356900_Audio_Pre-Processing_For_Deep_Learning

import json
import os
import math
import librosa

datasetPath = "Data"
jsonPath = "data_10.json"
sampleRate = 22050
trackDuration = 30 # measured in seconds
samplesPerTrack = sampleRate * trackDuration


def save_mfcc(datasetPath, jsonPath, n_mfcc=13, n_fft=2048, hop_length=512, numberSegments=5):
    """Extracts MFCCs from music dataset and saves them into a json file along witgh genre labels.
        :param datasetPath (str): Path to dataset
        :param jsonPath (str): Path to json file used to save MFCCs
        :param n_mfcc (int): Number of coefficients to extract
        :param n_fft (int): Interval we consider to apply FFT. Measured in # of samples
        :param hop_length (int): Sliding window for FFT. Measured in # of samples
        :param: numberSegments (int): Number of segments we want to divide sample tracks into
        :return:
        """

    # dictionary to store mapping, labels, and MFCCs
    data = {
        "mapping": [],
        "labels": [],
        "mfcc": []
    }

    samplesPerSegments = int(samplesPerTrack / numberSegments)
    numberMfccVectorsPerSegment = math.ceil(samplesPerSegments / hop_length)

    # loop through all genre sub-folder
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(datasetPath)):

        # ensure we're processing a genre sub-folder level
        if dirpath is not datasetPath:

            # save genre label (i.e., sub-folder name) in the mapping
            semanticLabel = dirpath.split("\\")[-1] # if you are using linux use "/" instead of "\\"
            data["mapping"].append(semanticLabel)

            # process all audio files in genre sub-dir
            for f in filenames:

		        # load audio file
                filePath = os.path.join(dirpath, f)
                signal, sampleRateN = librosa.load(filePath, sr=sampleRate)

                # process all segments of audio file
                for d in range(numberSegments):

                    # calculate start and finish sample for current segment
                    start = samplesPerSegments * d
                    finish = start + samplesPerSegments

                    # extract mfcc
                    mfcc = librosa.feature.mfcc(signal[start:finish], sampleRateN, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)
                    mfcc = mfcc.T

                    # store only mfcc feature with expected number of vectors
                    if len(mfcc) == numberMfccVectorsPerSegment:
                        data["mfcc"].append(mfcc.tolist())
                        data["labels"].append(i-1)

    # save MFCCs to json file
    with open(jsonPath, "w") as fp:
        json.dump(data, fp, indent=4)
    
if __name__ == "__main__":
    save_mfcc(datasetPath, jsonPath, numberSegments=1)
