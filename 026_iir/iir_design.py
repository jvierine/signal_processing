#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as n
import scipy.signal as s

import plot_h

# Design an IIR low pass filter with:
# sample-rate = 1000 Hz
# edge of the band pass = 100 Hz
# start of the band stop = 200 Hz
sample_rate=1000.0
zeros,poles,k=s.iirdesign(100.0, 200.0, gpass=1.0, gstop=100, ftype='ellip', output="zpk",fs=sample_rate)

# return the filter coefficients for the IIR filter
b,a=s.iirdesign(100.0, 200.0, gpass=1.0, gstop=100, ftype='ellip', output="ba",fs=sample_rate)

# Plot the system function and the magnitude response of the IIR filter.
plot_h.plot_hmag("ex_design.png",zeros=zeros,poles=poles,vmin=-150,fs=sample_rate)
