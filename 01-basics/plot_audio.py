import wave
import matplotlib.pyplot as plt # in cmd => pip install --user matplotlib 
import numpy as np
import sys

obj = wave.open("I Want It That Way.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples/sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
plt.ylabel("Signal wave")
# If Stereo
if obj.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)
times = np.linspace(0, len(signal_array)/sample_freq, num=n_samples)
plt.figure(1)
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()
