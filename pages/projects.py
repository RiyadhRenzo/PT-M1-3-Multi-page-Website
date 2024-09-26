import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title="Multi - Projects", layout="wide")


# Sidebar for page selection
with st.sidebar:
    st.header("Choose a page")
    
st.title("My Projects")
st.write("##")
col_l, col_r = st.columns((1,2))
with col_r:
                  st.subheader("Case Study: ShopSmart")
                  st.write("""

                  This case study, titled "Developing a Multi-Platform E-Commerce Solution," 
                  focuses on a mid-sized retail company, ShopSmart, seeking to expand its online presence. 
                  The project involves creating an e-commerce platform that integrates ShopSmart's existing legacy inventory 
                  management system and provides customers with seamless access through web, mobile, and desktop platforms. 
                  The objective is to modernize the company's operations while ensuring efficient data synchronization, 
                  enhanced customer experience, and smooth operational efficiency. 
                  Key challenges include technological integration and maintaining security during the transition.
                  """)
                  st.markdown("[Read the file here>](https://docs.google.com/document/d/1D8-cJGa9UYPRC506A0XZgsVfhFqGTRHH/edit?usp=sharing&ouid=109839613783124788939&rtpof=true&sd=true)")
with col_l:
    st.image("images/1.png")
st.write("---")
col_l2, col_r2 = st.columns((1,2))
with col_r2:
                  st.subheader("Data Visualization Streamlit")
                  st.write("""

                  Data visualization is the graphical representation of data and information. 
                  It helps make complex data easier to understand by using visual elements like charts, graphs, and maps. 
                  The goal of data visualization is to reveal patterns, trends, and insights that might be difficult to spot in raw data, 
                  enabling more informed decision-making and clearer communication.
                  """)
                  st.markdown("[Check the File's Code out>](https://drive.google.com/file/d/1HzL-UJINho6hcEbODSns0Knh4u3imSv9/view?usp=sharing)")
with col_l2:
    st.image("images/2.png")
#---------------------------------------------------------------------------------------------------