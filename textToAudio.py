import os

from scipy.io.wavfile import write
import numpy as np
import time
from RW import read


def getAudio(a_data, s_rate, name):

    ts = time.time()
    name = "MG"+str(int(ts))
    name = name + ".wav"

    path = os.getcwd()
    path = os.path.join(path, "static", "audioFiles")
    path = os.path.join(path, name)

    a_data = a_data.squeeze()
    if a_data.dtype == np.int16:
        a_data = a_data.astype(np.float32) / 32768.0
    elif a_data.dtype == np.float32:
        a_data = np.clip(a_data, -1.0, 1.0)

    write(path, s_rate, a_data)
    return name


# audio_data = read()
# sample_rate = 32000
# path = "/static/audioFiles/"
# # print(os.path.join(path, "trial.wav"))
# print(getAudio(audio_data, sample_rate, "trial"))
# # print(os.getcwd())
