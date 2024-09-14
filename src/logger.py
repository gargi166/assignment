from logging import handlers
import logging
import  os 


'''
-------------------------------- HOW TO USE -------------------------------------
#       from src import logger                                                  #
#       infoLog , errorLog = logger.getLogs()                                   #
#       infoLogs(Info Level Logs)   // Use where ever required to Log Info      #
#       errorLog(Error Level Logs)  // Use where ever required to Log Error     #
---------------------------------------------------------------------------------
'''

'''
Simple Logging Utility
    - Import In your Library and Call in exception
'''
BASEDIR = os.getcwd() + '/'         # Get it from OS.envron
LOGDIR = BASEDIR + 'logs/'
LOGFILE = 'api-server.log'
ERRLOGFILE = 'errors.log'

LOGFILE_PATH = LOGDIR+LOGFILE
ERRORFILE_PATH = LOGDIR+ERRLOGFILE
MAX_FILE_SIZE = 50000 # 50MB
BACKUP_COUNT = 3 # 3 old backups

# Handle Log Dir Doesn't Exist:
try:
    os.makedirs(LOGDIR)
except Exception as E:
    pass    # Nothing to do, project will fail

info_logger = logging.getLogger('info_logger')
error_logger = logging.getLogger('error_logger')

info_logger.setLevel(logging.INFO)
error_logger.setLevel(logging.ERROR)


LOG_FORMAT = logging.Formatter(f'%(asctime)s %(module)s:%(lineno)s %(funcName)s- %(levelname)s :- %(message)s')
ERROR_FORMAT = logging.Formatter(f'%(asctime)s %(module)s:%(lineno)s %(funcName)s- %(levelname)s :- %(message)s')
info_handler = handlers.RotatingFileHandler(LOGFILE_PATH, mode='a', maxBytes=MAX_FILE_SIZE, backupCount=BACKUP_COUNT)
error_handler = handlers.RotatingFileHandler(ERRORFILE_PATH, mode='a', maxBytes=MAX_FILE_SIZE, backupCount=BACKUP_COUNT)

info_handler.setFormatter(LOG_FORMAT)
error_handler.setFormatter(ERROR_FORMAT)

info_logger.addHandler(info_handler)
error_logger.addHandler(error_handler)


def getLogs():
    infoLog = info_logger.info
    errorLog = error_logger.error
    return infoLog , errorLog