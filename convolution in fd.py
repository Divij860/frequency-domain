import numpy as np
import matplotlib.pyplot as plt

# Generate two signals
t = np.linspace(0, 1, 1000)
signal1 = np.sin(2 * np.pi * 10 * t)
signal2 = np.exp(-t)

# Compute the convolution using FFT
convolution = np.fft.ifft(np.fft.fft(signal1) * np.fft.fft(signal2))

# Plot the convolution result
plt.plot(convolution.real)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
