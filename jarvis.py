import pyttsx3
import speechRecognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setproperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphon() as source:
        print("Listening...")
        r.pause_threshole = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
        try:
            print("Understanding...")
            query  = r.recognize_google(audio,language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Sorry... Say that again")
            return "None"
        return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "weke up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleeep/shutdown" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                elif"Hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect sir")