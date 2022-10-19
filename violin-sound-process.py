# %% [markdown]
# # GP 112 ACTIVITY 17

# %% [markdown]
# ## Import the modules

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline

# %%
import librosa
import IPython.display as ipd

# %% [markdown]
# ## Import the audio

# %%
#load .wav sound file
#sr = sample rate = #sam[le per second, 22050 Hz
x, sr = librosa.load('violin-C4.wav')
x = x[0:(3*sr)+1]
print(type(x))
print('x length: {}'.format(len(x)))
print(type(sr))
print('sr = {}'.format(sr))

# %%
# confirm the audio sample length
print('Sound clip is {} seconds long.'.format((len(x)-1)/sr))

# %% [markdown]
# ## Plot the graph in time domain

# %%
plt.figure(figsize=(20,8))
# Develop array 't to match x
t = np.array(range(0, len(x)))/sr
#plt.plot(t,x)
plt.plot(t[2000:3000],x[2000:3000])
plt.xlabel('Time (seconds)')
plt.ylabel('Pressure')

# %% [markdown]
# ## Embad the audio

# %%
ipd.Audio(x ,rate = sr)

# %% [markdown]
# ## Fourier transformation

# %%
# find the fourier transform
c = np.fft.fft(x)
print(type(c))
print(len(c))
#print the array of complex numbers
print(c[0:10])

# %% [markdown]
# ## Plot the Frequency vs Amlitude Graph

# %% [markdown]
# ### Graph for whole range

# %%
fr = np.array(range(0,66151))/3
# plot the absolute value
plt.figure(figsize=(20,8))
plt.plot(fr,c)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amblitude')


# %%
fr = np.array(range(0,66151))/3
# plot the absolute value
plt.figure(figsize=(20,8))
plt.plot(fr,np.abs(c))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amblitude')

# %% [markdown]
# ### Graph for specific range 

# %%
fig, ax = plt.subplots(figsize=(20,8))
condition = (fr >0) & (fr < 1800)
plt.plot(fr[condition],np.abs(c[condition]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amblitude')
ax.text(260, 1378, '(260, 1378)', size=12)
ax.text(519.7, 452, '(519.7, 452)', size=12)
ax.text(777.67, 289, '(777.67, 289)', size=12)
ax.text(1038.67, 152, '(1038.67, 152)', size=12)
ax.text(1299.66, 203, '(1299.66, 203)', size=12)
ax.text(1558.66, 120, '(1558.66, 120)', size=12)

# %% [markdown]
# ## Plot Frequency vs Phase graph

# %%
fig, ax = plt.subplots(figsize=(20,8))
condition = (fr >0) & (fr < 1800)
plt.plot(fr[condition],np.angle(c[condition]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase')
ax.text(260, 3.12, '(260, 3.12)', size=12)
ax.text(519.7, 2.99, '(519.7, 2.99)', size=12)
ax.text(777.67, 2.40, '(777.67, 2.40)', size=12)
ax.text(1038.67, 2.69, '(1038.67, 2.69)', size=12)
ax.text(1299.66, 2.09, '(1299.66, 2.09)', size=12)
ax.text(1558.66, 3.02, '(1558.66, 3.02)', size=12)

# %% [markdown]
# ### Zoomed frequency vs phase graph

# %%
fig, ax = plt.subplots(figsize=(20,8))
condition = (fr >1555) & (fr < 1565)
plt.plot(fr[condition],np.angle(c[condition]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase')
ax.text(1558.66, 3.02, '(1558.66, 3.02)', size=12)


