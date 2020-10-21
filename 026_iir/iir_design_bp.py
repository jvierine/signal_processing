#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as n
import scipy.signal as s

import plot_h

# Design an IIR band-pass filter with:
# sample-rate = 1000 Hz
# pass band = 100 to 300 Hz
# maximum pass band ripple 1 dB
# minimum attenuation of signals out of band = 100 dB
sample_rate=1000.0
zeros,poles,k=s.iirdesign(100,200, gpass=3.0, gstop=100, ftype='ellip', output="zpk",fs=sample_rate)
b,a=s.iirdesign(100,200, gpass=3.0, gstop=100, ftype='ellip', output="ba",fs=sample_rate)

# create a white noise signal
signal = n.random.randn(100000)

# filter signal with the IIR filter specified with
# coefficients b and a
filtered_signal=s.lfilter(b,a,signal)

# plot the power spectrum estimate
plt.psd(filtered_signal,NFFT=1024,Fs=sample_rate)
plt.savefig("ex_pdf_lp.png")
plt.show()

# Plot the system function and the magnitude response of the IIR filter.
plot_h.plot_hmag("ex_design_lp.png",zeros=zeros,poles=poles,vmin=-150,fs=sample_rate)
