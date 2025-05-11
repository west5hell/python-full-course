import sys
import os
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet(
            """ 
            QLabel, QPushButton{font-family: calibri;}
            QLabel#city_label{font-size: 40px;font-style:italic;}
            QLineEdit#city_input{font-size: 40px;}
            QPushButton#get_weather_button{font-size: 30px;font-weight: bold;}
            QLabel#temperature_label{font-size: 75px;}
            QLabel#emoji_label{font-size: 100px; font-family: Segoe UI emoji;}
            QLabel#description_label{font-size: 50px;}
            """
        )

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = os.environ.get("API_KEY")
        city = self.city_input.text()
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    print("Bad request\nPlease check your input")
                case 401:
                    print("Unauthorized\nInvalid API key")
                case 403:
                    print("Forbidden\nAccess is denied")
                case 404:
                    print("Not Found\nCity not found")
                case 500:
                    print("Internal Server Error\nPlease try again later")
                case 502:
                    print("Bad Gateway\nInvalid response from the server")
                case 503:
                    print("Service Unavailable\nServer is down")
                case 504:
                    print("Gateway Timeout\nNo response from the server")
                case _:
                    print(f"HTTP error occured\n{http_error}")

        except requests.exceptions.RequestException:
            pass

    def display_error(self, message):
        pass

    def display_weather(self, data):
        print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

{
    "coord": {"lon": 116.3972, "lat": 39.9075},
    "weather": [
        {"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04n"}
    ],
    "base": "stations",
    "main": {
        "temp": 290.09,
        "feels_like": 288.86,
        "temp_min": 290.09,
        "temp_max": 290.09,
        "pressure": 999,
        "humidity": 39,
        "sea_level": 999,
        "grnd_level": 994,
    },
    "visibility": 10000,
    "wind": {"speed": 2.76, "deg": 196, "gust": 6.57},
    "clouds": {"all": 51},
    "dt": 1746972006,
    "sys": {
        "type": 1,
        "id": 9609,
        "country": "CN",
        "sunrise": 1746911017,
        "sunset": 1746962282,
    },
    "timezone": 28800,
    "id": 1816670,
    "name": "Beijing",
    "cod": 200,
}
