import sys, os, logging, shutil
sys.path.append(os.path.dirname(__file__))
from variables import *
from getFileLines import getFileLines
from clear import clear
from Print import Print
from invalidOption import invalidOption
from question import question
from errorClasses import PositionalArgError, IncompatableArgsError, UnknownVars, CannotOverwrite, IncorrectFilePathError, IncorrectArgsError, IncorrectTypesError, UnknownError
from logger import logC
from validationChecker import checkPara
from fileTypeFinder import fileTypes
from createVar import createVar
maxBackupsallowed = 5
def Logging() -> None:
    needLogging = []
    if os.path.isdir("NTSModule/Loggers"):
        pass
    else:
        os.mkdir("NTSModule/Loggers")
        needLogging.append("Loggers folder created.")
    if os.path.isfile("NTSModule/Loggers/logger.log"):
        pass
    else:
        with open("NTSModule/Loggers/logger.log", "w") as openedFile:
            openedFile.write("")
        needLogging.append("'logger.log' file created.") 
    if os.path.isfile("NTSModule/Loggers/onetimelogger.log"):
        pass
    else:
        with open("NTSModule/Loggers/onetimelogger.log", "w") as openedFile:
            openedFile.write("")
        needLogging.append("'onetimelogger.log' file created.")
    if os.path.isdir("NTSModule/Loggers/backups"):
        pass
    else:
        os.mkdir("NTSModule/Loggers/backups")
        needLogging.append("NTSModule/Loggers/backups folder created.")
    loggerHandler = logging.FileHandler("NTSModule/Loggers/logger.log")
    oneTimeHandler = logging.FileHandler("NTSModule/Loggers/onetimelogger.log", "w")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s : %(asctime)s - {%(message)s} from %(pathname)s on line %(lineno)d',
        datefmt='%d-%b-%y %H:%M:%S',
        handlers=[loggerHandler, oneTimeHandler]
    )
    [logging.debug(debugMessage) for debugMessage in needLogging]
    if len(getFileLines("NTSModule/Loggers/logger.log")) > 100_000:
        x=0
        while True:
            if os.path.isfile(f"NTSModule/Loggers/backups/backuplogger{x}.log"):
                logging.error(f"Backup file true: {x}")
                x+=1
            else: 
                break

        with open(f"NTSModule/Loggers/backups/backuplogger{x}.log", "w") as o1:
            with open("NTSModule/Loggers/logger.log", "r") as o3:
                read = o3.readlines()
            o1.writelines(read)
        with open("NTSModule/Loggers/logger.log", "w") as o2:
            o2.write("")
    maxReached = len(os.listdir("NTSModule/Loggers/backups")) == maxBackupsallowed+1
    for file in os.listdir("NTSModule/Loggers/backups"):
        filePath = "NTSModule/Loggers/backups/"+file
        try:
            int(file[12])
            if maxReached:
                if int(file[12]) >= maxBackupsallowed or int(file[12]) <= 0:
                    os.remove(filePath)
                else:
                    os.rename(filePath, f"NTSModule/Loggers/backups/backuplogger{int(file[12])-1}.log")
        except ValueError:
            os.remove(filePath)
Logging()
del Logging, maxBackupsallowed
@logC()
def pycacheDel() -> None:
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    if os.path.isdir("NTSModule/__pycache__"):
        shutil.rmtree("NTSModule/__pycache__")
    if os.path.isdir("__pycache__"):
        shutil.rmtree("__pycache__")
    if os.path.isdir("NTSModule/pygameNTS/__pycache__"):
        shutil.rmtree("NTSModule/pygameNTS/__pycache__")
    if os.path.isdir("NTSModule/pygameNTS/ButtonClasses/__pycache__"):
        shutil.rmtree("NTSModule/pygameNTS/ButtonClasses/__pycache__")
pycacheDel()
del pycacheDel
from createInstaller import createInstaller, createModuleInstaller
logging.info(f"NTSModule imported successfully.")
clear()
Print(f"Module {GREEN}NTSModule{RESET} has been successfully imported!\nEnjoy!")
