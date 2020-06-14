import pyttsx3
import speech_recognition as sr


# text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# speech to text
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ""

        try:
            text = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))

    return text.lower()





def main():
    wake = ['kara', 'cara', 'kawa']

    while True:
        text = get_audio()

        for word in wake:
            if word in text:
                text = get_audio()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
