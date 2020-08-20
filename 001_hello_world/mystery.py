#!/usr/bin/env python3
import numpy as n
import scipy.constants as c
import matplotlib.pyplot as plt

# test some functions
x=n.linspace(-2,2,num=2000)
cx,cy=n.meshgrid(x,x)
c=cx+1j*cy
z=n.zeros(c.shape,dtype=n.complex64)
for n_iterations in range(100):
    z=z**2+c

plt.imshow(n.abs(z),extent=[-2,2,-2,2],vmin=0,vmax=1,cmap="plasma")
plt.colorbar()
plt.xlabel("$\mathrm{Re}\{z\}$")
plt.ylabel("$\mathrm{Im}\{z\}$")
plt.show()
