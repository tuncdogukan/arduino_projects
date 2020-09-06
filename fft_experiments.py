# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:23:04 2019

@author: dtunc
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pylab as pl
from IPython import display
import time as ttime
import random
from mpl_toolkits.mplot3d import Axes3D

## illustration of the effect of phase offsets on dot products

srate = 1000;
time  = np.arange(-1.,1.,1./srate)

# create complex sine wave
csw = np.exp( 1j*2*np.pi*5*time )
rsw = np.sin(    2*np.pi*5*time )


# specify range of phase offsets for signal
phases = np.linspace(0,7*np.pi/2,num=100)


for phi in range(0,len(phases)):
    
    # create signal
    sinew  = np.sin(2*np.pi*5*time + phases[phi])
    gauss  = np.exp( (-time**2) / .1)
    signal = np.multiply(sinew,gauss)

    # compute complex dot product
    cdp = np.sum( np.multiply(signal,csw) ) / len(time)

    # compute real-valued dot product
    rdp = sum( np.multiply(signal,rsw) ) / len(time)

    # plot signal and real part of sine wave
    pl.cla() # wipe the figure
    plt.subplot2grid((2,2), (0, 0), colspan=2)
    plt.plot(time,signal)
    plt.plot(time,rsw)
    plt.title('Signal and sine wave over time')

    # plot complex dot product
    plt.subplot2grid((2,2), (1, 0))
    plt.plot(np.real(cdp),np.imag(cdp),'ro')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.axis('square')
    plt.grid(True)
    plt.axis([-.2,.2,-.2,.2])
    plt.plot([0,np.real(cdp)],[0,np.imag(cdp)],'r')


    # draw normal dot product
    plt.subplot2grid((2,2), (1, 1))
    plt.plot(rdp,0,'ro')
    plt.xlabel('Real')
    plt.axis('square')
    plt.grid(True)
    plt.axis([-.2,.2,-.2,.2])


    # show plot    
    display.clear_output(wait=True)
    display.display(pl.gcf())
    ttime.sleep(.01)
    
#%%

# with a signal

# phase of signal
theta = 2*np.pi/4;


# simulation parameters
srate = 1000;
time  = np.arange(-1,1,1/srate)

# signal
sinew  = np.sin(2*np.pi*5*time + theta)
gauss  = np.exp( (-time**2) / .1);
signal = np.multiply(sinew,gauss)

# sine wave frequencies
sinefrex = np.arange(2.,10.,.5);

# plot signal
plt.plot(time,signal)
plt.xlabel('Time (sec.)'), plt.ylabel('Amplitude (a.u.)')
plt.title('Signal')
plt.show()



# initialize dot products vector
dps = np.zeros(len(sinefrex));

# loop over sine waves
for fi in range(1,len(dps)):
    
    # create sine wave
    sinew = np.sin( 2*np.pi*sinefrex[fi]*time)
    
    # compute dot product
    dps[fi] = np.dot( sinew,signal ) / len(time)


# and plot
plt.stem(sinefrex,dps)
plt.xlabel('Sine wave frequency (Hz)'), plt.ylabel('Dot product')
plt.title('Dot products with sine waves')
plt.show()



#%% GELELİM ŞU BİZİM İŞE

srate = 10000 # sampling rate in Hz
time  = np.arange(0,10) # time in seconds

# sine wave param.eters
freq = 50   # frequency in Hz
ampl = 2    # amplitude in a.u.
phas = 0 #np.pi/3; # phase in radians

# generate the sine wave
sinewave = ampl * np.sin( 2*np.pi * freq * time + phas )

plt.plot(time,sinewave,'k')
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude (a.u.)')
plt.show() 

#for x in sinewave:
#    print(x)    

fftOut = np.fft.fft(sinewave)

for x in range(len(fftOut)):
    if abs(fftOut[x] > 0.1):
        print(x, " - " ,abs(fftOut[x])) 
