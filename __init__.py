import sys, os, logging, shutil
sys.path.append(os.path.dirname(__file__))
from variables import *
from getFileLines import getFileLines
from clear import clear
from Print import Print
from invalidOption import invalidOption
from question import question
from errorClasses import *
from logger import logC
from validationChecker import checkPara
from createInstaller import createInstaller, createModuleInstaller
from fileTypeFinder import fileTypes
from createVar import createVar

maxBackupsallowed = 5
def Logging() -> None:
    needLogging = []
    if os.path.isdir("Loggers"):
        pass
    else:
        os.mkdir("Loggers")
        needLogging.append("Loggers folder created.")
    if os.path.isfile("Loggers/logger.log"):
        pass
    else:
        with open("Loggers/logger.log", "w") as openedFile:
            openedFile.write("")
        needLogging.append("'logger.log' file created.") 
    if os.path.isfile("Loggers/onetimelogger.log"):
        pass
    else:
        with open("Loggers/onetimelogger.log", "w") as openedFile:
            openedFile.write("")
        needLogging.append("'onetimelogger.log' file created.")
    if os.path.isdir("Loggers/backups"):
        pass
    else:
        os.mkdir("Loggers/backups")
        needLogging.append("Loggers/backups folder created.")
    loggerHandler = logging.FileHandler("Loggers/logger.log")
    oneTimeHandler = logging.FileHandler("Loggers/onetimelogger.log", "w")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s : %(asctime)s - {%(message)s} from %(pathname)s on line %(lineno)d',
        datefmt='%d-%b-%y %H:%M:%S',
        handlers=[loggerHandler, oneTimeHandler]
    )
    [logging.debug(debugMessage) for debugMessage in needLogging]
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
    if len(os.listdir("Loggers/backups")) == maxBackupsallowed:
        shutil.rmtree("Loggers/backups")

Logging()
del Logging, maxBackupsallowed
@logC()
def pycacheDel(foldersToCheck: Optional[dict] = None) -> None:
    if not checkPara(foldersToCheck, None):
        for path, typeOfFille in foldersToCheck.items():
            if typeOfFille == "file":
                continue
            elif type(typeOfFille) == dict:
                if createVar(path, ["/", "\\"], "/").split("/")[-1] == "__pycache__":
                    shutil.rmtree(path)
                    Print(f"{RED}{path} deleted{RESET}")
                else:
                    pycacheDel(typeOfFille)
    else:
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
del pycacheDel, overload, Optional, Any, os, sys
logging.info(f"NTSModule imported successfully.")
clear()
Print(f"Module {GREEN}NTSModule{RESET} has been successfully imported!\nEnjoy!")
