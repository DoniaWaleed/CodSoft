import sys

import requests
from datetime import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# -------------------------Dark Theme--------------------------------------------------
palette = QPalette()
palette.setColor(QPalette.Window, QColor(124, 180, 201))
palette.setColor(QPalette.WindowText, Qt.black)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(124, 180, 201))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.black)
palette.setColor(QPalette.Text, Qt.black)
palette.setColor(QPalette.Button, QColor(124, 180, 201))
palette.setColor(QPalette.ButtonText, Qt.black)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.white)

appFont = QFont()

appFont.setPixelSize(50)
appFont.setFamily('Times New Roman')

# -------------------------Dark Theme--------------------------------------------------

country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Weather Forcast")
        self.setWindowIcon(self.WindowIcon)
        self.setMinimumSize(680, 1120)
        self.setMaximumHeight(1120)

        self.mainLayout = QVBoxLayout()

        self.layout1 = QVBoxLayout()

        self.country_comboBox = QComboBox()

        self.label_logo = QLabel()
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setPixmap(QPixmap('images/icon2.png').scaled(200, 200))

        self.label_title = QLabel("Weather Real-Time Forcast")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setFont(QFont('Times New Roman', 18, weight=QtGui.QFont.Bold, italic=True))

        self.country_comboBox.addItems(country_list)
        self.country_comboBox.setMaxVisibleItems(2)
        self.country_comboBox.setCurrentIndex(-1)
        self.country_comboBox.setPlaceholderText(str('--Select Country--'))

        self.getForcastBtn = QPushButton('Get Weather')
        self.getForcastBtn.clicked.connect(self.getWeather)
        self.getForcastBtn.setStyleSheet("background-color :rgb(43, 35, 90)")

        self.layout1.addWidget(self.label_logo)
        self.layout1.addWidget(self.label_title)
        self.layout1.addWidget(self.country_comboBox)
        self.layout1.addWidget(self.getForcastBtn)

        self.realtimeWeather = QBoxLayout(QBoxLayout.Direction.TopToBottom)

        self.currentTemp = QLabel()
        self.temperatureApparent = QLabel()
        self.humidity = QLabel()
        self.precipitation = QLabel()
        self.pressureSurfaceLevel = QLabel()
        self.uvIndex = QLabel()
        self.visibility = QLabel()
        self.windSpeed = QLabel()
        self.name = QLabel()

        self.realtimeWeather.addWidget(self.currentTemp)
        self.realtimeWeather.addWidget(self.temperatureApparent)
        self.realtimeWeather.addWidget(self.humidity)
        self.realtimeWeather.addWidget(self.precipitation)
        self.realtimeWeather.addWidget(self.pressureSurfaceLevel)
        self.realtimeWeather.addWidget(self.uvIndex)
        self.realtimeWeather.addWidget(self.visibility)
        self.realtimeWeather.addWidget(self.windSpeed)
        self.realtimeWeather.addWidget(self.name)

        self.mainLayout.addLayout(self.layout1)
        self.mainLayout.addLayout(self.realtimeWeather)
        self.mainLayout.addStretch(1)
        self.setLayout(self.mainLayout)
        self.adjustSize()

    # -------------------------Functions-----------------------------------------------START
    def getWeather(self):

        url = "https://api.tomorrow.io/v4/weather/realtime?location={}&apikey=...&units=metric".format("'" + str(self.country_comboBox.currentText()) + "'")

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)

        weather_data = response.json()
        print(weather_data)
        print("------------------------------------------------")

        ISOtime = weather_data['data']['time']

        currentTemp = weather_data['data']['values']['temperature']
        temperatureApparent = weather_data['data']['values']['temperatureApparent']
        humidity = weather_data['data']['values']['humidity']
        precipitation = weather_data['data']['values']['precipitationProbability']
        pressureSurfaceLevel = weather_data['data']['values']['pressureSurfaceLevel']
        uvIndex = weather_data['data']['values']['uvIndex']
        visibility = weather_data['data']['values']['visibility']
        windSpeed = weather_data['data']['values']['windSpeed']
        name = weather_data['location']['name']

        Time = datetime.fromisoformat(ISOtime)
        currentTimeZone = datetime.now().tzname()
        Time.astimezone(tz=currentTimeZone)

        self.currentTemp.setText(f'Temperature: {currentTemp}')
        self.temperatureApparent.setText(f'Temperature Apparent: {temperatureApparent}')
        self.humidity.setText(f'Humidity: {humidity}')
        self.precipitation.setText(f'Precipitation: {precipitation}')
        self.pressureSurfaceLevel.setText(f'Pressure Surface Level: {pressureSurfaceLevel}')
        self.uvIndex.setText(f'UV Index: {uvIndex}')
        self.visibility.setText(f'Visibility: {visibility}')
        self.windSpeed.setText(f'Wind Speed: {windSpeed}')
        self.name.setText(f'Country: {name}')

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
