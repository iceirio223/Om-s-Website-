import tkinter as tk
from PIL import Image, ImageEnhance
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        st.error(f"Failed to load Lottie animation: {e}")
        return None

# Assets
img_calculator = Image.open("C:\\Users\\Om Prakash Patel\\Desktop\\Python projects\\Images\\calculator.png")
img_2d_snake = Image.open("C:\\Users\\Om Prakash Patel\\Desktop\\Python projects\\Images\\2d snake game .png")
img_me = Image.open("C:\\Users\\Om Prakash Patel\\Desktop\\Python projects\\Images\\IMG_ME.JPG")

# Fix the orientation by transposing it correctly
img_me = img_me.transpose(Image.Transpose.ROTATE_270)  # Rotate to correct orientation

# Enhance image clarity (increase sharpness and contrast)
enhancer = ImageEnhance.Sharpness(img_me)
img_me = enhancer.enhance(2.0)  # Increase sharpness, adjust value if needed

enhancer = ImageEnhance.Contrast(img_me)
img_me = enhancer.enhance(1.2)  # Adjust contrast to make image clearer

# Replace with a valid Lottie JSON URL
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json")

# Header section
with st.container():
    # Create two columns: one for text and one for the image
    header_column, img_column = st.columns([2, 1])
    with header_column:
        st.subheader("Hi, I am Om Prakash Patel :wave:")
        st.title("Undergrad student studying at University of Cincinnati")
        st.write("I am passionate about computers and software development")
        st.write("[Learn More >](https://www.linkedin.com/in/om-prakash-patel-a95746175/)")
    
    with img_column:
        st.image(img_me, width=200)  # Adjust the width as needed

# Content section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("ABOUT ME")
        st.write("##")
        st.write(
            """
            Hello! My name is Om Prakash Patel, and I’m 17 years old, born on February 22, 2007. My fascination with computers began at a young age, inspired by my father, a dedicated computer professional.
            Watching him work not only sparked my interest in technology but also taught me the value of focus and perseverance in achieving my goals.
            Fueled by this passion, I decided to pursue a degree in Computer Science. I completed my high school education at Credence High School and am currently a Computer Science student at the University of Cincinnati.
            I take pride in being a skilled programmer and constantly strive to improve my craft. Technology excites me, and I look forward to building innovative solutions that make a difference.
            """
        )
        st.write("[<Handshake Profile>](https://uc.joinhandshake.com/profiles/xduucf)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("FEW OF MY PROJECTS")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2d_snake)
    with text_column:
        st.subheader("Fully functional snake game")
        st.write(
            """
            I developed a fully functional Snake game in C++ as a fun and challenging coding project.
            It features smooth gameplay, dynamic movement, and a scoring system, all built using fundamental programming concepts like loops, arrays, and simple graphics.
            This project was a great opportunity to enhance my problem-solving skills and deepen my understanding of game development in C++.

            """
        )
        st.markdown("[Code on Github](https://github.com/iceirio223)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_calculator)
    with text_column:
        st.subheader("Scientific Calculator with GUI purely built on Python")
        st.write(
             """
            A Python-based scientific calculator featuring a sleek and user-friendly Tkinter GUI.
            It supports basic arithmetic operations as well as advanced scientific functions like square root, trigonometry (sin, cos, tan), logarithms, and powers.
            With its clean interface and smooth functionality, it’s an ideal tool for both students and professionals who need quick and accurate calculations.

            """
        )
        st.markdown("[Code on Github](https://github.com/iceirio223)")

# Contact Section
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/ompat07@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty() 

# Use CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
