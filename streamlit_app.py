import streamlit as st

from services import analyze_text


st.set_page_config(page_title="Sentiment Analysis", page_icon=":speech_balloon:")

st.title("Sentiment Analysis Web Interface")
st.write("Enter text to analyze its sentiment.")

text = st.text_area("Text for analysis", placeholder="Type text here...")

if st.button("Analyze"):
    if text.strip():
        result = analyze_text(text)
        st.subheader("Result")
        st.json(result)
    else:
        st.warning("Please enter text before analysis.")
