import numpy as np
import matplotlib.pyplot as plt

# Generate a time domain signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 50 * t)

# Generate a filter
filter_freq = np.fft.fftfreq(len(signal), d=t[1]-t[0])
filter_freq[np.abs(filter_freq) > 20] = 0

# Apply the filter in frequency domain
filtered_signal = np.fft.ifft(np.fft.fft(signal) * filter_freq)

# Plot the filtered signal
plt.plot(filtered_signal.real)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
