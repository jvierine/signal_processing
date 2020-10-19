#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as n

# define system function
def h(z,L=20):
    zeros=n.exp(1j*2.0*n.pi*n.arange(1,L)/L)
    H=1.0
    for i in range(len(zeros)):
        H=H*(1.0-zeros[i]*z**(-1))
    
    return(H/L)

    

omhat=n.linspace(-n.pi,n.pi,num=1000)
H=h(n.exp(1j*omhat))

plt.figure(figsize=(5,5))
plt.subplot(211)
plt.plot(omhat,n.abs(H))
plt.ylabel("$|\\mathcal{H}(\\hat{\\omega})|$")
plt.xlabel("$\hat{\omega}$")
plt.subplot(212)
plt.plot(omhat,n.angle(H))
plt.ylabel("$\\angle \\mathcal{H}(\\hat{\\omega})$")
plt.xlabel("$\\hat{\\omega}$")
plt.tight_layout()
plt.savefig("rma_magresp.png")
plt.show()
