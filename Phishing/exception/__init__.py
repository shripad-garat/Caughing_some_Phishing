from Phishing.logger import logging
import sys

def get_error_message(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured on line no {exc_tb.tb_lineno} in file name {file_name} and error is {error}"
    logging.error(error_message)
    return error_message

class My_Exception(Exception):

    def __init__(self,error,error_detail:sys) :
        self.error = error
        self.error_details = error_detail
        self.error_message = get_error_message(error=self.error,error_details=self.error_details)

    def __str__(self) -> str:
        return self.error_message
