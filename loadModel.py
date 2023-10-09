from transformers import MusicgenForConditionalGeneration
import pickle


def load(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model
