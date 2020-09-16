import scipy.io.wavfile as sw
import numpy as n
import matplotlib.pyplot as plt
# read wav file
ts=sw.read("7na.wav")
sr=ts[0]     # sample rate
clip=ts[1]  # extract audio file as numpy data vector
if len(clip.shape)==2: # if stereo, only use one channel
    print("converting to mono")
    clip=ts[1][:,0]+ts[1][:,1]

print(clip.shape)
# if clip is too long, make it shorter (1 million samples)
if len(clip)>1000000:
    clip=clip[0:1000000]
# compress and decompress audio file
# compression_ratio=0.95 means 95% reduction in 
# file size. 
cr=0.95

print(len(clip))

# Fourier transform
F = n.fft.fft(clip)
F_orig=n.copy(F)

# what is the magnitude of each spectral component
mag=n.abs(F)

# sort by magnitude
idx=n.argsort(n.abs(F))
# figure out what is the smallest component that we'll include
print(idx[int(cr*float(len(idx)))])
smallest_comp=mag[idx[int(cr*len(idx))]]
print(smallest_comp)
print(n.max(mag))

# remove spectral components with magnitude less than smallest_comp
F[mag < smallest_comp]=0.0

# inverse Fourier transform to obtain signal composed of just a few spectral components
compressed=n.real(n.fft.ifft(F))

print("Plotting")
# plot the spectrum
freq_vec=n.fft.fftshift(n.fft.fftfreq(len(F),d=1/float(sr)))
plt.plot(freq_vec/1e3,n.fft.fftshift(10.0*n.log10(n.abs(F_orig)**2.0)),label="Original")
plt.xlim([0,float(sr)/1e3/2.0])
plt.plot(freq_vec/1e3,n.fft.fftshift(10.0*n.log10(n.abs(F)**2.0)),label="Compressed")
plt.legend()
plt.xlabel("Frequency (kHz)")
plt.ylabel("Power (dB)")
plt.title("Spectrum")
plt.show()

# plot the first 10000 samples
time_vec=n.arange(len(clip))/float(sr)
plt.title("Waveform")
plt.plot(time_vec[0:10000]*1e3,clip[0:10000],label="Original")
plt.plot(time_vec[0:10000]*1e3,compressed[0:10000],label="Compressed")
plt.legend()
plt.xlabel("Time (ms)")
plt.ylabel("Audio waveform")
plt.show()

# Save result as wav file so that we can easily listen to the audio
# quality after decompression of the compressed signal.

# scale numbers to 0..1 scale
compressed = compressed/(1.05*n.max(compressed))
print("Saving spectrally sparse signal to file compressed_signal.wav")
sw.write("compressed_signal.wav",44100,n.array(20e3*compressed,dtype=n.int16))
