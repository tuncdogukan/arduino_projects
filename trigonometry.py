# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:42:37 2019

@author: dtunc
"""

from mpmath import *
import matplotlib.pyplot as plt
import numpy as np


#%%
z = complex(3,3*sqrt(3))

hypZ = abs(z)

print(hypZ)

print(degrees(numpy.angle(z)))

#%%
m = 4
k = pi/3

complexNum = m*exp(k*1j)
complexNum = complex(complexNum)

print(type(complexNum))

ang = np.angle(complexNum)
                          
dist = abs(complexNum)

print("dist: ",dist)
print("ang: ",ang)

#%%


ampl = 1
Fs = 8000
phase = 0
f = 35
sample = 8000
x = np.arange(sample)
y = ampl * np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()

fftResult = np.fft.fft(y)

#plt.plot(fftResult)

enumerate(fftResult,1)

for x in range(len(fftResult)):
    lenComp = abs(fftResult[x])
    if lenComp > 1:
        print(lenComp, " - " , x)

#%%
srate = 300; # sampling rate in Hz
time  = np.arange(0.,2.,1./srate) # time in seconds

# sine wave param.eters
freq = 3;    # frequency in Hz
ampl = 2;    # amplitude in a.u.
phas = np.pi/3; # phase in radians

# generate the sine wave
sinewave = ampl * np.sin( 2*np.pi * freq * time + phas )

plt.plot(time,sinewave,'k')
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude (a.u.)')
plt.show() 

for x in sinewave:
    print(x)       
        
        
#%%

sinewave = ampl * np.sin( 2*np.pi * freq * time + phas )
coswave  = ampl * np.cos( 2*np.pi * freq * time + phas )

plt.plot(time,sinewave,'k',label='sine')
plt.plot(time,coswave,'r',label='cosine')
plt.xlabel('Time (sec.)'), plt.ylabel('Amplitude')
plt.title('A sine and cosine with the same parameters.')
plt.show()