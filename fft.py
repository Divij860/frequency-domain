import numpy as np
import matplotlib.pyplot as plt

# Generate a time domain signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Compute the FFT
fft = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), d=t[1]-t[0])

# Plot the frequency spectrum
plt.plot(freq, np.abs(fft))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()
