import streamlit as st
import sys
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def resolution (image):
    width, height = image.size
    return width, height

def param_input ():
    res_increase = st.number_input("Increase final image resolution by:",0.0,10.0,step=0.5, value=2.0)
    font_size = st.slider("ASCII font size", 0, 20, step=1, value=10)
    new_width = st.number_input("Width adjustment", 0, 1000, value=220)
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
    #img = Image.open(url)
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
    #print (width, height)
    return ascii_image

def image_maker (x_res, y_res, font_size, txt, color):
    font = ImageFont.truetype("./fonts/courier.ttf", font_size)
    img = Image.new('RGB', (x_res, y_res), color=(30,30,30))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), txt,(color,color,color), font=font)
    return img