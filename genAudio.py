from transformers import AutoProcessor


def genaud(input_string, model, device):
    model.to(device)
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")

    inputs = processor(
        text=input_string,
        padding=True,
        return_tensors="pt",
    )

    audio_values = model.generate(**inputs.to(device), do_sample=True, guidance_scale=3, max_new_tokens=256)
    aud_values = audio_values[0].cpu().numpy()
    # print(aud_values)
    return aud_values

