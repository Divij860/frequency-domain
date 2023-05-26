import numpy as np
import matplotlib.pyplot as plt

# Generate two signals
t = np.linspace(0, 1, 1000)
signal1 = np.sin(2 * np.pi * 10 * t)
signal2 = np.sin(2 * np.pi * 10 * t + np.pi/4)

# Compute the cross-correlation using FFT
cross_corr = np.fft.ifft(np.fft.fft(signal1) * np.conj(np.fft.fft(signal2)))

# Plot the cross-correlation result
plt.plot(cross_corr.real)
plt.xlabel('Time Lag')
plt.ylabel('Correlation')
plt.show()
