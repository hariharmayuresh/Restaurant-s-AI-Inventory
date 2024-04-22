import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline (replace with your preferred model)
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """Analyzes the sentiment of the provided text using the loaded pipeline.

    Args:
        text (str): The text to be analyzed.

    Returns:
        str: The sentiment label (positive, neutral, or negative).
    """

    results = classifier(text)
    label = results[0]['label']
    return label.upper()  # Convert to uppercase for better display

st.title("Feedback Analysis")

# ... Your other app functionalities here ...

# Feedback section
# st.header("Feedback")
feedback_text = st.text_area("Enter your comments or feedback:", height=100)
submit_button = st.button("Submit Feedback")

if submit_button:
    if feedback_text:
        sentiment = analyze_sentiment(feedback_text)
        st.write(f"Feedback Type: {sentiment}")

        # Optionally, store or process the feedback based on sentiment
        if sentiment == "POSITIVE":
            st.success("Thank you for your positive feedback!")
        elif sentiment == "NEGATIVE":
            st.error("We apologize for any inconvenience. Please let us know how we can improve at our site.")
        else:
            st.info("Thank you for your feedback!")
    else:
        st.warning("Please enter some feedback before submitting.")