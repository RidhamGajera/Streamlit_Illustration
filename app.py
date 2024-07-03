import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
from io import BytesIO

# Function to load and cache the model
@st.cache_resource
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)
    return pipe

# Load the model
pipe = load_model()

# Streamlit app title
st.title("AI Illustration Generator")

# Prompt input
prompt = st.text_input("Enter a prompt to generate an illustration:", "A beautiful sunset over the mountains")

# Generate image button
if st.button("Generate Image"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt to generate an image.")
    else:
        with st.spinner("Generating image..."):
            # Generate image with reduced steps and guidance scale
            result = pipe(prompt, num_inference_steps=25, guidance_scale=7.5)
            image = result.images[0]

            # Convert image to bytes for display
            image_bytes = BytesIO()
            image.save(image_bytes, format="PNG")
            image_bytes.seek(0)

            # Display image
            st.image(image_bytes, caption=f"Generated Image for: '{prompt}'")

# Footer with credits
st.markdown("""
**Note**: This application uses a lightweight configuration of the Stable Diffusion model for faster performance. 
For more details, visit the [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5) page.
""")
