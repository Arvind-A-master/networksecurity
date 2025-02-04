import sys 
from networksecurity.logging import logger
class NetoworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message =error_message
        _,_,exec_tb = error_details.exc_info()

        self.lineno = exec_tb.tb_lineno
        self.file_name = exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error Occured in python script name [{0}] Line number [{1}] error message[{2}]".format(
            self.file_name,self.lineno,str(self.error_message)
        )
if __name__ =='__main__':
    try:
        logger.logging.info("test logging")
        a=1/0
    except Exception as e :
        raise NetoworkSecurityException(e,sys)