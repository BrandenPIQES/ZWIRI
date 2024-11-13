import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import SystemInOOP
import speech_recognition as sr
import os
import json

class WelcomeWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Member variable for first window
        self.next_window = None

        # get laptops dimensions
        self.screen = QDesktopWidget().screenGeometry()

        # set min and max size
        self.setMinimumSize(500,500)  
        self.setMinimumSize(500,500)

        # set where to place window to laptops specifications
        self.setGeometry(int(0.25 * self.screen.width()), int(0.25 * self.height()),int(0.5 * self.screen.width()),int(0.5 * self.screen.height()))

        # allow resize of the window
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set window title and logo
        self.setWindowTitle("Welcome to Zwiri")
        self.setWindowIcon(QIcon("data/window_icon.gif"))

        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 red,
                    stop: 0.5 orange,
                    stop: 1 yellow
                );
        }
        """)

        # corrected layout, Grid
        self.grid_layout = QGridLayout()

        # go on buttons and adjustments
        self.Next = QPushButton('GET STARTED',self)
        self.welcome_msg = QLabel("WELCOME TO ZWIRI",self)
        self.Next.clicked.connect(self.WindowONE)

        # set sizes, styles and positioning for the button
        self.Next.setFixedWidth(200)
        self.Next.setFixedHeight(50)
        self.Next.setStyleSheet("border: 3px solid blue; border-radius: 20px;font-size:20px; font-weight: bold; color:white;")
        self.welcome_msg.setStyleSheet("background-color: transparent ;font-size:50px; font-weight: bold; color:white;")
        

        self.grid_layout.addWidget(self.welcome_msg,2,2,alignment=Qt.AlignCenter)
        self.grid_layout.addWidget(self.Next,4,2,alignment=Qt.AlignCenter)

        self.setLayout(self.grid_layout)


    def WindowONE(self):
        self.next_window = firstWindow()
        self.next_window.show()
        self.close()

class firstWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Member variable for first window
        self.next_window = None

        # get laptops dimensions
        self.screen = QDesktopWidget().screenGeometry()

        # set min and max size
        self.setMinimumSize(500,500)  
        self.setMinimumSize(500,500)

        # set where to place window to laptops specifications
        self.setGeometry(int(0.25 * self.screen.width()), int(0.25 * self.height()),int(0.5 * self.screen.width()),int(0.5 * self.screen.height()))

        # allow resize of the window
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set window title and logo
        self.setWindowTitle("Tasks Assistant")
        self.setWindowIcon(QIcon("data/window_icon.gif"))

        # set the background color of the window
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 red,
                    stop: 0.5 orange,
                    stop: 1 yellow
                );
        }
        """)

        # corrected layout, Grid
        self.grid_layout = QGridLayout()

        # tells us your name, submit and lineedit labels
        self.EntNameLbl = QLabel("Tell us your name",self)
        self.EntName = QLineEdit('',self)
        self.Next = QPushButton('NEXT',self)

        # Set the size of the QLineEdit and QPushButton
        self.EntName.setFixedWidth(400)
        self.EntName.setFixedHeight(50)
        self.Next.setFixedWidth(200)
        self.Next.setFixedHeight(50)

        # style name and adjustment labels
        self.EntNameLbl.setStyleSheet("background-color: transparent; font-size:50px; font-weight: bold; color:white;")
        self.EntName.setStyleSheet("background-color: white; font-weight: bold; font-size:20px;")
        self.Next.setStyleSheet("border: 3px solid blue; border-radius: 20px;font-size:20px; font-weight: bold; color:white;")
        
        # add labels to main layout
        self.grid_layout.addWidget(self.EntNameLbl,0,2,alignment = Qt.AlignCenter)
        self.grid_layout.addWidget(self.EntName,1,2,alignment=Qt.AlignCenter)
        self.grid_layout.addWidget(self.Next,2,2,alignment=Qt.AlignCenter)

        # next window when NEXT is clicked
        self.Next.clicked.connect(self.WindowTwo)

        self.setLayout(self.grid_layout)
    
    def WindowTwo(self):
        name = self.EntName.text()
        if name:
            with open("name.txt", "w") as file:
                file.write(name)
                file.close()

            self.next_window = secondWindow()
            self.next_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Please enter a name.")

class secondWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Member variable for first window
        self.next_window = None

        # get laptops dimensions
        self.screen = QDesktopWidget().screenGeometry()

        # set min and max size
        self.setMinimumSize(500,500)  
        self.setMinimumSize(500,500)

        # set where to place window to laptops specifications
        self.setGeometry(int(0.25 * self.screen.width()), int(0.25 * self.height()),int(0.5 * self.screen.width()),int(0.5 * self.screen.height()))

        # allow resize of the window
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set window title and logo
        self.setWindowTitle("Contomisation")
        self.setWindowIcon(QIcon("data/window_icon.gif"))

        # set the background color of the window
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 red,
                    stop: 0.5 orange,
                    stop: 1 yellow
                );
        }
        """)

        # corrected layout, Grid
        self.grid_layout = QGridLayout()

        # tells us your name, submit and lineedit labels
        self.EntNameLbl = QLabel("COSTOMIZE YOUR ASSISTANT",self)
        self.EntName = QLineEdit('',self)
        self.Next = QPushButton('NEXT',self)

        # Set placeholder text for the QLineEdit
        self.EntName.setPlaceholderText("Give it an english name")

        # Set the size of the QLineEdit and QPushButton
        self.EntName.setFixedWidth(400)
        self.EntName.setFixedHeight(50)
        self.Next.setFixedWidth(200)
        self.Next.setFixedHeight(50)

        # style name and adjustment labels
        self.EntNameLbl.setStyleSheet("background-color: transparent; font-size:50px; font-weight: bold; color:white;")
        self.EntName.setStyleSheet("background-color: white; font-weight: bold; font-size:20px;")
        self.Next.setStyleSheet("border: 3px solid blue; border-radius: 20px;font-size:20px; font-weight: bold; color:white;")
        
        # add labels to main layout
        self.grid_layout.addWidget(self.EntNameLbl,0,2,alignment = Qt.AlignCenter)
        self.grid_layout.addWidget(self.EntName,1,2,alignment=Qt.AlignCenter)
        self.grid_layout.addWidget(self.Next,2,2,alignment=Qt.AlignCenter)

        # Go to next window when NEXT clicked
        self.Next.clicked.connect(self.Windowthree)

        self.setLayout(self.grid_layout)

    def Windowthree(self):
        costom_name = self.EntName.text()
        if costom_name:
            with open("costom_name.txt", "w") as file:
                file.write(costom_name)
                file.close()

            self.next_window = thirdWindow()
            self.next_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Please give it a name.")
           
class thirdWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Member variable for first window
        self.next_window = None

        # get laptops dimensions
        self.screen = QDesktopWidget().screenGeometry()

        # set min and max size
        self.setMinimumSize(500,500)  
        self.setMinimumSize(500,500)

        # set where to place window to laptops specifications
        self.setGeometry(int(0.25 * self.screen.width()), int(0.25 * self.height()),int(0.5 * self.screen.width()),int(0.5 * self.screen.height()))

        # allow resize of the window
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set window title and logo
        self.setWindowTitle("Speak to Zwiri")
        self.setWindowIcon(QIcon("data/window_icon.gif"))

        # set the background color of the window
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 red,
                    stop: 0.5 orange,
                    stop: 1 yellow
                );
        }
        """)

        self.MainLayout = QGridLayout(self)

        # get the constom made name
        with open("costom_name.txt", "r") as file:
            cost_name = file.readline()
            file.close()

        
        # Create a circular QLabel and how to
        self.RecordBtn = QPushButton(self)
        self.RecordBtn.setFixedSize(200, 200)
        #self.RecordBtn.setAlignment(Qt.AlignCenter)
        self.YourSpeech = QLabel("Click to talk to {}.".format(cost_name),self)
        self.HowTo = QPushButton("I dont know what to say!")
        self.HowTo.clicked.connect(self.TheyDont)
        self.RecordBtn.clicked.connect(self.CallZwiri)


        # style labels
        self.RecordBtn.setStyleSheet("border-radius: 100px; background-image: url('data/2176428.png');")
        self.YourSpeech.setStyleSheet("background-color: transparent; font-size:20px;")
        self.HowTo.setStyleSheet("background-color: transparent; font-size:20px;text-decoration: underline; color:black;")

    
        self.MainLayout.addWidget(self.RecordBtn, 0, 1, alignment=Qt.AlignCenter)
        self.MainLayout.addWidget(self.YourSpeech,4,1, alignment=Qt.AlignCenter)
        self.MainLayout.addWidget(self.HowTo,6,1, alignment=Qt.AlignCenter)

        self.setLayout(self.MainLayout)

    def CallZwiri(self):
        file = open("costom_name.txt", "r")
        costom_name = file.read()
        file.close()

        zwiri = SystemInOOP.Zwiri()
        zwiri.talk("Hi my name is {} how can I help you".format(costom_name))

        self.YourSpeech.setText("Listening...")
        QApplication.processEvents()
        zwiri.run_zwiri(costom_name)
        self.YourSpeech.setText("Click to talk to {}.".format(costom_name))
        QApplication.processEvents()

    def TheyDont(self):
        self.next_window = DontKnowCommands()
        self.next_window.show()

class DontKnowCommands(QDialog):
    def __init__(self):
        QDialog.__init__(self)


        # get laptops dimensions
        self.screen = QDesktopWidget().screenGeometry()

        # set min and max size
        self.setMinimumSize(500,500)  
        self.setMinimumSize(500,500)

        # set where to place window to laptops specifications
        self.setGeometry(int(0.25 * self.screen.width()), int(0.25 * self.height()),int(0.5 * self.screen.width()),int(0.5 * self.screen.height()))

        # allow resize of the window
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set window title and logo
        self.setWindowTitle("Help")
        self.setWindowIcon(QIcon("data/window_icon.gif"))

        # set the background color of the window
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 red,
                    stop: 0.5 orange,
                    stop: 1 yellow
                );
        }
        """)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Create buttons for commands
        self.play = QLabel("To play music say: Hey <constomised name> play <song name and artist>", self)
        self.search = QLabel("To search info say: Hey <constomised name> search <infomation>", self)
        self.detect = QLabel("To enter security mode say: Hey <constomised name> detect", self)
        self.shutdown = QLabel("To shutdown computer say: Hey <constomised name> shut down", self)
        self.name = QLabel("To hear your name: Hey <constomised name> what is my name", self)
        self.adj = QLabel(self)
        self.okay = QPushButton("OK",self)
        self.okay.clicked.connect(self.close)

        # style the labels
        self.play.setStyleSheet("background-color: transparent; font-size:20px; color: white; font-weight: bold;")
        self.search.setStyleSheet("background-color: transparent; font-size:20px; color: white; font-weight: bold;")
        self.detect.setStyleSheet("background-color: transparent; font-size:20px; color: white; font-weight: bold;")
        self.name.setStyleSheet("background-color: transparent; font-size:20px; color: white; font-weight: bold;")
        self.shutdown.setStyleSheet("background-color: transparent; font-size:20px; color: white; font-weight: bold;")
        self.adj.setStyleSheet("background-color: transparent; font-size:20px; color: white; font-weight: bold;")
        self.okay.setStyleSheet("border: 2px solid blue; border-radius:20px ;font-size:25px; color:white; font-weight: bold;")

        
        # Add buttons to layout
        layout.addWidget(self.play)
        layout.addWidget(self.search)
        layout.addWidget(self.detect)
        layout.addWidget(self.shutdown)
        layout.addWidget(self.name)
        layout.addWidget(self.adj)
        layout.addWidget(self.okay)
        
        # Set layout
        self.setLayout(layout)

def check_first_launch():
    # Check if the app has been launched before
    config_file_path = os.path.join(sys.path[0], 'config.json')
    try:
        with open(config_file_path, 'r') as file:
            config = json.load(file)
            return config.get('first_launch', True)
        
    except FileNotFoundError:
        return True

def update_first_launch():
    # Update the configuration file after the first launch
    config_file_path = os.path.join(sys.path[0], 'config.json')
    config = {'first_launch': False}

    with open(config_file_path, 'w') as file:
        json.dump(config, file)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    first_launch = check_first_launch()

    if first_launch:
        window = WelcomeWindow()
        window.show()
        update_first_launch()
        sys.exit(app.exec_())
    else:
        window = thirdWindow()
        window.show()
        sys.exit(app.exec_())   