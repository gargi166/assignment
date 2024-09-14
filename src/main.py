"""
main function will intiate the whole application
it will handle the flow of the data 
Call different modules for the data flow
call logger module for error handling 


"""
from data_analysis import dataSet_Analysis
from data_preprocessing import data_Preprocessing
from data_visualization import visualPlots
from db_upload import upload_TimeSeries_Data
import argparse
import logger
import os

# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

infoLog , errorLog = logger.getLogs()



def timeseries_dataset_flow(file_path):
    try :
        if not os.path.exists(file_path):
            raise FileNotFoundError({"Error":f"file doesn't exit"})
        
        # Call for analysis of dataset
        timeseries_dataset = dataSet_Analysis(file_path)
       
        
        #Call for preprocessing 
        timeseries_dataset = data_Preprocessing(timeseries_dataset)
        
        print( "preprocessed",timeseries_dataset)
       
       #Call for Time Series Visualization 
        visualPlots(timeseries_dataset)

        #upload data to the database 
        message = upload_TimeSeries_Data(timeseries_dataset)
        print(message)
            


    except FileNotFoundError as e :
        errorLog({"ERROR":"file doesn't exit"})  
        return {"Error":"file doesn't exit"}
    except Exception as e :
        errorLog({"ERROR":f"Unknown error occur:{e}"})  
        return {"Error":f"Unknown error occur :{e}"}
    

    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="takes timeseries dataset from input")

    # Adding argument
    parser.add_argument("file_path",type=str,help ="path of the dataset")

    # parsing argument
    args = parser.parse_args()

    if args.file_path:
        print("File parsed sucessfully to the application ")

        #passing file path to process differnt operation in dataset 
        #file_path ='C:/Users/gargi/DATA Science/python_dataset/baggagecomplaints.csv'
        return_statement= timeseries_dataset_flow(args.file_path)

    else:
        print("file fail to parsed, Try again ")
    

 