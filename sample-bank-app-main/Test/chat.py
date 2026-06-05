import string
import random
import json
import gtts
from gtts import gTTS
import torch
import tkinter as tk
import speech_recognition as sr
import pygame
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "BBot"

def respond(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    rname=''.join(random.choices(string.ascii_letters + string.digits, k=10))
    rname=rname+".mp3"
    print(rname)
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                text_response = random.choice(intent['responses'])
                tts = gTTS(text=text_response, lang='en', slow=False)
                tts.save(rname)
                return text_response, rname
    else:
        return "I do not understand...", None

def send_message():
    message = entry.get()
    text_area.insert(tk.END, f"You: {message}\n")
    response_text, response_audio = respond(message)
    text_area.insert(tk.END, f"{bot_name}: {response_text}\n")
    entry.delete(0, tk.END)
    if response_audio:
        play_mp3(response_audio)

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

def voice_input():
    text = record_and_transcribe()
    if text:
        text_area.insert(tk.END, f"You: {text}\n")
        response = respond(text)
        text_area.insert(tk.END, f"{bot_name}: {response[0]}\n")
        if response[1]:
            play_mp3(response[1])

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

root = tk.Tk()
root.title("Chatbot")

text_area = tk.Text(root, height=20, width=80)
text_area.pack(pady=10)

entry = tk.Entry(root, width=100)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

voice_button = tk.Button(root, text="Voice Input", command=voice_input)
voice_button.pack(pady=5)

root.mainloop()