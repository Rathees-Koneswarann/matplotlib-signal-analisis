import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa
import IPython.display as ipd
x, sr = librosa.load('violin-C4.wav')
x = x[0:(3*sr)+1]
t = np.array(range(0, len(x)))/sr
c = np.fft.fft(x)
fr = np.array(range(0,66151))/3

fig, ax = plt.subplots(figsize=(20,8))
condition = (fr >0) & (fr < 1800)
plt.plot(fr[condition],np.abs(c[condition]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amblitude')
plt.show()