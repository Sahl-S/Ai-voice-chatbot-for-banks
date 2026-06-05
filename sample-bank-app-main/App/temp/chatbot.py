import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def send_message():
    message = user_input.get()
    add_to_chat_history("User: " + message)
    user_input.delete(0, tk.END)
    # Process the message and generate a response here
    # For simplicity, I'm just echoing back the user's message
    add_to_chat_history("Bot: " + message)

def listen_message():
    listen_button.config(state="disabled")
    threading.Thread(target=listen_and_reply).start()

def listen_and_reply():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        try:
            user_message = r.recognize_google(audio)
            print("User:", user_message)
            add_to_chat_history("User: " + user_message)
            # Process user_message and generate response here
            # For simplicity, I'm just echoing back the user's message
            add_to_chat_history("Bot: " + user_message)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    listen_button.config(state="normal")

def add_to_chat_history(message):
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, message + '\n')
    chat_history.configure(state='disabled')
    chat_history.see(tk.END)

root = tk.Tk()
root.title("Voice-Enabled Chatbot")

chat_history = scrolledtext.ScrolledText(root, width=50, height=20)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

user_input = tk.Entry(root, width=40)
user_input.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

listen_button = tk.Button(root, text="Listen", command=listen_message)
listen_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()