# -*- coding: utf-8 -*
from flask import Flask, render_template, Response, jsonify
import subprocess
import csv
import fan as fan


app = Flask(__name__)

# Initialising the Web Server and load "hardware drives" as subprocess.
process1 = subprocess.Popen(['python', 'lidar.py'])
process2 = subprocess.Popen(['python', 'environment_sensor.py'])


@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/distance')
def showDistance():
    return render_template('distance.html')

@app.route('/temperature')
def showTemperature():
    return render_template('temperature.html')

@app.route('/humidity')
def showHumidity():
    return render_template('humidity.html')

@app.route('/getLatestDistance')
def getLatestDistance():
    try:
        with open('distance_log.csv', 'r') as file:
            last_row = list(csv.reader(file))[-1]
            return jsonify({'date': last_row[0], 'distance': last_row[2]})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/getDistanceData')
def getDistanceData():
    try:
        with open('distance_log.csv', 'r') as file:
            csv_data = list(csv.reader(file))
            return jsonify(csv_data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/getEnvData')
def getEnvData():
    try:
        with open('temperature_humidity_log.csv', 'r') as file:
            csv_data = list(csv.reader(file))
            return jsonify(csv_data)
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/getLatestTemperature')
def getLatestTemperature():
    try:
        with open('temperature_humidity_log.csv', 'r') as file:
            last_row = list(csv.reader(file))[-1]
            return jsonify({'date': last_row[0], 'temperature': last_row[2]})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/get_latest_humidity')
def get_latest_humidity():
    try:
        with open('temperature_humidity_log.csv', 'r') as file:
            last_row = list(csv.reader(file))[-1]
            return jsonify({'date': last_row[0], 'humidity': last_row[3]})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_humidity_data')
def get_humidity_data():
    try:
        with open('temperature_humidity_log.csv', 'r') as file:
            csv_data = list(csv.reader(file))
            return jsonify(csv_data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/fan/auto')
def fanOn():
    fan.fanOn()
    return 'auto'

@app.route('/fan/off')
def fanOff():
    fan.fanOff()
    return 'Off'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, ssl_context='adhoc')