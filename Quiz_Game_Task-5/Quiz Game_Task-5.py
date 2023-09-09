import random
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# -------------------------Dark Theme--------------------------------------------------
palette = QPalette()
palette.setColor(QPalette.Window, QColor(83, 59, 124))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(83, 59, 124))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(83, 59, 124))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)

appFont = QFont()

appFont.setPixelSize(30)
appFont.setFamily('Helvetica')

# -------------------------Dark Theme--------------------------------------------------
class startWindow(QWidget):
    def __init__(self, stackedLayout):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Quiz Game")
        self.setWindowIcon(self.WindowIcon)

        self.stackedLayout = stackedLayout

        self.mainLayout = QVBoxLayout()

        self.label_logo = QLabel()
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setPixmap(QPixmap('images/icon.png').scaled(200, 200))

        self.label_title = QLabel("Quiz Game")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setFont(QFont('Helvetica', 18, weight=QtGui.QFont.Bold, italic=True))

        self.score = 0
        self.label_score = QLabel(f"Your Score: {self.score} ")
        self.label_score.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score.setFont(QFont('Helvetica', 15))

        self.btnPlay = QPushButton("Play")

        self.mainLayout.addWidget(self.label_logo)
        self.mainLayout.addWidget(self.label_title)
        self.mainLayout.addWidget(self.label_score)
        self.mainLayout.addWidget(self.btnPlay)

        self.setLayout(self.mainLayout)
        self.adjustSize()


Q_C_A = [('This drink contains caffeine.', ('A Mineral water', 'B Orange juice', 'C Coffee', 'D Beer'), 'C Coffee'), ('Finish the proverb:\nPoets are born, ________.', ('A ...not made.', 'B ...but can also be made.', 'C ...but thats not for sure.', 'D ..., long live the poets!'), 'A ...not made.'), ('The theory of relativity was introduced in physics by this man.', ('A Galileo Galilei', 'B Albert Einstein', 'C Archimedes', 'D Isaac Newton'), 'B Albert Einstein'), ('The symbol for the chemical element iron is this.', ('A I', 'B Fe', 'C Zn', 'D Br'), 'B Fe'), ('The capital of Mongolia is this city.', ('A Davao', 'B Islamabad', 'C Quezon','D Ulaanbaatar'), 'D Ulaanbaatar'), ('Mitochondrias function in cells is to perform this.', ('A To control chemical reactions within the cytoplasm', 'B To store information needed for cellular division', 'C To convert organic materials into energy', 'D To process proteins targeted to the plasma membrane'), 'C To convert organic materials into energy'), ('The US bought Alaska in this year.', ('A 1942', 'B 1882', 'C 1854', 'D 1867'), 'D 1867'), ('The 1962 Soccer World Cup tournament was held in this country.', ('A Switzerland', 'B Mexico', 'C Chile', 'D Italy'), 'C Chile'), ('The word abacus derives from a Hebrew word, meaning this.', ('A Movement', 'B Sky', 'C Dust', 'D Wood'), 'C Dust'), ('Sean Connery, George Lazenby, Roger Moore, Timothy Dalton and Pierce Brosnan have all played the role of a fictional British spy. Who was that character?', ('A James Bond', 'B Johnny English', 'C Jim Malone', 'D Eliot Ness'), 'A James Bond'), ('The common link between these four movies -Chicken Run, Harry Potter, The Mummy Returns and Cast Away, is that...?',('A They all treat one and the same social problem.', 'B They all are produced by one and the same company.', 'C One and the same actor is starring in all of them.', 'D They all refer to one and the same social class.'), 'B They all are produced by one and the same company.'), ('Three of the following movies are produced by 20th Century Fox. Which is the odd one?',('A Me, Myself  Irene', 'B Dr. Dolittle 2', 'C Cast Away', 'D House of Wax'), 'D House of Wax'), ('Tom Cruise had a lead role in all, but one of these movies.  Which one?',('A Rain Man', 'B The Firm', 'C Magnolia', 'D Endless Love'), 'D Endless Love'), ('All but one of these statements represents a common bond between the movies, The Terminal and Catch Me if You Can.',('A They both can be classified as dramas.', 'B They both are produced by Spielberg.', 'C Tom Hanks stars in them both.', 'D Leonardo DiCaprio stars in them both.'), 'D Leonardo DiCaprio stars in them both.'), ('Brad Pitt starred in all these movies, except one. Can you spot it?',('A Meet Joe Black', 'B Mr.  Mrs. Smith', 'C Oceans Eleven', 'D The Beach'), 'D The Beach'), ('Robin Williams starred in Mrs. Doubtfire. Another great actor, Dustin Hoffman starred in Tootsie. Both characters pretended to be this.',('A Women', 'B Dead', 'C Insane', 'D Bed-ridden and sick'), 'A Women'), ('Which of the following statements about ghosts is incorrect?',('A They are always depicted of a human size and shape.', 'B Ghosts do not have a gross physical body.', 'C Sometimes they might manifest their presence by moving other objects or producing noises.', 'D They are usually portrayed as silvery, shadowy and fog-like.'), 'A They are always depicted of a human size and shape.'), ('The fear of the fatal date is called this.',('A Paraskevidekatriaphobia', 'B Aphenphosmphobia', 'C Chronomentrophobia', 'D Coitophobia'), 'A Paraskevidekatriaphobia'), ('There are countless theories about the origins of fear of number 13. One says that the phobia comes from Norse mythology. According to a legend, the 13th god, the god of mischief, turned up at a gathering of the 12 Viking gods and caused the death of Balder the Good.  What was the god of mischief called?',('A Loki', 'B Tor', 'C Odin', 'D Hod'), 'A Loki'), ('People fear Friday for many reasons. For example, Jesus Christ was crucified on Friday, the Great Flood began on Friday and Adam and Eve were banned from the Garden of Eden on Friday. Do you know what type of day Friday was in the pagan Roman empire?', ('A Parade day', 'B Tax day', 'C Execution day', 'D Day for prayers'), 'C Execution day'), ('Which 1985 comedy film starred Tom Hanks, Jim Belushi and Lori Singer?',('A The Man With One Red Shoe', 'B The Woman In Red', 'C The Masque of the Red Death', 'D Reds'), 'A The Man With One Red Shoe'), ('One of the first known blondes was this Greek goddess, whose hair was described by Homer as golden.', ('A Demeter', 'B Aphrodite', 'C Hera', 'D Medusa'), 'B Aphrodite'), ('The hairs of a natural blonde can be described as this.',('A More than those of a brunette', 'B Thinner than those of a brunette', 'C The same number as those of a brunette', 'D Fewer than those of a brunette'), 'A More than those of a brunette'), ('Most fairy tale characters have this color hair.',('A Blonde', 'B Dark', 'C Green', 'D Red'), 'A Blonde'), ('She is regarded as the most famous blonde of all times.',('A Marlene Dietrich', 'B Eva Brown', 'C Marilyn Monroe', 'D Madonna'), 'C Marilyn Monroe'), ('Red is the color of all these except one.',('A Danger', 'B Warmth', 'C Passion', 'D Sadness'), 'D Sadness'), ('One of these four countries does not border the Red Sea.',('A Jordan', 'B Egypt', 'C Oman', 'D Sudan'), 'C Oman'), ('This huge company is often referred to as Big Blue.',('A Hewlett-Packard', 'B Microsoft', 'C IBM', 'D Cisco Systems, Inc.'), 'C IBM'), ('What did electrical engineering professor, Dr. Brent Townshend, invent in 1996?',('A The 56K modem', 'B Potato Chips', 'C Bookshelf speakers', 'D The remote control locator'), 'A The 56K modem'), ('In 1971, this programmer implemented the first email system capable of sending mail between users on different hosts connected to the ARPANET.',('A David Thomson', 'B John Tomlinson', 'C Mark Thomson', 'D Ray Tomlinson'), 'D Ray Tomlinson'), ('This device, named Missing Link,  was invented by twin sisters Kelli and Vanessa Dunn.',('A The remote control locator', 'B The bookshelf speakers', 'C The 56K modem', 'D The microphone'), 'A The remote control locator'), ('This is the number of heavens in Islamic tradition. It is also the figurative number of seas.',('A 11', 'B 3', 'C 4', 'D 7'), 'D 7'), ('50 years of marriage are known as this.',('A Pearl anniversary', 'B Diamond anniversary', 'C Gold anniversary', 'D Platinum anniversary'), 'C Gold anniversary'), ('Which battleship of the Imperial Japanese Navy was sent on a suicide mission in 1945, during the invasion of Okinawa?',('A Yamato', 'B Kamikaze', 'C Tojo', 'D Noh'), 'A Yamato'), ('In chemistry, if you mix an acid with a base you would get these chemicals.', ('A Water and carbon dioxide', 'B Carbon dioxide and water', 'C Water and a salt', 'D A salt and oxygen'), 'C Water and a salt')]

class PlayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Game Started")
        self.setWindowIcon(self.WindowIcon)

        self.mainLayout = QVBoxLayout()

        self.questionStackedLayout = QStackedLayout()

        self.questions_displayed = random.sample(Q_C_A, 4)

#-----------------------------------------------------------------
        self.question1 = QWidget()
        self.question1_layout = QVBoxLayout()
        self.choices1_Layout = QVBoxLayout()

        self.Q1 = QLabel(self.questions_displayed[0][0])
        self.Q1.setWordWrap(True)
        self.Q1.setMinimumSize(1000, 400)
        self.Q1.setMaximumSize(1500, 500)
        self.Q1.setFont(QFont('Times New Roman', 16, weight=QtGui.QFont.Bold))

        self.choices1_radio_btns = []
        for choice in self.questions_displayed[0][1]:
            self.choices1_radio_btns.append(QRadioButton(choice))
        for radioBtn in self.choices1_radio_btns:
            self.choices1_Layout.addWidget(radioBtn, 1)


        self.question1_layout.addWidget(self.Q1, 1)
        self.question1_layout.addLayout(self.choices1_Layout)

#-----------------------------------------------------------------
        self.question2 = QWidget()
        self.question2_layout = QVBoxLayout()
        self.choices2_Layout = QVBoxLayout()

        self.Q2 = QLabel(self.questions_displayed[1][0])
        self.Q2.setWordWrap(True)
        self.Q2.setMinimumSize(1000, 400)
        self.Q2.setMaximumSize(1500, 500)
        self.Q2.setFont(QFont('Times New Roman', 16, weight=QtGui.QFont.Bold))

        self.choices2_radio_btns = []
        for choice in self.questions_displayed[1][1]:
            self.choices2_radio_btns.append(QRadioButton(choice))
        for radioBtn in self.choices2_radio_btns:
            self.choices2_Layout.addWidget(radioBtn, 1)

        self.question2_layout.addWidget(self.Q2, 1)
        self.question2_layout.addLayout(self.choices2_Layout)
#-----------------------------------------------------------------

        self.question3 = QWidget()
        self.question3_layout = QVBoxLayout()
        self.choices3_Layout = QVBoxLayout()

        self.Q3 = QLabel(self.questions_displayed[2][0])
        self.Q3.setWordWrap(True)
        self.Q3.setMinimumSize(1000, 400)
        self.Q3.setMaximumSize(1500, 500)
        self.Q3.setFont(QFont('Times New Roman', 16, weight=QtGui.QFont.Bold))

        self.choices3_radio_btns = []
        for choice in self.questions_displayed[2][1]:
            self.choices3_radio_btns.append(QRadioButton(choice))
        for radioBtn in self.choices3_radio_btns:
            self.choices3_Layout.addWidget(radioBtn, 1)

        self.question3_layout.addWidget(self.Q3, 1)
        self.question3_layout.addLayout(self.choices3_Layout)
#-----------------------------------------------------------------

        self.question4 = QWidget()
        self.question4_layout = QVBoxLayout()
        self.choices4_Layout = QVBoxLayout()

        self.Q4 = QLabel(self.questions_displayed[3][0])
        self.Q4.setWordWrap(True)
        self.Q4.setMinimumSize(1000, 400)
        self.Q4.setMaximumSize(1500, 500)
        self.Q4.setFont(QFont('Times New Roman', 16, weight=QtGui.QFont.Bold))

        self.choices4_radio_btns = []
        for choice in self.questions_displayed[3][1]:
            self.choices4_radio_btns.append(QRadioButton(choice))
        for radioBtn in self.choices4_radio_btns:
            self.choices4_Layout.addWidget(radioBtn, 1)

        self.question4_layout.addWidget(self.Q4, 1)
        self.question4_layout.addLayout(self.choices4_Layout)

#-----------------------------------------------------------------

        self.btnNext = QPushButton("Next")

        self.question1.setLayout(self.question1_layout)
        self.question2.setLayout(self.question2_layout)
        self.question3.setLayout(self.question3_layout)
        self.question4.setLayout(self.question4_layout)

        self.questionStackedLayout.addWidget(self.question1)
        self.questionStackedLayout.addWidget(self.question2)
        self.questionStackedLayout.addWidget(self.question3)
        self.questionStackedLayout.addWidget(self.question4)

        self.mainLayout.addLayout(self.questionStackedLayout)
        self.mainLayout.addWidget(self.btnNext)

        self.mainLayout.addStretch(1)
        self.setLayout(self.mainLayout)
        self.adjustSize()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Quiz Game")
        self.setWindowIcon(self.WindowIcon)

        self.mainLayout = QVBoxLayout()

        self.stackedLayout = QStackedLayout()

        self.startPage = startWindow(self.stackedLayout)
        self.startPage.btnPlay.clicked.connect(self.play)

        self.playFirstTime = True
        self.nextCounter = 0

        self.playPage = PlayWindow()
        self.playPage.btnNext.clicked.connect(self.next)

        self.stackedLayout.addWidget(self.startPage)
        self.stackedLayout.addWidget(self.playPage)
        self.mainLayout.addLayout(self.stackedLayout)
        self.setLayout(self.mainLayout)
        self.adjustSize()

    # -------------------------Functions-----------------------------------------------START
    def play(self):
        self.nextCounter = 0
        if self.playFirstTime:
            self.stackedLayout.setCurrentIndex(1)
        else:
            self.playPage.questions_displayed = []
            self.playPage.questions_displayed = random.sample(Q_C_A, 4)

            # -----------------------------------------------------------------
            self.playPage.Q1.setText(self.playPage.questions_displayed[0][0])

            counter = 0
            for radioBtn in self.playPage.choices1_radio_btns:
                radioBtn.setText(self.playPage.questions_displayed[0][1][counter])
                counter += 1

            # -----------------------------------------------------------------

            self.playPage.Q2.setText(self.playPage.questions_displayed[1][0])

            counter = 0
            for radioBtn in self.playPage.choices2_radio_btns:
                radioBtn.setText(self.playPage.questions_displayed[1][1][counter])
                counter += 1

            # -----------------------------------------------------------------

            self.playPage.Q3.setText(self.playPage.questions_displayed[2][0])

            counter = 0
            for radioBtn in self.playPage.choices3_radio_btns:
                radioBtn.setText(self.playPage.questions_displayed[2][1][counter])
                counter += 1

            # -----------------------------------------------------------------

            self.playPage.Q4.setText(self.playPage.questions_displayed[3][0])

            counter = 0
            for radioBtn in self.playPage.choices4_radio_btns:
                radioBtn.setText(self.playPage.questions_displayed[3][1][counter])
                counter += 1

            self.stackedLayout.setCurrentIndex(1)

    def next(self):
        self.nextCounter += 1
        currentIndex = self.playPage.questionStackedLayout.currentIndex()
        self.playPage.questionStackedLayout.setCurrentIndex(currentIndex+1 % 4)
        if currentIndex == 0:
            for radioBtn in self.playPage.choices1_radio_btns:
                if radioBtn.isChecked():
                    if self.playPage.questions_displayed[0][2] == radioBtn.text():
                        self.startPage.score += 10
                    radioBtn.setAutoExclusive(False)
                    radioBtn.setChecked(False)
                    radioBtn.setAutoExclusive(True)

        elif currentIndex == 1:
            for radioBtn in self.playPage.choices2_radio_btns:
                if radioBtn.isChecked():
                    if self.playPage.questions_displayed[1][2] == radioBtn.text():
                        self.startPage.score += 10
                    radioBtn.setAutoExclusive(False)
                    radioBtn.setChecked(False)
                    radioBtn.setAutoExclusive(True)
        elif currentIndex == 2:
            for radioBtn in self.playPage.choices3_radio_btns:
                if radioBtn.isChecked():
                    if self.playPage.questions_displayed[2][2] == radioBtn.text():
                        self.startPage.score += 10
                    radioBtn.setAutoExclusive(False)
                    radioBtn.setChecked(False)
                    radioBtn.setAutoExclusive(True)
        elif currentIndex == 3:
            for radioBtn in self.playPage.choices4_radio_btns:
                if radioBtn.isChecked():
                    if self.playPage.questions_displayed[3][2] == radioBtn.text():
                        self.startPage.score += 10
                    radioBtn.setAutoExclusive(False)
                    radioBtn.setChecked(False)
                    radioBtn.setAutoExclusive(True)

        if self.nextCounter == 3:
            self.playFirstTime = False

        if currentIndex+1 == 4:
            self.stackedLayout.setCurrentIndex(0)
            self.startPage.label_score.setText(f"Your Score: {self.startPage.score} out of 40")
            self.startPage.label_score.setAlignment(QtCore.Qt.AlignCenter)
            self.startPage.label_score.adjustSize()
            self.startPage.score = 0
            self.playPage.questionStackedLayout.setCurrentIndex(0)
    # -------------------------Functions-------------------------------------------END


# -------------------------Class MainWindow----------------------------------------END

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setPalette(palette)
    app.setStyle("Fusion")
    app.setFont(appFont)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
