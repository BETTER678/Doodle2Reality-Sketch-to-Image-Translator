# 🎨 Doodle2Reality – Sketch-to-Image Translator

Doodle2Reality is an AI-powered application that transforms rough hand-drawn sketches into realistic images.

Users can draw an object, scene, or concept on a canvas and provide a text description. The application uses **ControlNet + Stable Diffusion** to generate a realistic image while following the structure of the user's doodle.

---

## ✨ Features

- 🎨 Interactive drawing canvas
- 🧠 AI-powered sketch-to-image generation
- ✏️ Supports different types of doodles
- 📝 Text description for better results
- 🤖 ControlNet Scribble for sketch guidance
- 📸 Stable Diffusion for realistic image generation
- ⚡ GPU acceleration using CUDA
- 🖥️ CPU fallback
- 🧠 Cached AI model for faster repeated generations
- ⬇️ Download generated images
- 🌐 Streamlit web interface

---

## 🏗️ Project Architecture

```text
USER
  ↓
🎨 DRAW A DOODLE
  ↓
STREAMLIT WEB APP
  ↓
✏️ SKETCH + 📝 PROMPT
  ↓
PREPROCESSING
  ↓
CONTROLNET SCRIBBLE
  ↓
STABLE DIFFUSION
  ↓
📸 REALISTIC IMAGE
```

---

## 🤖 AI Models Used

### ControlNet Scribble

```text
lllyasviel/control_v11p_sd15_scribble
```

ControlNet helps the AI understand the structure and lines of the user's doodle.

### Stable Diffusion

```text
runwayml/stable-diffusion-v1-5
```

Stable Diffusion generates the final realistic image.

---

## 📁 Project Structure

```text
Doodle2Reality-Sketch-to-Image-Translator/
│
├── app.py
├── test_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── model_setup.py
│
├── utils/
│   └── preprocess.py
│
└── outputs/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BETTER678/Doodle2Reality-Sketch-to-Image-Translator.git
cd Doodle2Reality-Sketch-to-Image-Translator
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🖥️ Check GPU

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

Check GPU name:

```bash
python -c "import torch; print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CUDA unavailable')"
```

Example:

```text
Tesla T4
```

---

## 🚀 Run the Application

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🎨 How to Use

1. Open the application.
2. Draw something on the canvas.
3. Describe what you drew.
4. Click **✨ Generate Reality**.
5. Wait for AI generation.
6. Download the generated image.

Example prompt:

```text
A realistic red sports car driving on a mountain road
```

---

## ⚡ GPU Acceleration

The application automatically detects CUDA:

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

For the best performance, use an NVIDIA GPU.

---

## ☁️ Google Colab

Enable GPU:

```text
Runtime → Change runtime type → Hardware accelerator → GPU
```

Clone the repository:

```python
!git clone https://github.com/BETTER678/Doodle2Reality-Sketch-to-Image-Translator.git
```

Enter the project folder:

```python
%cd /content/Doodle2Reality-Sketch-to-Image-Translator
```

Install dependencies:

```python
!python -m pip install -r requirements.txt
```

Verify CUDA:

```python
import torch
print(torch.cuda.is_available())

if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
```

---

## 🌐 Run Streamlit in Google Colab

```python
!python -m streamlit run app.py \
    --server.port 8501 \
    --server.address 0.0.0.0 \
    > /content/streamlit.log 2>&1 &
```

A tunnel service can be used to access the Streamlit application from a browser.

---

## 🧪 Test the AI Model

```bash
python test_model.py
```

Expected output:

```text
Starting model test...
Using device: cuda
Model loaded successfully!
AI model loaded successfully!
```

---

## ⏱️ Performance

Performance depends on hardware:

| Hardware | Performance |
|---|---|
| CPU | Very slow |
| NVIDIA GPU | Faster |
| Tesla T4 | Much faster |
| High-end GPU | Faster |

The first run may take longer because the AI models need to be downloaded. After downloading, they are cached.

---

## 🔧 Technologies Used

- Python
- Streamlit
- PyTorch
- Diffusers
- Hugging Face
- Stable Diffusion
- ControlNet
- Pillow
- NumPy
- Streamlit Drawable Canvas

---

## 🎯 Project Goal

Doodle2Reality allows users to express ideas through simple sketches.

```text
Simple Doodle
      +
Text Description
      ↓
Artificial Intelligence
      ↓
Realistic Image
```

The project is designed to support many types of objects, scenes, and concepts rather than being limited to cats, dogs, shoes, or faces.

---

## 🚧 Future Improvements

- 🎨 Better UI and UX
- 🖼️ Multiple image variations
- 🎭 Different artistic styles
- 🌄 Background generation
- 🧠 Improved prompt handling
- 📱 Mobile-friendly design
- ☁️ Permanent cloud deployment
- ⚡ Faster inference
- 🖌️ Image editing
- 💾 Generation history
- 🔐 User authentication
- 🚀 API backend

---

## 📜 License

This project is created for educational and experimental purposes.

Please review the licenses and terms of the pretrained models before deploying publicly.

---

## 👨‍💻 Author
Srushti Khillare

GitHub Repository:

[https://github.com/BETTER678/Doodle2Reality-Sketch-to-Image-Translator](https://github.com/BETTER678/Doodle2Reality-Sketch-to-Image-Translator)

---

## ⭐ Acknowledgements

Thanks to:

- Hugging Face
- PyTorch
- Diffusers
- Stable Diffusion
- ControlNet
- Streamlit

---

# 🎨 Doodle2Reality

```text
✏️ DRAW
   ↓
🧠 AI
   ↓
📸 REALITY
```

**Turn your imagination into reality.**
