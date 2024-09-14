import matplotlib.pyplot as plt
import pandas 
import seaborn as sns
import logger 

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
    sns.scatterplot(data=df_time_series, x="Formated_Date", y=column, hue="seasons", style="seasons")

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
        #line plot for each numerical value 
        numerical_col = ["Baggage","Scheduled",	"Cancelled","Enplaned"]
        print("visual ",df_time_series)
        for col in numerical_col:
            linePlot(df_time_series, col)

        #Scatter plot withe respec to season 
        for col in numerical_col:
            scatterplot_Compareto_Season(df_time_series, col)

        # heatMap of correlation matrix 
        print(df_time_series.corr())
        # Plotting correlation heatmap
        sns.heatmap(df_time_series.corr(), cmap="YlGnBu", annot=True)
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
