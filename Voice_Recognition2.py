import sounddevice as sd
import numpy as np
import speech_recognition as sr
import soundfile as sf


#Audio recording settings
duration = 5  # time (Second)
fs = 44100  #  frequency rate
channels = 1  # numbers of channels(1 for mono)

# recording function
def record_audio(duration, fs, channels):
    print("recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='int16')
    sd.wait()  # waiting...
    print("End.")
    return recording

# sound record
recording = record_audio(duration, fs, channels)

# convert Numpyarray to AudioData
audio_data = sr.AudioData(recording.tobytes(), fs, recording.dtype.itemsize)

# make a recognizer
recognizer = sr.Recognizer()

#record your voice
sf.write("test.wav", recording, fs)

# convert audio to text

# **************************** Functions *****************************
def startFunction():
    print("StartFunction is Running")

def endFunction():
    print("EndFunction is Running")
    
def runFunction():
    print("RunFunction is Running")
    
# ********************************************************************
text = ""
try:
    #text = recognizer.recognize_google(audio_data, language='en-US')
    text = recognizer.recognize_google(audio_data, language='fa-IR')
    print("your text: ", text)
except sr.UnknownValueError:
    print("We couldn't recognize your voice")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

if "start" in text:
    startFunction()
if "شروع" in text:
    startFunction()
if "end" in text:
    endFunction()
if "پایان" in text:
    endFunction()
if "run" in text:
    runFunction()
if "اجرا" in text:
    runFunction()

