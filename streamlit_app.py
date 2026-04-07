import streamlit as st

from services import analyze_text

MAX_HISTORY = 10

st.set_page_config(page_title="Sentiment Analysis", page_icon=":speech_balloon:")

st.title("Sentiment Analysis Web Interface")
st.write("Enter text to analyze its sentiment.")

if "history" not in st.session_state:
    st.session_state.history = []

text = st.text_area("Text for analysis", placeholder="Type text here...")

if st.button("Analyze"):
    if text.strip():
        try:
            result = analyze_text(text)
            label = result[0]["label"]
            score = result[0]["score"]

            color = "green" if label == "POSITIVE" else "red"
            st.markdown(
                f"**Result:** :{color}[{label}] — confidence: {score:.1%}"
            )

            st.session_state.history = [
                {"text": text, "label": label, "score": score}
            ] + st.session_state.history[:MAX_HISTORY - 1]

        except Exception as e:
            st.error(f"Analysis failed: {e}")
    else:
        st.warning("Please enter text before analysis.")

if st.session_state.history:
    st.divider()
    col1, col2 = st.columns([4, 1])
    col1.subheader("History")
    if col2.button("Clear"):
        st.session_state.history = []
        st.rerun()

    for entry in st.session_state.history:
        color = "green" if entry["label"] == "POSITIVE" else "red"
        st.markdown(
            f"- :{color}[{entry['label']}] {entry['score']:.1%} — *{entry['text'][:80]}*"
        )
