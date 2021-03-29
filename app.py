from flask import Flask, render_template, request
from forms import *

import requests, json
from datetime import date
from datetime import datetime
import threading, webbrowser

api_key = "b33f94a6ce5a75f0c19751c36ae20a98"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    today = date.today()
    d1 = today.strftime("%B %d, %Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    dict ={}
    city =""

    form = TextForm(request.form)
    if request.method == 'POST' and form.validate():
        city = form.city.data
        
        complete_url = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(complete_url)
        x = response.json()
        if x['cod'] != "404":
            y = x["main"]
            current_temperature = int(y["temp"]-273.15)
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            head = "Present Weather Condition"
            dict={'City':city,'Date':d1,'Current Time':current_time,'Temperature (in Celsius unit)':str(current_temperature),'Atmospheric pressure (in hPa unit)':str(current_pressure),'Humidity (in percentage)':str(current_humidiy),'Description':str(weather_description)}
    return render_template('index.html',result=dict)

if __name__=="__main__":
    port = 500
    url = "http://127.0.0.1:{0}".format(port)
    threading.Timer(1, lambda: webbrowser.open(url)).start()
    app.run(port=port,debug=False)
