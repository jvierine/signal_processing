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
zeros,poles,k=s.iirfilter(10, [100,300], rp=1.0, rs=100, ftype='ellip', output="zpk",fs=sample_rate)

# Plot the system function and the magnitude response of the IIR filter.
plot_h.plot_hmag("ex_design.png",zeros=zeros,poles=poles,vmin=-150,fs=sample_rate)
