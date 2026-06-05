import speech_recognition as sr
import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def record_and_transcribe():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Record the audio

    try:
        print("Transcribing...")
        # Specify the language code for Malayalam (ml)
        text = recognizer.recognize_google(audio, language="en")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Example usage
transcribed_text = record_and_transcribe()
print("You said:", transcribed_text)
'''
# Example usage
mp3_file_path = "recoutput.mp3"  # Provide the path to your MP3 file
play_mp3(mp3_file_path)
'''
