import speech_recognition as sr
import pyttsx3
import pywhatkit
import OPPDetect
import googlesearch
import time
import requests
from bs4 import BeautifulSoup


class Zwiri:
    def __init__(self):
        self.computer_listen = sr.Recognizer()
        self.computer_talk = pyttsx3.init()
        self.voices = self.computer_talk.getProperty('voices')
        self.computer_talk.setProperty('voice', self.voices[1].id)

    def talk(self, text):
        self.computer_talk.say(text)
        self.computer_talk.runAndWait()

    def take_command(self, name):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                speakers_voice = self.computer_listen.listen(source)
                command = self.computer_listen.recognize_google(speakers_voice)
                command = command.lower()
                if name in command:
                    command = command.replace('hey', '')
                    command = command.replace(name, '')
                    print(command)
                        
        except:  
            pass
        return command


    def take_response(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                speakers_voice = self.computer_listen.listen(source)
                command = self.computer_listen.recognize_google(speakers_voice)
                command = command.lower()
        except:
            pass

        return command

    def ReadFromWeb(self, urls):
        response = requests.get(urls)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        self.lst_paras = []

        # Extract text from all paragraphs on the web page
        paragraphs = soup.find_all('p')

        for paragraph in paragraphs:
            self.lst_paras.append(paragraph.get_text())

        return self.lst_paras
      
    
    # def search_on_google(self,query):
    #     search_results = search(query, num_results=5)  # Perform a Google search and get the top 5 results
    #     urls = []
    #     for result in search_results:
    #         urls.append(result)

    #     return urls

    # def search_on_google(self, query):
    #     url = "https://api.bard.ai/v1/query"
    #     question = {
    #         "query" : query,
    #     }
    #     responce = requests.get(url=url, params=question)

    #     return responce.json()

    def search_on_google(self, query):
        url = "https://api.bard.ai/v1/query"
        params = {
            "query": query,
        }

        max_retries = 3
        retry_delay = 1


        for retry in range(max_retries):
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()  # Raise an exception for any HTTP error status
                return response.json()
            
            except requests.exceptions.RequestException as e:
                print("An error occurred during the request:", e)

            # Delay before the next retry with exponential backoff
            delay = retry_delay * (2 ** retry)
            time.sleep(delay)

        return None

    def run_zwiri(self, name):
        self.command = self.take_command(name)

        if 'play' in self.command:
            song = self.command.replace('play', '')
            self.talk('Playing ' + song)
            pywhatkit.playonyt(song)

        elif 'search' in self.command or 'what' in self.command:
            search = self.command.replace('search', '')
            self.talk('Looking for results')
            time.sleep(2)
            self.talk('Would you like me to open google or read the results to you? Note that reading to you might take time as I have to go to through many links')
            self.responce = self.take_response()
            if "open" in self.responce or "google" in self.responce: 
                pywhatkit.search(search)
            else:
                self.talk("Please note my results are from BARDN AI, the info might not be as accurate.")
                # for urls in self.search_on_google(self.command):
                #     self.para = self.ReadFromWeb(urls)
                #     for line in self.para:
                #         self.talk(line)
                answer = self.search_on_google(self.command)
                self.talk(answer)

        # elif 'name' in self.command:
        #     self.talk('You think I do not know you, Branden?')

        elif 'send' in self.command:
            name = self.command.split(" ")[-1]
            self.talk("Sure, what is the message?")
            message = self.take_command()
            

        elif 'detect' in self.command:
            OPPDetect.motion_detector.detect_motion()
        
        elif 'shut down' in self.command:
            pywhatkit.shutdown(time=0)

    def start(self):
        self.talk('Hello, my name is Zwiri. How can I help you?')
        self.run_zwiri()

# usage
zwiri = Zwiri()
