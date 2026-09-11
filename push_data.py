import os
import sys
import json

import pandas as pd
import numpy as np
import pymongo

# Custom exception and logging modules from your project
from Network_Security.src.exception.exception import CustomException
from Network_Security.src.logging.logger import logging

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()


# Get MongoDB connection string from environment
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)  # Debug: confirm the URI is loaded

import certifi
ca = certifi.where()  # Path to SSL certificates (used for secure MongoDB connections)




class NetworkDataExtract:
    """
    A class to handle data extraction from CSV and insertion into MongoDB.
    """

    def __init__(self):
        try:
            # Currently no initialization logic, but error handling is ready
            pass
        except Exception as e:
            raise CustomException(e, sys)

    def csv_to_json_convertor(self, file_path):
        """
        Reads a CSV file and converts it into a list of JSON records (dicts).
        Args:
            file_path (str): Path to the CSV file.
        Returns:
            list: List of JSON-like dictionaries representing rows.
        """
        try:
            # Read CSV into pandas DataFrame
            data = pd.read_csv(file_path)

            # Reset index to avoid issues with row numbers
            data.reset_index(drop=True, inplace=True)

            # Convert DataFrame to JSON records (list of dicts)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        """
        Inserts records into a MongoDB collection.
        Args:
            records (list): List of JSON-like dictionaries to insert.
            database (str): Name of the MongoDB database.
            collection (str): Name of the MongoDB collection.
        Returns:
            int: Number of records inserted.
        """
        try:
            # Save parameters
            self.database = database
            self.collection = collection
            self.records = records

            # Connect to MongoDB using URI from .env
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            # Select database
            self.database = self.mongo_client[self.database]

            # Select collection
            self.collection = self.database[self.collection]

            # Insert records
            self.collection.insert_many(self.records)

            # Return number of records inserted
            return len(self.records)
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    # File path to your CSV dataset
    FILE_PATH = "dataset\\phisingData.csv"

    # MongoDB database and collection names
    DATABASE = "aneeshjose012_db_user"
    COLLECTION = "NetworkData"

    # Create object of NetworkDataExtract
    networkobj = NetworkDataExtract()

    # Convert CSV to JSON records
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)  # Debug: print records before insertion

    # Insert records into MongoDB
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"Inserted {no_of_records} records into MongoDB.")
