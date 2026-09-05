import torch
from diffusers import (
    ControlNetModel,
    StableDiffusionControlNetPipeline
)


def load_model():

    # Your system uses CPU
    device = "cpu"

    print("Loading AI model...")
    print(f"Using device: {device}")

    # Load Scribble ControlNet
    controlnet = ControlNetModel.from_pretrained(
        "lllyasviel/control_v11p_sd15_scribble",
        torch_dtype=torch.float32
    )

    # Load Stable Diffusion
    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        controlnet=controlnet,
        torch_dtype=torch.float32,
        safety_checker=None
    )

    # Move model to CPU
    pipe = pipe.to(device)

    print("Model loaded successfully!")

    return pipe