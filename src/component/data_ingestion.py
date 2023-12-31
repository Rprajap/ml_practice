import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join("artifacts",'train.csv')
    test_data_path:str = os.path.join("artifacts",'test.csv')
    raw_data_path:str = os.path.join("artifacts",'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingetion_config  = DataIngestionconfig()
    def initiate_data_ingedtion(self):
        logging.info("Entered data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read a dataset as a dataframe")
            os.makedirs(os.path.dirname(self.ingetion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingetion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set ,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingetion_config.train_data_path,index=False,header = True)
            test_set.to_csv(self.ingetion_config.test_data_path,index=False,header = True)
            logging.info('Ingestion of data is completed')
            return(

                self.ingetion_config.raw_data_path,
                self.ingetion_config.train_data_path,
                self.ingetion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
        obj = DataIngestion()
        obj.initiate_data_ingedtion()