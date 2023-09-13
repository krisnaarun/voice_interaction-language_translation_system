# import streamlit as st
# import os
# import cv2
# import time
# import pytesseract
# import speech_recognition as sr
# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
# from googletrans import Translator
# from gtts import gTTS
# from ffpyplayer.player import MediaPlayer
# import moviepy.editor as mp

# # # Specify the path to ImageMagick binary
# # import moviepy.config as mpconfig
# # mpconfig.change_settings({"IMAGEMAGICK_BINARY": r"c:\Program Files\ImageMagick-6.9.12-Q8\convert.exe"})

# def app():
#     st.title("Video Speech Language Translation")
#     st.write("Upload a video with speech, and we'll translate and play it!")

#     # File upload widget for video
#     uploaded_video = st.file_uploader("Upload a video", type=["mp4"])

    

#     if uploaded_video:
#         # Perform translation when a video is uploaded and the button is clicked
#         # if st.button("Translate and Play"):
#             # Temporary paths for audio and video files
#         video_path = "temp_video.mp4"
#         audio_path = "temp_audio.wav"
#         translated_audio_path = "temp_translated_audio.mp3"
#         translated_video_path = "temp_translated_video.mp4"

#             # Save uploaded video to temporary file
#         with open(video_path, "wb") as video_file:
#             video_file.write(uploaded_video.read())

#             # Extract audio from video
#         video_clip = VideoFileClip(video_path)
#         audio_clip = video_clip.audio
#         audio_clip.write_audiofile(audio_path)

#             # Initialize recognizer and translator
#         recognizer = sr.Recognizer()
#         translator = Translator()

#         # Perform speech recognition on the extracted audio
#         with sr.AudioFile(audio_path) as source:
#             audio = recognizer.listen(source)

#         try:
#             spoken_text = recognizer.recognize_google(audio, language='en')
#             # Initialize Streamlit video element to play the original video with audio
#             st.video(video_path, format="video/mp4")

#             # Language selection for translation
#             selected_language = st.selectbox("Select Target Language", ["select", "Kannada", "Malayalam", "Spanish",
#                                                               "French", "German", "Italian", "Arabic",
#                                                               "Chinese (Simplified)", "Chinese (Traditional)",
#                                                               "Dutch", "Greek", "Hindi", "Japanese", "Korean",
#                                                               "Portuguese", "Russian"])

#             # Mapping of user-friendly language names to Google Translate language codes
#             language_codes = {
#         "Kannada": "kn",
#         "Spanish": "es",
#         "French": "fr",
#         "Malayalam": "ml",
#         "German": "de",
#         "Italian": "it",
#         "Arabic": "ar",
#         "Chinese (Simplified)": "zh-CN",
#         "Chinese (Traditional)": "zh-TW",
#         "Dutch": "nl",
#         "Greek": "el",
#         "Hindi": "hi",
#         "Japanese": "ja",
#         "Korean": "ko",
#         "Portuguese": "pt",
#         "Russian": "ru",
#              }

#             # Translate the spoken text
#             target_language = language_codes.get(selected_language, "ml")  # Default to Kannada if language not found
#             translation = translator.translate(spoken_text, src='en', dest=target_language.lower())

#             # Check if the translation response is valid
#             if hasattr(translation, "text"):
#                 translated_text = translation.text
#             else:
#                 translated_text = "Translation not available."

#             translated_audio = gTTS(text=translated_text, lang=target_language.lower())
#             translated_audio.save(translated_audio_path)

#             # # Adding subtitles to the video
#             # txt_clip = TextClip(translated_text, fontsize=24, color="white",font=r"D:\dlproject\streamlit_multipage\FreeSansBold.ttf")
#             # txt_clip = txt_clip.set_duration(video_clip.duration)
#             # txt_clip = txt_clip.set_position(("center", "bottom")).set_start(0)

#             # video_with_subtitles = CompositeVideoClip([txt_clip.set_duration(video_clip.duration)])

#             # Combine the translated audio with the original video
#             clip = mp.VideoFileClip(video_path)
#             audio = mp.AudioFileClip(translated_audio_path)
            
#             # final_video = final_video.set_duration(video_clip.duration)
#             final_video = clip.set_audio(audio)
#             # final_video = final_video.set_mask(video_with_subtitles)  
#             # final_video.write_videofile(translated_video_path, codec="libx264")

#             # Display the video in the Streamlit app
#             st.video(translated_video_path, format="video/mp4")
            
#             if st.button("Translate Text"):
#                 st.subheader(f"Translated Text ({selected_language}):")
#                 st.write(translated_text)    
        

#         except sr.UnknownValueError:
#             st.error("Sorry, could not understand audio")
#         except sr.RequestError as e:
#             st.error("Could not request results; {0}".format(e))
#         except Exception as e:
#             st.error(f"An error occurred: {e}")

import streamlit as st
import os
import cv2
import time
import pytesseract
import speech_recognition as sr
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from googletrans import Translator
from gtts import gTTS

def app():
    st.title("Video Speech Language Translation")
    st.write("Upload a video with speech, and we'll translate and play it!")

    # File upload widget for video
    uploaded_video = st.file_uploader("Upload a video", type=["mp4"])

    if uploaded_video:
        # Temporary paths for audio and video files
        video_path = "temp_video.mp4"
        audio_path = "temp_audio.wav"
        translated_audio_path = "temp_translated_audio.mp3"
        translated_video_path = "temp_translated_video.mp4"

        # Save uploaded video to temporary file
        with open(video_path, "wb") as video_file:
            video_file.write(uploaded_video.read())

        # Extract audio from video
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_path)

        # Initialize recognizer and translator
        recognizer = sr.Recognizer()
        translator = Translator()

        # Perform speech recognition on the extracted audio
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.listen(source)

        try:
            spoken_text = recognizer.recognize_google(audio, language='en')
            # Initialize Streamlit video element to play the original video with audio
            st.video(video_path, format="video/mp4")

            # Language selection for translation
            selected_language = st.selectbox("Select Target Language", ["select", "Kannada", "Malayalam", "Spanish",
                                                              "French", "German", "Italian", "Arabic",
                                                              "Chinese (Simplified)", "Chinese (Traditional)",
                                                              "Dutch", "Greek", "Hindi", "Japanese", "Korean",
                                                              "Portuguese", "Russian"])

            # Mapping of user-friendly language names to Google Translate language codes
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

            # Translate the spoken text
            target_language = language_codes.get(selected_language, "ml")  # Default to Kannada if language not found
            translation = translator.translate(spoken_text, src='en', dest=target_language.lower())

            # Check if the translation response is valid
            if hasattr(translation, "text"):
                translated_text = translation.text
            else:
                translated_text = "Translation not available."

            translated_audio = gTTS(text=translated_text, lang=target_language.lower())
            translated_audio.save(translated_audio_path)

            # Combine the translated audio with the original video
            final_video = video_clip.set_audio(AudioFileClip(translated_audio_path))

            # Display the video in the Streamlit app
            st.video(final_video, format="video/mp4")
            
            if st.button("Translate Text"):
                st.subheader(f"Translated Text ({selected_language}):")
                st.write(translated_text)    
        

        except sr.UnknownValueError:
            st.error("Sorry, could not understand audio")
        except sr.RequestError as e:
            st.error("Could not request results; {0}".format(e))
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    app()