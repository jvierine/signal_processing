#!/usr/bin/env python


import numpy as n
import matplotlib.pyplot as plt

def frequency_response(h,sample_idx,omhat):
    H=n.zeros(len(omhat),dtype=n.complex64)
    for idx in range(len(h)):
        H+=h[idx]*n.exp(-1j*sample_idx[idx]*omhat)
    return(H)
        
# impulse response
h=n.array([1.0,1.0,-1.0,-1.0])
# a sweep of -\pi to \pi in normalized angular frequency
omhat = n.linspace(-n.pi,n.pi,num=500)

H=frequency_response(h,n.arange(len(h)),omhat)

plt.figure(figsize=(0.8*6,0.8*8))
plt.subplot(211)
plt.plot(omhat,n.abs(H))
plt.title("Magnitude response")
plt.ylabel("$|\\mathcal{H}(\hat{\omega})|$")
plt.xlabel("$\hat{\omega}$")
plt.subplot(212)
plt.title("Phase response")
plt.plot(omhat,n.angle(H))
plt.xlabel("$\hat{\omega}$")
plt.ylabel("$\\angle\\mathcal{H}(\hat{\omega})$")
plt.tight_layout()
plt.show()
