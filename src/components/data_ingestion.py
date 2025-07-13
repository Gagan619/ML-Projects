# Data ingestion means data reading
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# Define Data ingestion path
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "data.csv")
   # make three files in artifacts folder

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    # This will read data from database
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            
            df = pd.read_csv('notebook/data/StudentsPerformance.csv')
            logging.info("Read the dataset as dataframe")

            # Make the directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # Saving to the raw data path
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            # saving to the train data path
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            # saving to the test data path
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )


        except Exception as e :
            raise CustomException(e,sys)
        

if __name__ == "__main__" :
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)