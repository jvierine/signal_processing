#!/usr/bin/env python3
import numpy as n
import scipy.constants as c
import matplotlib.pyplot as plt

print("Hello World!")
# test numpy
print(n.pi)

# test scipy
print(c.pi)

# test matplotlib
plt.plot(n.random.randn(10),".")
plt.show()
