import numpy as np
import matplotlib.pyplot as plt

# Generate a time domain signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

# Compute and plot the spectrogram
plt.specgram(signal, Fs=1000)
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
plt.show()
