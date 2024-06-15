import webbrowser as wb
import speech_recognition as sr
import pyttsx3
import os

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError as e:
        return f"Request error; {e}"

def execute_command(command):
    if "open google" in command:
        speak("Opening Google")
        wb.open("https://google.com")
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        wb.open("https://youtube.com")
        
    elif "open facebook" in command:
        speak("Opening Facebook")
        wb.open("https://facebook.com")
         
    elif "open github" in command:
        speak("Opening GitHub")
        wb.open("https://github.com")
          
    elif "play music" in command:
        speak("Playing music")
      
        os.system("start wmplayer")  
        
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
          
    elif "open daraz" in command:
        speak("Opening Daraz")
        wb.open("https://www.daraz.com")

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            execute_command(command.lower()) 
        else:
            speak("Please try again.")

          
         
          

           
        
         

        
    
    
