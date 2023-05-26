import numpy as np
import matplotlib.pyplot as plt

# Generate a time domain signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

# Compute the phase spectrum
phase_spectrum = np.angle(np.fft.fft(signal))

# Plot the phase spectrum
plt.plot(phase_spectrum)
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.show()
