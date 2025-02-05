from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation,DataTransformationConfig
from networksecurity.exception.exception import NetoworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
if __name__ =='__main__':
    try:
        trainingpiplineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpiplineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("initiate ingestiom")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("initiate ingestion completed")
        data_validation_config = DataValidationConfig(trainingpiplineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("initiate validation completed")
        print(data_validation_artifact)
        logging.info("initiate transformation started")
        data_transformation_config = DataTransformationConfig(trainingpiplineconfig)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("initiate transformation completed")
        print(data_transformation_artifact)


    except Exception as e :
        raise NetoworkSecurityException(e,sys)