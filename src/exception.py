import sys
import logging

'''
this custom class will be used through out the entire project, for any exception
'''
# custom error message showing the file, line number, and message
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{0}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
   
class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_details)

    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Dividing by Zero Error")
        raise CustomException(e, sys)