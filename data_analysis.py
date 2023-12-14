import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_distance = pd.read_csv('/content/distance_log_week_raw.csv')
df_distance['datetime'] = pd.to_datetime(df_distance['date']+' '+df_distance['time'], format='%Y-%m-%d %H:%M:%S')
df_distance.set_index('datetime', inplace=True)
df_distance = df_distance.drop(columns=['date', 'time'])
#df_distance.head()
#df_distance.info()
df_distance.to_csv('distance_log_week_clean.csv', index= True)
#df_distance.plot() 

df_temp = pd.read_csv('/content/temperature_humidity_log_week_raw.csv')
df_temp['datetime'] = pd.to_datetime(df_temp['date']+' '+df_temp['time'], format='%Y-%m-%d %H:%M:%S')
df_temp.set_index('datetime', inplace=True)
df_temp = df_temp.drop(columns=['date', 'time', 'humidity'])
#df_temp.head()
#df_temp.info()
#df_temp.plot()

df_humid = pd.read_csv('/content/temperature_humidity_log_week_raw.csv')
df_humid['datetime'] = pd.to_datetime(df_humid['date']+' '+df_humid['time'], format='%Y-%m-%d %H:%M:%S')
df_humid.set_index('datetime', inplace=True)
df_humid.to_csv('temperature_humidity_log_week_clean.csv', index= True)
df_humid = df_humid.drop(columns=['date', 'time', 'temperature'])
#df_humid.head()
#df_humid.info()
#df_humid.plot()
