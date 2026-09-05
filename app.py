import streamlit as st
from streamlit_drawable_canvas import st_canvas

from models.model_setup import load_model
from utils.preprocess import preprocess_doodle


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Doodle2Reality",
    page_icon="🎨",
    layout="wide"
)


# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🎨 Doodle2Reality")
st.subheader("Sketch-to-Image Translator")

st.write(
    "Draw anything and describe it. "
    "AI will transform your doodle into a realistic image."
)


# -------------------------------------------------
# Load AI Model
# -------------------------------------------------

@st.cache_resource
def get_model():
    return load_model()


# -------------------------------------------------
# User Description
# -------------------------------------------------

description = st.text_input(
    "What did you draw?",
    placeholder="Example: A realistic red sports car on a mountain road"
)


# -------------------------------------------------
# Drawing Canvas
# -------------------------------------------------

st.write("### ✏️ Draw your doodle")

canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",
    stroke_width=5,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=500,
    width=700,
    drawing_mode="freedraw",
    key="drawing_canvas",
)


# -------------------------------------------------
# Generate Button
# -------------------------------------------------

if st.button("✨ Generate Reality"):

    if canvas_result.image_data is None:

        st.warning("Please draw something first!")

    else:

        # Process the doodle
        doodle = preprocess_doodle(
            canvas_result.image_data
        )

        # Get the user prompt
        prompt = description.strip()

        if not prompt:
            prompt = "a highly realistic photograph based on this sketch"

        # Show input
        st.write("### ✏️ Input Doodle")

        st.image(
            doodle,
            caption="Processed Doodle",
            width=400
        )

        # Load model
        with st.spinner("🧠 Loading AI model..."):

            pipe = get_model()

        # Generate image
        with st.spinner(
            "🎨 Generating realistic image... "
            "This may take a long time on CPU."
        ):

            result = pipe(
                prompt=prompt,
                image=doodle,
                num_inference_steps=10,
                guidance_scale=7.5
            )

        generated_image = result.images[0]

        # Show generated image
        st.success("Image generated successfully!")

        st.write("## 📸 Generated Reality")

        st.image(
            generated_image,
            use_container_width=True
        )