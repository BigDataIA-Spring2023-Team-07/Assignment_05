import streamlit as st
import os
import re
from streamlit_player import st_player
from backend import logic



# # Add a title and subtitle
st.title('YouTube Digest :movie_camera:')



video_url = st.text_input('YouTube Video URL')

# Embed the video using the HTML code for the video player
if video_url:

    # Extract the video ID from the URL
    video_id = video_url.split("v=")[1]
    # Construct the shortened URL
    short_url = f"https://youtu.be/{video_id}"
    st.video(short_url)






selected_option = st.selectbox("Select an option", ["Select", "Summarizer", "Topic Generator", "Viewers Sentiments"])


if selected_option == "Summarizer":
    st.subheader('Summarizer')




if selected_option == "Topic Generator":
    st.subheader('Topic Generator')
    transcript = logic.transcribe_audio('lex_ai_sam_altman_5min.mp3')
    name, start_time, end_time = logic.main_topics(transcript)
    st.write(name)
    st.write(start_time)
    st.write(end_time)
    



if selected_option == "Viewers Sentiments":
    st.subheader('Viewers Sentiments')


if selected_option == "Custom":
    st.subheader('Custom')




# # Add a text input
# search_query = st.text_input('Search on YouTube')

# # Add a button
# if st.button('Search'):
#     st.write(f'Searching for "{search_query}"...')

# # Add a video player
# video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
# st.video(video_url)
