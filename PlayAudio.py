from IPython.display import Audio


def play(model, values):
    sampling_rate = model.config.audio_encoder.sampling_rate
    Audio(values[0].cpu().numpy(), rate=sampling_rate)
