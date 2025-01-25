import requests
from PIL import Image
import io
import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Function to load Lottie animations from a URL
def load_lottieurl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        st.error(f"Failed to load Lottie animation: {e}")
        return None

# URLs for the images
img_calculator_url = "https://i.imgur.com/rFMKi1d.png"
img_2d_snake_url = "https://i.imgur.com/e5NnR5v.png"
img_me_url = "https://i.imgur.com/zZddBuc.jpeg"

# Header Section
with st.container():
    header_column, img_column = st.columns([2, 1])
    with header_column:
        st.subheader("Hi, I am Om Prakash Patel :wave:")
        st.title("Undergrad student studying at University of Cincinnati")
        st.write("I am passionate about computers and software development.")
        st.write("[Learn More >](https://www.linkedin.com/in/om-prakash-patel-a95746175/)")
    with img_column:
        st.image(img_me_url)

# About Me Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("ABOUT ME")
        st.write("##")
        st.write(
            """
            Hello! My name is Om Prakash Patel, and I’m 17 years old, born on February 22, 2007. 
            My fascination with computers began at a young age, inspired by my father, a dedicated computer professional.
            Watching him work not only sparked my interest in technology but also taught me the value of focus and perseverance.
            Fueled by this passion, I decided to pursue a degree in Computer Science.
            I completed my high school education at Credence High School and am currently a Computer Science student at the University of Cincinnati.
            I take pride in being a skilled programmer and constantly strive to improve my craft.
            """
        )
        st.write("[<Handshake Profile>](https://uc.joinhandshake.com/profiles/xduucf)")
    with right_column:
        # If you want to load a Lottie animation
        # lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json")
        # if lottie_coding:
        #     st_lottie(lottie_coding, height=300, key="coding")
        pass

# Projects Section
with st.container():
    st.write("---")
    st.header("FEW OF MY PROJECTS")
    st.write("##")
    
    # Project 1: Snake Game
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_calculator_url)
    with text_column:
        st.subheader("Fully functional snake game")
        st.write(
            """
             I developed a fully functional Snake game in C++ as a fun and challenging coding project.
            It features smooth gameplay, dynamic movement, and a scoring system, all built using fundamental programming concepts.
            """
        )
        st.markdown("[Code on Github](https://github.com/iceirio223)")

    # Project 2: Scientific Calculator
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2d_snake_url)
    with text_column:
        st.subheader("Scientific Calculator with GUI purely built on Python")
        st.write(
            """
            A Python-based scientific calculator featuring a sleek and user-friendly Tkinter GUI.
            It supports basic arithmetic operations as well as advanced scientific functions like square root, trigonometry, logarithms, and powers.
            """
        )
        st.markdown("[Code on Github](https://github.com/iceirio223)")

# Contact Section with Styling
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/ompat07@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <div style="margin-bottom: 10px;">
            <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; font-size: 16px;">
        </div>
        <div style="margin-bottom: 10px;">
            <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; font-size: 16px;">
        </div>
        <div style="margin-bottom: 10px;">
            <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 10px; font-size: 16px; height: 150px;"></textarea>
        </div>
        <button type="submit" style="background-color: #4CAF50; color: white; border: none; padding: 15px 32px; text-align: center; font-size: 16px; cursor: pointer;">
            Send
        </button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# Use CSS (optional if needed)
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply custom CSS if needed
# local_css("style/style.css")
