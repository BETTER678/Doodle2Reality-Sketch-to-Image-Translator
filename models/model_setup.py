import torch
from diffusers import (
    ControlNetModel,
    StableDiffusionControlNetPipeline
)


def load_model():

    # Detect available device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # CUDA can efficiently use FP16.
    # CPU should use FP32.
    dtype = (
        torch.float16
        if device == "cuda"
        else torch.float32
    )

    print("=" * 50)
    print("Loading Doodle2Reality AI Model")
    print(f"Device: {device}")
    print(f"Data type: {dtype}")
    print("=" * 50)

    # Load ControlNet Scribble
    controlnet = ControlNetModel.from_pretrained(
        "lllyasviel/control_v11p_sd15_scribble",
        torch_dtype=dtype,
        low_cpu_mem_usage=True
    )

    # Load Stable Diffusion + ControlNet
    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        controlnet=controlnet,
        torch_dtype=dtype,
        low_cpu_mem_usage=True
    )

    # Move pipeline to selected device
    pipe = pipe.to(device)

    # Reduce memory usage
    pipe.enable_attention_slicing()

    # CPU optimizations
    if device == "cpu":

        # Use available CPU cores efficiently
        torch.set_grad_enabled(False)

        print("CPU mode enabled.")
        print("Generation may take some time.")

    print("=" * 50)
    print("Model loaded successfully!")
    print("=" * 50)

    return pipe