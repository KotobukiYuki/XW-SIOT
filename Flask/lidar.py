# -*- coding: utf-8 -*
import serial
import time, sys
from time import strftime
import os
import pandas as pd

ser = serial.Serial("/dev/ttyAMA0", 115200)
filename = 'distance_log.csv'

def getTFminiData():
    while True:
        full_date = strftime("%Y-%m-%d")
        full_time = strftime("%H:%M:%S")
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)   
            ser.reset_input_buffer() 
            
            if recv[0] == 0x59 and recv[1] == 0x59:     #python3
                distance = recv[2] + recv[3] * 256
                if distance < 100:
                    storeDistData(full_date, full_time, distance)
                else:
                    distance = 100
                    storeDistData(full_date, full_time, distance)
                ser.reset_input_buffer()
        
        time.sleep(1)
                

def storeDistData(date, time, distance):
        new_data = pd.DataFrame([[date, time, distance]], columns=['Date', 'Time', 'Distance'])
        new_data.to_csv(filename, mode='a', header=False, index=False)
    

if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        getTFminiData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()