import csv

from Caller import get_aud_data
import numpy as np

path2 = "C:\\Users\\hkkas\\PycharmProjects\\HCLHackathon\\audioData\\audData.npy"


def write():
    input_string = "80s pop track with bassy drums and synth"
    aud_val = get_aud_data(input_string)
    print(aud_val.shape)
    np.save(path2, aud_val)


def read():
    aud_data = np.load(path2)
    return aud_data

