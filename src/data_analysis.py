"""



"""

import pandas as pd 
import logger
import os

# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

infoLog , errorLog = logger.getLogs()


def dataSet_Analysis(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError({"Error":f"file doesn't exit"})
        
        # read the csv file to panda dataframe 
        df_time_series = pd.read_csv(file_path)

        #10 samples from dataset
        df_time_series.sample(10) 

        # print all Columns in dataset
        print("columns in dataset",df_time_series.columns)

        # print each column null values and datatype
        print("Brief info of each column",df_time_series.info())

        # Statistical analysis for each column 
        print("Statical info for each numerical column",df_time_series.describe())
         
        # datatype of each column
        print("datatype of each column" ,df_time_series.dtypes)
        
        # number of airline present in the data
        print(" Airline present in the data")
        print(df_time_series["Airline"].unique())

        ## total number of unique dates
        print(df_time_series["Date"].value_counts().count())

        #year involve in the data
        df_time_series["Year"].unique()

       # Reframing the date column 
        df_time_series["Formated_Date"]= (pd.to_datetime(df_time_series['Year'].astype(str)  +df_time_series['Month'].astype(str), format='%Y%m'))
        df_time_series['Formated_Date'] = pd.to_datetime(df_time_series['Formated_Date']).dt.normalize()

        df_time_series.drop(columns=["Date"])
        print(df_time_series.head())

        # Yearly Cancellation of flight and Average Cancellation of flight
        Yearly_cancellation =  df_time_series.groupby('Year')['Cancelled'].sum()
        Average_Yearly_cancellation =  df_time_series.groupby('Year')['Cancelled'].mean()
        print("Yearly_cancellation",Yearly_cancellation)
        print("Average_Yearly_cancellation",Average_Yearly_cancellation)

        # Yearly Cancellation pf flight for each flight_airline
        Yearly_cancellation_foreach =  df_time_series.groupby(['Year',"Airline"])['Cancelled'].sum()
        print("Yearly_cancellation_foreach year ",Yearly_cancellation_foreach)

        # Avearge Yearly Cancellation of flight for each flight_airline
        Average_Yearly_cancellation_foreach =  df_time_series.groupby(['Year','Airline'])['Cancelled'].mean()
        print("Average_Yearly_cancellation_foreach year",Average_Yearly_cancellation_foreach)

        # Maximum cancellation of flight for which 3 months
        Cancellation_foreach_month = df_time_series.groupby("Month")["Cancelled"].sum().head(3)
        print("Top 3 months having hightes Cancellation",Cancellation_foreach_month)

        # how passage baggage complaint is affecting the cancellation of flight for a each airline
        # Calculate correlation coefficient
        correlation = df_time_series['Cancelled'].corr(df_time_series['Baggage'])
        print(f'Correlation coefficient between Cancelled and Baggage: {correlation:.2f}')
        

        df_time_series.groupby("Airline")["Cancelled"].sum().head(3)

        # In which year maximum passenger onboaded 
        max_year_pass_onboaded=df_time_series.groupby("Year")["Enplaned"].sum().sort_values().head(1)
        print("Year in which msximum passanger onboard", max_year_pass_onboaded)

        # which flight is most trustworthy 
        df_analysis = df_time_series.groupby("Airline").apply(lambda x: pd.Series({ 
                                                        'boaded_flight': x['Scheduled'].sum()-x['Cancelled'].sum(),
                                                        'Cancelled_flight': x['Cancelled'].sum(),
                                                        'Scheduled_flight':x['Scheduled'].sum(),
                                                    }))
                                                    
        df_analysis["percentage_of_suncessfull_flight"]=(df_analysis["boaded_flight"]/df_analysis["Scheduled_flight"])*100
        print(df_analysis.head())

        #sessonal flight evalution 
        def month_to_season(month_num):
            if month_num in [12, 1, 2]:
                return 'Winter'
            elif month_num in [3, 4, 5]:
                return 'Spring'
            elif month_num in [6, 7, 8]:
                return 'Summer'
            elif month_num in [9, 10, 11]:
                return 'Fall'
            else:
                return 'Invalid month'
            
        df_time_series["seasons"]=[month_to_season(m) for m in df_time_series["Month"]]
        print(df_time_series)

        # seasonal dependency on the flight 
        df_time_series.groupby("seasons")[['Scheduled','Cancelled']].sum().sort_values('Cancelled')
         
        infoLog({"Info":"Dataset Analysis done"})
        print({"Info":"Dataset Analysis"})
        return df_time_series
        
             
        
    except FileNotFoundError as e :
        errorLog({"ERROR":f"file doesn't exit"})  
        return {"Error":f"file doesn't exit"}
    
    except Exception as e:
        errorLog({"ERROR":f"Unknown error occur :{e}"})  
        return {"Error":f"Unknown error occur :{e}"}

        
