#!/usr/bin/env python3

"""
Get weather data from openweathermaps.org

Usage:
    weather [options] <City/tdl>
    weather [-hv] <City/tdl>

Options:
    -h, --help  Print this screen and exit.
    -v, --version  Print version number and exit.
"""

__version__ = 0.1

from datetime import datetime
from docopt import docopt
import requests

BASEURL = "http://api.openweathermap.org/data/2.5/weather?q="


def getopt():
    '''Return Options'''
    return docopt(__doc__)


def splitCityTdl(citytdl):
    '''splits city/tdl -> city, tdl'''
    city, tdl = citytdl.split("/")
    return city, tdl


def mkurl(city, tdl):
    '''generate url from city and tdl'''
    destination = ",".join((city, tdl))
    url = "".join((BASEURL, destination))
    return url


def getweather(url):
    '''Return weather dict'''
    try:
        weather = requests.get(url)
        return weather.json()
    except requests.exceptions.ConnectionError():
        return False


def K2C(kelvin):
    '''Kelvin to Celsius'''
    celsius = kelvin-273.15
    return celsius


def symbolFromId(ID):
    '''return symbol equivalent to the OWM condition code'''
    if ID in range(200, 300):   # Thunderstorm
        return "⚡"
    if ID in range(300, 400):   # Drizzle
        return "☂"
    if ID in range(500, 600):   # Rainy
        return "☔"
    if ID in range(600, 700):   # Snowy
        return "❄"
    if ID in range(801, 900):   # Cloudy
        return "☁"
    if ID == 800:               # Sunny/ Clear sky
        return "☀"
    if ID in range(900, 907):   # Extreme
        return "⚠"
    else:
        return "★"


# def getweatherdata(weatherjson):
#     main = weatherjson['main']
#     TODO AND THE REST


def mkweatherdata(pressure, humidity, temp, tempMax, tempMin):  # FIXME: Refactor this mess
    '''Return a string with SI units'''
    data = [(pressure, "[hPa]"),
            (humidity, "[%]"),
            (temp, "[°C]"),
            (tempMax, "[°C]"),
            (tempMin, "[°C]")]
    weatherlist = ["{:.2f}{}".format(*item) for item in data]
    return weatherlist


def getWeatherDescription(weather):
    '''return description'''
    return weather['weather'][0]['description'].capitalize()


def getWeatherId(weather):
    '''return weather id'''
    return weather['weather'][0]['id']


def getTime():
    now = datetime.now()
    return now.strftime('%H:%M')

if __name__ == '__main__':
    opt = getopt()                               # Get options ...
    city, tdl = splitCityTdl(opt['<City/tdl>'])  # ... get the city ...
    url = mkurl(city, tdl)                       # ... to make an url ...
    weather = getweather(url)                    # ... request data ...
    if weather:                                  # ... if sucessful...
        weatherDict = {'data': mkweatherdata(    # ... format data ...
            weather['main']['pressure'],
            weather['main']['humidity'],
            K2C(weather['main']['temp']),
            K2C(weather['main']['temp_max']),
            K2C(weather['main']['temp_min']),
            ),
            'desc': getWeatherDescription(weather),
            'symbol': symbolFromId(getWeatherId(weather))
            }
        print("\t".join(                         # ... and print it out.
            (
                getTime(),
                weatherDict['desc'],
                "    ".join(('\t', weatherDict['symbol'], '\t')).join(weatherDict['data']),
                )
            )
            )
    else:
        print("Connection Error")
