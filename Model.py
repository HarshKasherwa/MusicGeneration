from transformers import MusicgenForConditionalGeneration
import pickle


def download(path):
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    # path = "C:\\Users\\hkkas\\PycharmProjects\\HCLHackathon\\models\\GenAudioModel.pkl"
    with open(path, 'wb') as file:
        pickle.dump(model, file)