
import numpy as np 
import matplotlib.pyplot as plt

# construct a time signal

Fs = 2000 # sampling freq
tstep = 1/Fs # sample time interval
f0 = 100 # signal freq

N = Fs//f0 # number of samples

t = np.linspace(0, (N-1)*tstep, N) # time steps
fstep = Fs/N # freq interval
f= np.linspace(0, (N-1)*fstep, N) # freq steps

y = 1*np.sin(2*np.pi*f0*t)




#plot
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(t,y)
plt.show()
