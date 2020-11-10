#!/usr/bin/env python

import numpy as n
import matplotlib.pyplot as plt
import scipy.signal as s

# create dynamic spectrum
def spectrogram(x,M=1024,N=128,delta_n=100):
    """
    x = signal
    M = FFT length
    N = window function length
    delta_n = step step
    """
    max_t=int(n.floor((len(x)-N)/delta_n))
    t=n.arange(max_t)
    X=n.zeros([max_t,M],dtype=n.complex64)
    w=s.hann(N)
    xin=n.zeros(N)
    for i in range(max_t):
        # zero padded windowed FFT
        xin[0:N]=x[i*delta_n+n.arange(N)]
        X[i,:]=n.fft.fft(w*xin,M)
    return(X)

# sample rate (Hz)
fs=4096.0

# sample indices (one second of signal)
nn=n.arange(4096)
# generate a chirp signal
x=n.sin(0.15e-14*nn**5.0)

# alternatively, you can use the matplotlib
# implementation
mspec,mfreq,mt,mim=plt.specgram(x,NFFT=128,pad_to=2048,noverlap=128-25,Fs=fs,scale="dB",vmin=-50,vmax=-20)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar()
plt.show()
