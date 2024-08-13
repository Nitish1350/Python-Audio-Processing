import wave
import matplotlib.pyplot as plt
import numpy as np

# Open the wave file
obj = wave.open("rec.wav", "rb")

# Get audio parameters
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
n_channels = obj.getnchannels()

# Read frames and close the file
signal_wave = obj.readframes(-1)
obj.close()

# Calculate the total duration of the audio
t_audio = n_samples / sample_freq

# Convert the byte data to a numpy array of 16-bit integers
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

if n_channels == 2:
    signal_array = signal_array[::2]

# Generate the time axis
times = np.linspace(0, t_audio, num=n_samples)

# Plot the signal
print(len(signal_array), len(times))
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()