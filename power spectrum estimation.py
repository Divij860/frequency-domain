import numpy as np
import matplotlib.pyplot as plt

# Generate a time domain signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Compute the power spectrum
power_spectrum = np.abs(np.fft.fft(signal))**2

# Plot the power spectrum
plt.plot(power_spectrum)
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.show()
