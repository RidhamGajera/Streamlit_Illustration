# AI Illustration Generator

This is a Streamlit application that uses the Stable Diffusion model to generate AI illustrations based on text prompts. Users can input a descriptive prompt and receive a generated image in response.

## Features

- Enter a text prompt to generate an AI illustration.
- Optimized for faster performance with CUDA support if available.
- Streamlined and user-friendly interface.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RidhamGajera/Streamlit_Illustration
   cd AI-Illustration-Generator

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

streamlit run app.py
