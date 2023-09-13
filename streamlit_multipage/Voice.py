import streamlit as st
import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import openai
from PIL import Image


def app():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Initialize the translator
    translator = Translator()

    # Set your OpenAI API key
    openai.api_key = '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'


    # Center-align the title with padding in front
    st.markdown(
        "<h1 style='text-align: center; padding-left: 20px; font-size: 55px; font-family: Courier New, monospace; font-weight: bold; color: #90ee90;'>VOXBUDDY</h1>",
        unsafe_allow_html=True
    )
    
    st.markdown(
        "<h1 style='text-align: center; padding-left: 20px; font-size: 20px; font-family: Geneva, sans-serif; color: #ff9900;'>A Voice Interaction System</h1>",
        unsafe_allow_html=True
    )
    
    image_path = r"D:\dlproject\voice.jpg"
    img=Image.open(image_path)
    st.image(img,use_column_width=True)
    # Capture audio from the microphone
    with sr.Microphone() as source:
        st.write("Click the button below and speak something...")
        if st.button("START SPEAKING"):
            st.write("Listening.....")

            audio = recognizer.listen(source, phrase_time_limit=5)

            try:
                # Recognize speech using Google Web Speech API
                spoken_text = recognizer.recognize_google(audio)

                # Detect the language of the spoken text
                detected_language = translator.detect(spoken_text).lang
                st.write("YOU SAID:", spoken_text)
                st.write("DETECTED LANGUAGE:", detected_language)

                # Set the target language for translation based on detected language
                if detected_language == 'hi':
                     target_language = 'hi'
                else:
                     target_language = 'en'

                # Translate the spoken text to the specified target language
                
                translated_text = translator.translate(spoken_text, src=detected_language, dest=target_language)
                st.write("\nTRANSLATED TEXT:", translated_text.text)

                # Use the translated text as a prompt for GPT-3
                response = openai.Completion.create(
                    engine="text-davinci-003",  # Choose the desired GPT-3 engine
                    prompt=f"provide an accurate and one sentence answer for this question in {detected_language}: '{translated_text.text}'",
                    max_tokens=200,  # Specify the number of tokens for the response
                    temperature=0
                )

                # Display the GPT-3 generated answer
                st.write("ANSWER:", response.choices[0].text.strip())

    

                # Create a button to play generated text as audio
                # if st.button("Play Generated Text"):
                tts = gTTS(text=response.choices[0].text.strip(), lang=target_language)
                tts.save("output.mp3")

                # Display the generated text as audio
                st.audio("output.mp3", format="audio/mp3")


            except sr.UnknownValueError:
                st.write("Sorry, could not understand audio")
            except sr.RequestError as e:
                st.write("Could not request results; {0}".format(e))