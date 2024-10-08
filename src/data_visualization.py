import matplotlib.pyplot as plt
import pandas 
import seaborn as sns
import logger 
import pandas as pd
infoLog , errorLog = logger.getLogs()

def linePlot(df_time_series, column):
    # Plot the time series data
    
    plt.figure(figsize=(12, 6))
    print()
    sns.lineplot(x=df_time_series["Formated_Date"], y=df_time_series[column], label=column, marker='o')

    # Adding titles and labels
    plt.title('Time Series Plot with Seaborn')
    plt.xlabel('Formated_Date')
    plt.ylabel(column)
    plt.legend()
    plt.grid(True)


def scatterplot_Compareto_Season(df_time_series,column):
    try:
        sns.scatterplot(df_time_series["Formated_Date"], y=df_time_series[column], hue=df_time_series["seasons"], style=df_time_series["seasons"])
        plt.title('Scatter Plot with seasons')
        plt.xlabel('Formated_Date')
        plt.ylabel(column)
        plt.legend()
        plt.grid(True)
    
    except Exception as e:
        errorLog({"ERROR":f"UNknown error occur {e}"})
    
    
def histogram_Plot(df_time_series,column):
    plt.figure(figsize=(12, 6))
    plt.hist(df_time_series[column], bins=30, edgecolor='k', alpha=0.7)
    plt.title('Histogram of Time Series Data')
    plt.xlabel('column')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    

# Display the plot
plt.show()

def visualPlots(df_time_series):

    try:

        df_time_series = pd.DataFrame(df_time_series)
        
        
        
        numerical_col = ["Baggage","Scheduled",	"Cancelled","Enplaned"]
        #line plot for each numerical value 
        for col in numerical_col:
            linePlot(df_time_series, col)
   
        #Scatter plot withe respec to season 
        for col in numerical_col:
            scatterplot_Compareto_Season(df_time_series, col)

        # heatMap of correlation matrix 
        print(df_time_series.corr(numeric_only=True))
        # Plotting correlation heatmap
        sns.heatmap(df_time_series.corr(numeric_only=True), cmap="YlGnBu", annot=True)
        # Displaying heatmap
        plt.show()
        
        
        #boxplot for each numeric value
        for col in numerical_col:
            histogram_Plot(df_time_series, col)
        
        infoLog({"Info ":"Plotted all the require conditions"})
        return {"Info ":"Plotted all the require conditions"}

    except Exception as e:
        errorLog({"Error":f"Unknown Error Occur :{e}"})
        return {"Error":f"Unknown Error Occur :{e}"}
