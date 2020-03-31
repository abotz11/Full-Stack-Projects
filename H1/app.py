from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/weather/<city>')
def weather(city):
    secret = 'fcbd0b49aeaedc2399b10f80545ae74a'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': secret}
    response = requests.get(url=url, params=params)
    temp = str(response.json()['main']['temp'])

    secret = 'rJpFA71VGRqlilGAUyTUffsNVJMTnzqL'
    url = 'https://api.giphy.com/v1/gifs'
    
    if float(temp) > 30:
        ids = 'xT0Gqz4x4eLd5gDtaU'
    elif float(temp) > 14:
        ids = 'xUPJPs6FDhr3B7AI9O'
    else:
        ids = 'cGymv7T9ZzDdLGczy7'

    param ={'ids': ids, 'api_key': secret}
    response = requests.get(url=url, params=param)
    image = "<br><img src=" + str(response.json()['data'][0]['images']['downsized']['url']) + ">"

    return 'Temperature in ' + city + ' is: ' + temp + image


if __name__ == "__main__":
    app.run()

