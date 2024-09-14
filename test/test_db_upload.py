import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from pymongo import MongoClient, errors
from pymongo.collection import Collection
import mongomock
import os 
import sys 
from datetime import datetime


# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Assuming upload_TimeSeries_Data function is imported from your module

from db_upload import upload_TimeSeries_Data

class TestUploadTimeSeries(unittest.TestCase):
    @patch("pymongo.MongoClient",new_callable=mongomock.MongoClient)
    def test_upload_success(self, mock_client):
        

        # New Sample time series data DataFrame
        data_test ={'Airline': 'United' ,'seasons': ['Winter']}

        df_test = pd.DataFrame(data_test)
        # Call the orignal function
        result_test = upload_TimeSeries_Data(df_test)
        print("result",result_test)
        # Check test result
        self.assertEqual(result_test, ({"Info":"Data inserted in Collection successfully."}))

        # Check data in MongoDB
        
        
        # Access the mocked MongoDB client to verify data
        db = mock_client['python_timeseries_db']
        collection = db['Airline_formated_data']
        

        # Simulate a connection failure
        mock_client.side_effect = errors.ConnectionFailure({"ERROR":"Connection failed error"})
        # Call the function and assert exception
        with self.assertRaises(RuntimeError):
            upload_TimeSeries_Data(df_test )

        # Simulate a different kind of exception
        mock_client.side_effect = Exception({"ERROR":"Unknown error"})
        # Call the function and assert exception
        with self.assertRaises(RuntimeError):
            upload_TimeSeries_Data(df_test)
    


    


        


        
    


if __name__ == '__main__':
    unittest.main()