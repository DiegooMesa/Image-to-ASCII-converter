import functions as func
import streamlit as st
from PIL import Image

st.header("Image to ASCII converter")
data = st.file_uploader("Upload image", type=['png', 'jpg'])
if data is not None:
    func.main_info(data)
    data = Image.open(data)
    width, height = func.resolution(data)
    res_increase, font_size, new_width = func.param_input()
    chars = func.chars_selection()
    final_image = func.image_maker (int(width*res_increase), int(height*res_increase), font_size, 
            func.imagetransformer(data, new_width, chars), 255)
    func.final_image(final_image)
    
    