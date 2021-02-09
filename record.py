import sounddevice as sd
from scipy.io.wavfile import write

def record():
    fs = 22050  
    seconds = 9  
    myRecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myRecording)  # Save as WAV file 
