from transformers import MusicgenForConditionalGeneration
import pickle
import os


def download():
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    model_name = "Gen_audio_model.pkl"
    path = os.getcwd()
    path = os.path.join(path, "models")
    path = os.path.join(path, model_name)
    with open(path, 'wb') as file:
        pickle.dump(model, file)