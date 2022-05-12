import streamlit as st
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def main_info(data):
    st.subheader("Imported image")
    st.image(data)
    st.subheader("Image adjustment")

def resolution (image):
    width, height = image.size
    return width, height

def param_input ():
    res_increase = st.number_input("Increase final image resolution by:",0.0,10.0,step=0.5, value=2.0)
    col1, col2 = st.columns(2)
    font_size = col1.slider("ASCII font size", 0, 20, step=1, value=10)
    new_width = col2.number_input("Width adjustment", 0, 1000, value=220)
    return res_increase,font_size, new_width

def chars_selection ():
    invert = st.checkbox("Invert")
    if invert:
        chars = ["B","S","#","&","@","$","%","*","!",":","."," "]
        return  chars
    else:
        chars = [' ', '.', ':', '!', '*', '%', '$', '@', '&', '#', 'S', 'B']
        return chars

def imagetransformer (img, new_width, chars):
    width, height = img.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width *0.55
    img = img.resize((new_width, int(new_height)))
    img = img.convert('L')
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    return ascii_image

def image_maker (x_res, y_res, font_size, txt, color):
    font = ImageFont.truetype("./fonts/courier.ttf", font_size)
    img = Image.new('RGB', (x_res, y_res), color=(30,30,30))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), txt,(color,color,color), font=font)
    return img

def final_image(final_image):
    st.subheader("Final image")
    st.image(final_image)
    name = st.text_input("Final image name", value="My ASCII image")
    save = st.button("Save")
    if save:
        final_image = final_image.save("./saved_images/" + name + ".png")