import numpy as np
from scipy.io.wavfile import write
from RW import read

rate = 32000
data = read()
scaled = np.int16(data / np.max(np.abs(data)) * 32767)
write('test.wav', rate, scaled)