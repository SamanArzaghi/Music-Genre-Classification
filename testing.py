from tensorflow.keras.models import load_model
import librosa
import numpy as np
import tensorflow as tf
from pydub import AudioSegment
import soundfile as sf
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def get_model(name):
    model = load_model(name)
    return model

def prepare(filename):
    list = []
    f = sf.SoundFile(filename)
    time = (len(f)/f.samplerate)
    time = time // 3
    for i in range(int(time)):
        t1 = 3 * i
        t2 = 3 *(i + 1)

        ffmpeg_extract_subclip(filename,t1,t2,targetname='newSong%s.wav'%i)
        list.append(convert('newSong%s.wav'%i))

    return list

def predict(model,X):
    #change axis to 4
    vector = np.zeros((10))
    X = np.array(X)
    for x in X:
        x = np.array([x])

        X = tf.expand_dims(x,axis = -1)

        x = x[...,np.newaxis]

        prediction = model.predict(x)
        vector = np.add(vector,prediction)

    prediction = np.argmax(vector,axis=1)

    return prediction


def convert(location):
    signal, sampleRate = librosa.load(location, sr=22050)
    mfcc = librosa.feature.mfcc(signal, sampleRate, n_mfcc=13, n_fft=2048, hop_length=512)
    mfcc = mfcc.T.tolist()
    return mfcc

def get_name(number):
    mapping= [
        "blues",
        "classical",
        "country",
        "disco",
        "hiphop",
        "jazz",
        "metal",
        "pop",
        "reggae",
        "rock"
    ]
    return mapping[number[0]]

def testing(filename):
    model = get_model('model.h5')
    X = prepare(filename)
    prediction = predict(model,X)
    Genre_name = get_name(prediction)

    return Genre_name

