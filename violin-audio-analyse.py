import numpy as np
import matplotlib.pyplot as plt
import wave
import sys


# import audio file
raw = wave.open("violin-C4.wav", "r")

# Extract Raw Audio from Wav File
signal = raw.readframes(-1)
signal = np.frombuffer(signal, dtype=int)

# If the audio file is Stereo exit the code
if raw.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

# get the frame rate
sample_rate = raw.getframerate()
print('Sample rate of the audio is {}'.format(sample_rate))

# get the number of frames
num_of_frames = raw.getnframes()
print('Number of frames in the audio is {}'.format(num_of_frames))

# get the duration
duration = num_of_frames/sample_rate
print('Sound clip is {} seconds long'.format(duration))

# develop t array to match x
t = np.array(range(0, len(signal)))/sample_rate


#plot the clip
plt.plot(t, signal)
#plot the small part
#plt.plot(t[500:750],signal[500:750])
plt.show()

