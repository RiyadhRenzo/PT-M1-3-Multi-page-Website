import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Multi - Home", layout="wide")
with st.sidebar:
    st.header("Choose a page")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

gif_path = "images/like.gif"
lottie_profile = load_lottie("https://assets9.lottiefiles.com/packages/lf20_h5wdcgrm.json")
lottie_contact = load_lottie("https://assets2.lottiefiles.com/packages/lf20_px0ntw70.json")

st.write("##")
st.title("Hello, and Welcome to my Streamlit Website!  :wave:")
st.write("---")
st.header("What is Streamlit?")
col_l, col_r = st.columns((1,2))
with col_r:
    st.write("""Streamlit is an open-source framework that simplifies the process of building interactive web applications, particularly for data science and machine learning projects. 
         With its intuitive and user-friendly design, developers can create applications with minimal code,
         making it accessible even for those without extensive web development experience. 
         """)
with col_l:
    st.image("images/streamlit.png")
st.write("###")
st.write("---")

col_l2, col_r2 = st.columns((1,2))
with col_r2:
    st.header("          Why use Streamlit?")
    st.write("""Because streamlit supports real-time interactivity, allowing applications to update automatically as users interact 
             with various inputs like sliders and buttons. 
         It seamlessly integrates with popular data visualization libraries, enabling the creation of dynamic
         and visually appealing charts and graphs. Additionally, Streamlit supports Markdown for easy text formatting, 
         providing a straightforward way to include documentation and explanations.
         With a variety of built-in widgets, users can engage with the application without complex coding. 
         The deployment of Streamlit apps is also streamlined, allowing for easy sharing through platforms like Streamlit Sharing. 
         Overall, Streamlit empowers data scientists and machine learning engineers to transform their insights into 
         engaging web applications without needing to learn new programming languages or frameworks.""")
with col_l2:
    st.image(gif_path, use_column_width=True)
#----------------------------------------------------------------------------------------------------
