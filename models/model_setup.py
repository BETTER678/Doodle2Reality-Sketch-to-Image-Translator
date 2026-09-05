import torch
from diffusers import (
    ControlNetModel,
    StableDiffusionControlNetPipeline
)


def load_model():

    device = "cuda" if torch.cuda.is_available() else "cpu"

    dtype = (
        torch.float16
        if device == "cuda"
        else torch.float32
    )

    print(f"Using device: {device}")

    controlnet = ControlNetModel.from_pretrained(
        "lllyasviel/control_v11p_sd15_scribble",
        torch_dtype=dtype
    )

    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        controlnet=controlnet,
        torch_dtype=dtype
    )

    pipe = pipe.to(device)

    pipe.enable_attention_slicing()

    print("Model loaded successfully!")

    return pipe