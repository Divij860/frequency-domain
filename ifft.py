import numpy as np
import matplotlib.pyplot as plt

# Generate a frequency domain signal
freq = np.fft.fftfreq(1000, d=1/1000)
spectrum = np.fft.fftshift(np.exp(-freq**2 / 0.2))

# Compute the IFFT
signal = np.fft.ifft(spectrum)

# Plot the time domain signal
plt.plot(signal.real)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
