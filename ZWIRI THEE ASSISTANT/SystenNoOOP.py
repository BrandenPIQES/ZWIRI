'''
This is the whole System, Maggie.

Features: Speaking & Listening capabilities.
          Plays music on Youtube.
          Searches for info in Google.
          Shuts down the machine.
          Can detect motion (security if you step away).
          Tell your name if you tell it.

modules: speech_recognition: https://pypi.org/project/SpeechRecognition/
         pyttsx3:            https://pypi.org/project/pyttsx3/
         pywhatkit:          https://pypi.org/project/pywhatkit/
         open cv:            https://pypi.org/project/opencv-python/
'''
import speech_recognition as sr
import pyttsx3, pywhatkit
import OPPDetect


def google_with_voice():
    computer_listen = sr.Recognizer()
    computer_talk = pyttsx3.init()
    voices = computer_talk.getProperty('voices')
    computer_talk.setProperty('voice', voices[1].id)

    def talk(text):
        computer_talk.say(text)
        computer_talk.runAndWait()

    talk('Hello   My name is siri, how can I help you.')
    

    def take_command():
        try:
            with sr.Microphone() as source:
                print("listening...")
                speakers_voice = computer_listen.listen(source)
                command = computer_listen.recognize_google(speakers_voice)
                command = command.lower()
                if 'siri' in command:
                    command  = command.replace('hey','')
                    command = command.replace('siri', '')
                    print(command)
        except:
            pass
        return command

    def run_zwiri():
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)

        elif 'search' in command:
            search = command.replace('search', '')
            talk('looking for results in google')
            pywhatkit.search(search)

        elif 'name' in command:
            talk('You think i dont know you, Branden?')

        elif 'send' in command:
            name = command.split(" ")[-1]
            talk("Sure, what is the message?")
            message = take_command()
            
        elif 'detect' in command:
            OPPDetect.motion_detector.detect_motion()
        elif 'shut down' in command:
            pywhatkit.shutdown(time=0)
    run_zwiri()

def main():
    google_with_voice()
if __name__ == "__main__":
    main()
