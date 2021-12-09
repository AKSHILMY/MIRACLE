# I will use the .csv file dataset for New York City Daily Temperature From 1869 to 2021
# .. The file is too large and contains 10000+ rows
# https://www.kaggle.com/shaneysze/new-york-city-daily-temperature-18692021
 

import pandas as pd                    
data = pd.read_csv('nyc_temp_1869_2021.csv', sep=',', header= 0, index_col=False )     # load data from .csv file 
data.drop('Unnamed: 0', axis=1, inplace=True)       # removing unnecessary first column 
data['average_temp'] = data[['TMAX', 'TMIN']].mean(axis=1)           # calculating the average of maximum and minimum temperatures 
data.head(11680)


# importing matplotlib with pyplotlib 
import matplotlib.pyplot as plt 
import numpy as np 

plt.style.use('seaborn-whitegrid')

# # (TOP PLOT): is supposed to show the Monthly comparison between Minimum, Maximum and Average Calculated temperatures 
fig = plt.figure(figsize=[14,10])
grouped_data = data.groupby(data["MONTH"])

def bar(fig):
    ax_top = plt.subplot(211)

    grouped_data['TMAX'].max().plot(color='red', ax=ax_top, kind='bar')
    grouped_data['TMIN'].min().plot(color='blue', ax=ax_top, kind ='bar')
    grouped_data['TMAX'].mean().plot(color='salmon', ax=ax_top, kind='bar')
    grouped_data['TMIN'].mean().plot(color='aqua', ax=ax_top, kind='bar')

    plt.xlabel('Day of Year')
    plt.ylabel('Min and Max averages (per day)')
    plt.title('Min and Max temperatures  of NYC compared with their averages')
    plt.legend(loc="upper left")

    return 'bar.html'

def line(fig):
    # (BOTTOM LEFT SUBPLOT): shows the 12 months rolling average of the temperature in NYC
    ax_b1 = plt.subplot(223)

    data['simple_rolling'] = data['average_temp'].rolling(12).mean()
    grouped_data['simple_rolling'].mean().plot(ax=ax_b1)


    plt.xlabel('Month')
    plt.ylabel('12 month moving average')
    plt.title('Moving Average of Temperature of 12 months')
    # plt.show()
    plt.legend(loc="upper left")
    return 'line.html'


def scatter(fig):
    # (BOTTOM RIGHT SUBPLOT):  shows accumulated moving average of temperature 
    ax_b2 = plt.subplot(224)

    data['ACC_Ave'] = data['average_temp'].expanding().mean()              #calculating accumulated moving average 
    plt.scatter(data['MONTH'], data['TMAX'], marker= 'o', color= 'red')
    plt.scatter(data['MONTH'], data['TMIN'], marker= 'o', color = 'blue')
    plt.plot(data['MONTH'], data['ACC_Ave'], color='black')

    plt.xlabel('Month')
    plt.ylabel('Temperature comparison')

    return 'scatter.html'

import mpld3
# mpld3.save_html(fig, line(fig)) 
# mpld3.save_html(fig, bar(fig)) 
# mpld3.save_html(fig, scatter(fig)) 
