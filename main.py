import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


# this will process command
def processCommand(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open linked in" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")


if __name__ == "__main__":
    speak("Initialising jarvis...")
    # Listen for the word to start responding
    # Obtain audio from the microphone
    while True:
        r = sr.Recognizer()

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if "Jarvis" in word:
                speak("Yes")

                with sr.Microphone() as source:
                    print("Jarvis is active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(e)
