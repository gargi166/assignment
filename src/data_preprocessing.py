# import necessary modules
import os 
import pandas as pd
import numpy as np
import logger
import matplotlib.pyplot as plt

# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

infoLog , errorLog = logger.getLogs()

def plotOutliner(df_timeseries,df_timeseries_outlier,value):
    
    # Plot the time series data
    plt.figure(figsize=(12, 6))
    plt.plot(df_timeseries.index, df_timeseries[value], label=value, color='b', linestyle='-', marker='o')

    # Plot outliers
    plt.scatter(df_timeseries_outlier.index,df_timeseries_outlier[value], color='Black', label='Outliers', marker='X')

    # Adding titles and labels
    plt.title('Time Series Plot with Outliers')
    plt.xlabel('Formated_Date')
    plt.ylabel(value)
    plt.legend()

    # Display the plot
    plt.grid(True)
    plt.show()


def removeOutliner(df_time_series,column_name):
        
    Q1 = df_time_series[column_name].quantile(0.25)
    Q3 = df_time_series[column_name].quantile(0.75)
    IQR = Q3 - Q1

    df_timeseries_outliers = df_time_series[(df_time_series[column_name] < (Q1 - 1.5 * IQR)) | (df_time_series[column_name] > (Q3 + 1.5 * IQR))]
    print(column_name+" Outliers:")
    print(df_timeseries_outliers) 

    #plot outlier
    plotOutliner(df_time_series,df_timeseries_outliers,column_name)

    #remove Outlier 
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_time_series_cleaned = df_time_series[(df_time_series[column_name] >= lower_bound) & (df_time_series[column_name] <= upper_bound)]
    
    return  df_time_series_cleaned
    

       



def data_Preprocessing(df_time_series):
    try:
        df_time_series = pd.DataFrame(df_time_series)
        if  df_time_series.empty:
           return ({"Error" : "Data failure to pass to preprocessing module"})
        
        #convert the Formated date to date time
        df_time_series["Formated_Date"] = pd.to_datetime(df_time_series['Formated_Date'])

        # droping entries with null value 
        df_time_series.fillna(method='ffill', inplace=True)  # average filling 
        
        # remove duplicate values
        df_time_series.drop_duplicates(inplace=True)
        
        #Column from which outlier need to be removed
        outliner_col = ["Baggage","Scheduled",	"Cancelled","Enplaned"]
        #Outliners identification using Interquartile range and removing them 
        for col in outliner_col:
            df_time_series = removeOutliner(df_time_series,col)

        infoLog({"Info": "Preprocessing done Successfully"})
        return df_time_series

    except Exception as e :
        errorLog({"Error" : f"Unknown error occur :{e}"})
        return ({"Error" : f"Unknown error occur :{e}"})
    
 