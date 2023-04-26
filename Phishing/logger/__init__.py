import logging
import os
from datetime import datetime

#loging file name
file_name = f"Logs_{datetime.now().strftime('%d%m%y_%H%M%S')}.log"

#log file directory
Log_File_Dir = os.path.join(os.getcwd(),'Logs')

#Create dir
os.makedirs(Log_File_Dir,exist_ok=True)

##Logging file path
LOG_FILE_PATH = os.path.join(Log_File_Dir,file_name)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format=f"[%(asctime)s] : %(lineno)d - %(name)s - %(levelname)s - %(message)s"
)
