import speech_recognition as sr
import pyttsx3,pywhatkit,cv2


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

    def run_siri():
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

        elif 'detect' in command:
            pass
        elif 'shutdown' in command:
            pywhatkit.shutdown(time=20)

    run_siri()

google_with_voice()
