import streamlit as st
import mysql.connector
from mysql.connector import Error
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Multi - Testimonials", layout="wide")

# Sidebar for page selection
with st.sidebar:
    st.header("Choose a page")

# Title for the main content
st.title("Testimonials")
st.subheader("Leave a Comment Here!")
st.write("---")

# Create two columns for input
left_col, right_col = st.columns(2)

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  # e.g., 'localhost'
            port=3307,
            database='testimonial',
            user='root',
            password=''
        )
        return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None

# Insert testimonial into the database
def insert_testimonial(name, comment):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO testimonials (name, comment) VALUES (%s, %s)"
        cursor.execute(query, (name, comment))
        connection.commit()
        cursor.close()
        connection.close()
        st.success("Message sent successfully!")

# Fetch testimonials from the database
def fetch_testimonials():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT name, comment, created_at FROM testimonials ORDER BY created_at DESC"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    return []

# Input fields for name and message
with left_col:
    st.header(":bust_in_silhouette: Name")
    name_input = st.text_input("Your name", placeholder="Enter your name")

with right_col:
    st.header(":speech_balloon: Message")
    message_input = st.text_area("Your message", placeholder="Enter your message", height=150)

# Send button
if st.button("Send"):
    if name_input and message_input:
        insert_testimonial(name_input, message_input)
    else:
        st.error("Please fill in both fields before sending.")

# Display testimonials
testimonials = fetch_testimonials()
for name, comment, created_at in testimonials:
    st.write(f"**{name}** ({created_at}): {comment}")
