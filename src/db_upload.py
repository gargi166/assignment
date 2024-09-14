import os 
from pymongo import MongoClient , errors
import pandas as pd 
import logger

# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

infoLog , errorLog = logger.getLogs()

def upload_TimeSeries_Data(df_timeseries):

    try:
        
        # Connect to MongoDB
        
        client_connection = MongoClient('mongodb://localhost:27017')

        #database
        database = client_connection['python_timeseries_db']

        # Create a time-series collection
        if('Airline_formated_data' not in database.list_collection_names()):
            database.create_collection('Airline_formated_data')
        
        print("Database connection set up successfully")
        collection = database['Airline_formated_data']

        # Convert DataFrame to dictionary and than enter each record into MongoDB
        df_timeseries=pd.DataFrame(df_timeseries)
       
        records = df_timeseries.to_dict(orient='records')
        for record in records:
            
            collection.insert_one(record)

        
        
        print("Data inserted in Collection successfully.")
        return ({"Info":"Data inserted in Collection successfully."})

    except (errors.ConnectionFailure, errors.ConfigurationError, errors.OperationFailure) as e:
        raise RuntimeError(f"Error in Connection with MongoDB: {e}")
        return ({"Error":"RuntimeError :Error in Connection  with MongoDB"})
        

    except Exception as e :
        errorLog({"Error":f"Unknown error occur {e}"})
        return ({"Error":f" unknown error occur {e}"})
    
