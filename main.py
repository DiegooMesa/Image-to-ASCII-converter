from types import NoneType
import functions as func
import streamlit as st
from PIL import Image

st.header("Image to ASCII converter")
data = st.file_uploader("Upload image", type=['png', 'jpg'])
if data is not None:
    st.subheader("Imported image")
    st.image(data)
    st.subheader("Image adjustment")
    data = Image.open(data)
    width, height = func.resolution(data)
    res_increase, font_size, new_width = func.param_input()
    chars = func.chars_selection()

    final_image = func.image_maker (int(width*res_increase), int(height*res_increase), font_size, func.imagetransformer(data, new_width, chars), 255)
    st.subheader("Final image")
    st.image(final_image)
    name = st.text_input("Final image name", value="My ASCII image")
    save = st.button("Save")
    if save:
        final_image = final_image.save("./saved_images/" + name + ".png")
    