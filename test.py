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


plt.figure(figsize=(20,5))
condition = (fr >259) & (fr < 270)
plt.plot(fr[condition],np.angle(c[condition]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase')
plt.show()