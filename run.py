
import numpy as np 
import matplotlib.pyplot as plt

# construct a time signal

Fs = 2000 # sampling freq
tstep = 1/Fs # sample time interval
f0 = 100 # signal freq

N = 10*Fs//f0 # number of samples

t = np.linspace(0, (N-1)*tstep, N) # time steps
fstep = Fs/N # freq interval
f= np.linspace(0, (N-1)*fstep, N) # freq steps

y = 1*np.sin(2*np.pi*f0*t) + 5*np.sin(2*np.pi*3*f0*t)

# perform fft
x = np.fft.fft(y)
x_mag = np.abs(x) / N

f_plot = f[0:int(N/2+1)]
x_mag_plot = 2*x_mag[0:int(N/2+1)]
x_mag_plot[0] = x_mag_plot[0]/2 # Note: DC component does not need to multiply by tow


#plot
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t,y, '.-')
ax2.plot(f_plot,x_mag_plot, '.-')
ax1.set_xlabel("time (s)")
ax2.set_xlabel("freq (Hz)")
ax1.grid()
ax2.grid()

plt.show()
