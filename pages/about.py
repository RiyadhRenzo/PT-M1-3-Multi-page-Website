import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title="Multi - About", layout="wide")
with st.sidebar:
    st.header("Choose a page")
    
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_profile = load_lottie("https://assets9.lottiefiles.com/packages/lf20_h5wdcgrm.json")
lottie_contact = load_lottie("https://assets2.lottiefiles.com/packages/lf20_px0ntw70.json")
#----------------------------------------------------------------------------------------------------
st.title("About Me")
st.write("---")
col1, col2 = st.columns(2)
with col1:
                  st.write("##")
                  st.header("My name is Riyadh Renzo S. Bongolan")
                  st.subheader("3rd Year IT Student")
                  st.write("""Hello. My complete name is Riyadh Renzo Solima Bongolan, currently a 3rd year in the Laguna State Polytechnic University
                           , under the course of Bachelor of Science in Information Technology. 
                           I am currently 23 years old, living in the Philippines.
My current goal is to finish this semester, my future goal is to finish college, 
and what I want is to live my life unstressed.""")
with col2:
                    st_lottie(lottie_profile, height=230)
            
        
st.write("---")
st.subheader("""
                    Education
                    - ***Laguna State Polytechnic University***
                        - Bachelor of Science - Information Technology
                        - Grade: Pass""")
st.write("---")
st.markdown("<h3 style='color: #4B0082;'>Services Offered</h3>", unsafe_allow_html=True)
    
    # Create a list of services with icons
services = [
        ("🖥️", "Software Development: Creating software/programs based on need."),
        ("💻", "Code Development: Development of code based on program necessity."),
        ("📱", "Apps Design: Designing intuitive and visually appealing mobile and web applications."),
        ("🎮", "Game Design: Creation of immersive and engaging gaming experiences."),
        ("🌐", "Web Design: Designing appealing and user-friendly websites that effectively showcase brands."),
        ("🔧", "Network Management: Management and maintenance of technological infrastructures for optimal performance.")
    ]
    
    # Display each service as a bullet point
for icon, description in services:
        st.markdown(f"- {icon} {description}")

    
              