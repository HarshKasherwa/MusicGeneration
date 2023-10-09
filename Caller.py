import torch
from loadModel import load
from genAudio import genaud
import os


def get_aud_data(input_string):
    model_path = os.getcwd()
    model_path = os.path.join(model_path, "models", "Gen_audio_model.pkl")
    path2 = "C:\\Users\\hkkas\\Downloads\\GenAudioModel.pkl"

    # input = ["80s pop track with bassy drums and synth", "90s rock song with loud guitars and heavy drums"]
    # download()

    model = load(path2)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    aud_values = genaud(input_string, model, device)
    print(aud_values)
    return aud_values


# print(aud_values)

# Audio(audio_values[0].cpu().numpy(), rate=sampling_rate)