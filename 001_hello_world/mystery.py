#!/usr/bin/env python3
import numpy as n
import scipy.constants as c
import matplotlib.pyplot as plt

# test some complex numpy functions
x=n.linspace(-2.5,1.5,num=2000)
y=n.linspace(-2,2,num=2000)
cx,cy=n.meshgrid(x,y)
c=cx+1j*cy
z=n.zeros(c.shape,dtype=n.complex64)
for iteration in range(12):
    z=z**2+c
z[n.isnan(z)]=0.0
z[n.isinf(z)]=0.0
# test plotting the phase of a complex number
plt.imshow(n.angle(z),extent=[-2,2,-2,2],cmap="hsv")
plt.colorbar()
plt.xlabel("$\mathrm{Re}\{z\}$")
plt.ylabel("$\mathrm{Im}\{z\}$")
plt.show()
