import sys, os, logging
sys.path.append(os.path.dirname(__file__))
from variables import *
from getFileLines import getFileLines
from clear import clear
from Print import Print
from invalidOption import invalidOption
from question import question
from errorClasses import *

clear()
Print(f"Module {GREEN}NTSModule{RESET} has been successfully imported!\nEnjoy!")

def Logging() -> None:
    if os.path.isdir("Loggers"):
        pass
    else:
        os.mkdir("Loggers")
    if os.path.isfile("Loggers/logger.log"):
        pass
    else:
        with open("Loggers/logger.log", "w") as openedFile:
            openedFile.write("")
    if os.path.isfile("Loggers/onetimelogger.log"):
        pass
    else:
        with open("Loggers/onetimelogger.log", "w") as openedFile:
            openedFile.write("")
    if os.path.isdir("Loggers/backups"):
        pass
    else:
        os.mkdir("Loggers/backups")

    loggerHandler = logging.FileHandler("Loggers/logger.log")
    oneTimeHandler = logging.FileHandler("Loggers/onetimelogger.log", "w")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s : %(asctime)s - {%(message)s} from %(pathname)s on line %(lineno)d',
        datefmt='%d-%b-%y %H:%M:%S',
        handlers=[loggerHandler, oneTimeHandler]
    )

    if len(getFileLines("Loggers/logger.log")) > 100_000:
        x=0
        while True:
            if os.path.isfile(f"Loggers/backups/backuplogger{x}.log"):
                x+=1
                logging.error(f"Backup file true: {x}")
            else: 
                break

        with open(f"Loggers/backups/backuplogger{x}.log", "w") as o1:
            with open("Loggers/logger.log", "r") as o3:
                read = o3.readlines()
            o1.writelines(read)
        with open("Loggers/logger.log", "w") as o2:
            o2.write("")

Logging()
del Logging

logging.info(f"NTSModule imported successfully.")