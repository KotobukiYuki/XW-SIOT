# -*- coding: utf-8 -*
import board
import adafruit_dht
import time, sys
from time import strftime
import os
import pandas as pd

filename = 'temperature_humidity_log.csv'
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18)

def getDHT11Data():
    while True:
        try:
            # Print the values to the serial port
            full_date = strftime("%Y-%m-%d")
            full_time = strftime("%H:%M:%S")
            temperature = round(dhtDevice.temperature, 1) # Keep 1 decimal place for temperature
            humidity = int(dhtDevice.humidity)
            storeTempHumData(full_date, full_time, temperature, humidity)
            #print(temperature)


        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(10)

def storeTempHumData(date, time, temperature, humidity):
    new_data = pd.DataFrame([[date, time, temperature, humidity]], columns=['Date', 'Time', 'Temperature', 'Humidity'])
    new_data.to_csv(filename, mode='a', header=False, index=False)

if __name__ == '__main__':
    try:
        getDHT11Data()
    except KeyboardInterrupt:   # Ctrl+C
        print("ENV_STOP!")