from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetoworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
if __name__ =='__main__':
    try:
        trainingpiplineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpiplineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("initiate ingestiom")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e :
        raise NetoworkSecurityException(e,sys)