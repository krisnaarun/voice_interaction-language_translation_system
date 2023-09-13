

import streamlit as st
import streamlit as st
import pytesseract
from PIL import Image
from googletrans import Translator

def app():
    

    # Set page title and description
    st.title("Image Text Language Translation")
    st.write("Upload an image with text, and we'll translate it for you!")

    # Set the path to your Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # File upload widget
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    

    # Initialize the translator
    translator = Translator()

    # Initialize a variable to store the translated text
    translated_text = ""

    # Perform OCR and translation when an image is uploaded
    if uploaded_image:
        # Perform OCR on the uploaded image
        img = Image.open(uploaded_image)
        st.image(img,use_column_width=True)
        text = pytesseract.image_to_string(img)

        # Display the original and translated text when the button is clicked
        st.subheader("Original Text:")
        st.write(text)

        # Language selection widget after showing the original text
        selected_language = st.selectbox("Select Target Language", ["select","Kannada","Malayalam","Spanish", 
                                                                    "French","German", "Italian","Arabic","Chinese (Simplified)",
                                                                    "Chinese (Traditional)","Dutch","Greek","Hindi","Japanese",
                                                                    "Korean","Portuguese","Russian"])  # Add more languages as needed

        # Mapping of user-friendly language names to Google Translate language codes
        language_codes = {
        "Kannada": "kn",
        "Spanish": "es",
        "French": "fr",
        "Malayalam":"ml","German": "de",
        "Italian": "it","Arabic": "ar",
        "Chinese (Simplified)": "zh-CN",
        "Chinese (Traditional)": "zh-TW","Dutch": "nl",
        "Greek": "el","Hindi": "hi","Japanese": "ja","Korean": "ko",
        "Portuguese": "pt","Russian": "ru",

        }
        # Translate the extracted text to the selected language
        target_language = language_codes.get(selected_language, "ml")  # Default to Kannada if language not found
        # Translate the extracted text to your desired language
        translated_text = translator.translate(text, src='auto', dest=target_language)  # Translate to Kannada

        
        
    if st.button("Translate Text"):
        st.subheader(f"Translated Text ({selected_language}):")
        st.write(translated_text.text)