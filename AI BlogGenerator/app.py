


import streamlit as st
import google.generativeai as genai
import os

# Configure API

# API_KEY =Your API KEy
genai.configure(api_key=API_KEY)

# Set app to wide mode
st.set_page_config(layout='wide')

# Title of the app
st.title('Generate the Blog')

# Create a Subheader
st.subheader('Your New AI Blog Companion')

# Sidebar for user inputs
with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter the Details of the Blog you want to Generate")

    # Blog Title
    blog_title = st.text_input("Blog Title")

    # Keyword Input
    keywords = st.text_area('Keywords (Comma-Separated)')

    # Number of Words
    num_words = st.slider('Number of words', min_value=200,
                          max_value=1500, step=100)

    # Number of Images
    num_images = st.number_input(
        'Number of Images', min_value=1, max_value=5, step=1)

    # Button
    submit_button = st.button('Generate Blog')

# Generate blog on button click
if submit_button:
    if not blog_title or not keywords:
        st.error("Please fill in all required fields!")
    else:
        # Construct the prompt
        prompt_parts = f"""
        Write a detailed and engaging blog article based on the following input in paragraph style for each keyword each paragraph:

        Title: {blog_title}
        Keywords: {keywords}
        Word Count: Approximately {num_words} words.

        Instructions:
        - Begin with an engaging introduction that hooks the reader and sets the tone for the article.
        - Use the provided keywords naturally and strategically throughout the blog to maintain SEO optimization.
        - Break the content into well-structured sections with clear headings and subheadings.
        - Provide valuable insights, examples, or actionable tips to enhance the reader's understanding.
        - Conclude with a strong summary and, if appropriate, a call to action.
        - The tone should be Informative and tailored to a Beginner Engineer audience. Ensure that the article is original, coherent, and flows smoothly.
        """
try:
    # Replace with the correct model instantiation
    model = genai.GenerativeModel('gemini-pro')

    # Generate content using the model
    response = model.generate_content(prompt_parts)

    # Display the response
    st.write(response.text)

except Exception as e:
    st.error(f"An error occurred: {e}")
