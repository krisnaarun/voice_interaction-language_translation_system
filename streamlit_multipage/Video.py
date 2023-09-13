import streamlit as st
import os
import cv2
import time
import pytesseract
import speech_recognition as sr
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from googletrans import Translator
from gtts import gTTS
import moviepy.editor as mp

def app():
    st.title("Video Speech Language Translation")
    st.write("Upload a video with speech, and we'll translate and play it!")

    # File upload widget for video
    uploaded_video = st.file_uploader("Upload a video", type=["mp4"])

    if uploaded_video:
        # Perform translation when a video is uploaded and the button is clicked
        video_path = "temp_video.mp4"
        audio_path = "temp_audio.wav"
        translated_audio_path = "temp_translated_audio.mp3"
        translated_video_path = "temp_translated_video.mp4"

        with open(video_path, "wb") as video_file:
            video_file.write(uploaded_video.read())

        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_path)

        recognizer = sr.Recognizer()
        translator = Translator()

        with sr.AudioFile(audio_path) as source:
            audio = recognizer.listen(source)

        try:
            spoken_text = recognizer.recognize_google(audio, language='en')
            st.video(video_path, format="video/mp4")

            selected_language = st.selectbox("Select Target Language", ["select", "Kannada", "Malayalam", "Spanish",
                                                              "French", "German", "Italian", "Arabic",
                                                              "Chinese (Simplified)", "Chinese (Traditional)",
                                                              "Dutch", "Greek", "Hindi", "Japanese", "Korean",
                                                              "Portuguese", "Russian"])

            language_codes = {
                "Kannada": "kn",
                "Spanish": "es",
                "French": "fr",
                "Malayalam": "ml",
                "German": "de",
                "Italian": "it",
                "Arabic": "ar",
                "Chinese (Simplified)": "zh-CN",
                "Chinese (Traditional)": "zh-TW",
                "Dutch": "nl",
                "Greek": "el",
                "Hindi": "hi",
                "Japanese": "ja",
                "Korean": "ko",
                "Portuguese": "pt",
                "Russian": "ru",
            }

            target_language = language_codes.get(selected_language, "ml")
            translation = translator.translate(spoken_text, src='en', dest=target_language.lower())

            if hasattr(translation, "text"):
                translated_text = translation.text
            else:
                translated_text = "Translation not available."

            translated_audio = gTTS(text=translated_text, lang=target_language.lower())
            translated_audio.save(translated_audio_path)

            # Adding subtitles to the video
            txt_clip = TextClip(translated_text, fontsize=24, color="white")
            txt_clip = txt_clip.set_duration(video_clip.duration)
            txt_clip = txt_clip.set_position(("center", "bottom"))

            video_with_subtitles = CompositeVideoClip([video_clip, txt_clip])

            # Combine the translated audio with the original video
            clip = mp.VideoFileClip(video_path)
            audio = mp.AudioFileClip(translated_audio_path)

            final_video = clip.set_audio(audio)
            final_video.write_videofile(translated_video_path, codec="libx264")

            # Display the video in the Streamlit app
            st.video(translated_video_path, format="video/mp4")

            # Print the translated text
            st.write("Translated Text:")
            st.write(translated_text)

        except sr.UnknownValueError:
            st.error("Sorry, could not understand audio")
        except sr.RequestError as e:
            st.error("Could not request results; {0}".format(e))
        except Exception as e:
            st.error(f"An error occurred: {e}")
