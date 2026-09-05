from PIL import Image
import numpy as np


def preprocess_doodle(image_data, size=384):
    """
    Convert Streamlit canvas image data into a
    square RGB image while preserving aspect ratio.
    """

    # Convert NumPy array to uint8
    image_array = image_data.astype(np.uint8)

    # Convert to PIL image
    image = Image.fromarray(image_array).convert("RGB")

    # Preserve aspect ratio
    image.thumbnail(
        (size, size),
        Image.Resampling.LANCZOS
    )

    # Create a white square background
    processed_image = Image.new(
        "RGB",
        (size, size),
        "white"
    )

    # Center image
    x = (size - image.width) // 2
    y = (size - image.height) // 2

    processed_image.paste(
        image,
        (x, y)
    )

    return processed_image