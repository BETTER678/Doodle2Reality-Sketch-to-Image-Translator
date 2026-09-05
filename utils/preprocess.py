from PIL import Image
import numpy as np


def preprocess_doodle(image_data, size=512):
    """Convert Streamlit canvas data into a resized RGB image."""
    image_array = image_data.astype(np.uint8)
    image = Image.fromarray(image_array).convert("RGB")
    image = image.resize((size, size))

    return image