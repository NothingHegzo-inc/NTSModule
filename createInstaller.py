import os, sys, logging
sys.path.append(os.path.dirname(__file__))
from getFileLines import getFileLines
from Print import Print
from imports import *
from io import TextIOWrapper
from functools import cache

failed = []
installerLogger = logging.Logger("installerLogger", logging.DEBUG)
installerHandler = logging.FileHandler("NTSModule/Loggers/installerLogger.log" , "w")
installerHandler.setLevel(logging.DEBUG)
installerHandler.setFormatter(logging.Formatter('%(levelname)s : %(asctime)s - {%(message)s} from %(pathname)s on line %(lineno)d', '%d-%b-%y %H:%M:%S'))
installerLogger.addHandler(installerHandler)
Print = cache(Print)

@overload
def folderDict(Path: filePath) -> dict: None
@overload
def folderDict(Path: filePath, excludedFiles_Folder: list[filePath]) -> dict: None
@logC(installerLogger)
def folderDict(
        Path: filePath, 
        excludedFiles_Folder: Optional[list[filePath]] = None
) -> dict:
    FPathDict = {}
    try:
        for fileORfolder in os.listdir(Path):
            if not checkPara(excludedFiles_Folder, None) and f"{Path}/{fileORfolder}" in excludedFiles_Folder:
                continue
            elif os.path.isfile(f"{Path}/{fileORfolder}"):
                try:
                    FPathDict[fileORfolder] = getFileLines(f"{Path}/{fileORfolder}", "rb")
                except Exception as e:
                    failed.append(f"{Path}/{fileORfolder} due to Error: {e}")
            elif os.path.isdir(f"{Path}/{fileORfolder}"):
                if fileORfolder[0] == "." or fileORfolder == "Logger":
                    continue
                FPathDict[fileORfolder] = folderDict(f"{Path}/{fileORfolder}", excludedFiles_Folder)
        Print(f"{GREEN}folderDict created for {Path}{RESET}")
    except Exception as e:
        failed.append(Path)
        Print(f"{RED}failed to create folderDict for {Path} due to Error: {e}{RESET}")
    return FPathDict

@overload
def folderLines(Path: filePath) -> dict: None
@overload
def folderLines(Path: filePath, excludedFiles_Folder: list[filePath]) -> list[str]: None
@logC(installerLogger)
def folderLines(
        Path: filePath, 
        excludedFiles_Folder: Optional[list[filePath]] = None
) -> list[str]:
    # Print(Path)
    Fpaths: dict = folderDict(Path, excludedFiles_Folder)
    lines: list = []
    for file, info in Fpaths.items():
        info: dict
        if not checkPara(info, dict):
            continue
        lines.append([f"\n    if not os.path.isdir('{Path}/{file}'):    os.mkdir('{Path}/{file}')"])
        Print(f"{GREEN}lines created for {Path}/{file}{RESET}")
        for fileIn, infoIn in info.items():
            if checkPara(infoIn, list):
                fileVar = createVar(f"{Path}/{file}/{fileIn}", creatingInstallerVar=True)
                lines.append([f"\n    with open('{Path}/{file}/{fileIn}', 'wb') as {fileVar}:    {fileVar}.writelines({infoIn})"])
                Print(f"{GREEN}lines created for {Path}/{file}/{fileIn}{RESET}")
            elif checkPara(infoIn, dict):
                #lines.append([f"\n    if not os.path.isdir('{Path}/{file}/{fileIn}'):    os.mkdir('{Path}/{file}/{fileIn}')"])
                for x in folderLines(f"{Path}/{file}", excludedFiles_Folder):
                    lines.append(x)
    Print(f"{GREEN}lines created for {Path}/{file}{RESET}")
    return lines

CreatesInstaller = TextIOWrapper
@overload
def createInstaller(Path: filePath) -> CreatesInstaller: None
@overload
def createInstaller(Path: filePath, excludedFiles_Folder: list[filePath]) -> CreatesInstaller: None
@overload
def createInstaller(Path: filePath, excludedFiles_Folder: list[filePath], newFileName: str | filePath) -> CreatesInstaller: None
@logC(installerLogger)
def createInstaller(
        Path: filePath, 
        excludedFiles_Folder: Optional[list[filePath]] = [],
        newFileName: Optional[str | filePath] = None
) -> CreatesInstaller:
    """NOTE: Adding the full path of the folder/file will mess up with th functionality of this function and will 100% mess with your files, so it is recommended
     to add this module into the folder and call the folder using 1-3 /s\n
     NOTE: Folders starting with '.' will not be read as it will be considered private."""
    excludedFiles_Folder.append(f"{os.path.dirname(os.path.dirname(__file__))}/installer.py")
    excludedFiles_Folder.append(f"{os.path.dirname(os.path.dirname(__file__))}/NTSModuleInstaller.py")
    if newFileName == None:
        newFileName = "installer.py"
    else:
        try:
            if newFileName[-3:] != ".py":
                newFileName+=".py"   
        except:
            newFileName+=".py"
    foldersIn = createVar(newFileName, ["/","\\"],"/").split("/") 
    for n, folder in enumerate(foldersIn):
        if folder[-3:] == ".py":
            continue
        elif n == 0:
            if not os.path.isdir(f"{folder}"): os.mkdir(f"{folder}")
        elif n == len(foldersIn):
            if not os.path.isdir(f"{'/'.join(foldersIn[:n])}"): os.mkdir(f"{'/'.join(foldersIn[:n])}")
        else:
            if not os.path.isdir(f"{'/'.join(foldersIn[:n+1])}"): os.mkdir(f"{'/'.join(foldersIn[:n+1])}")
    excludedFiles_Folder.append(newFileName)
    defExcluded = list(excludedFiles_Folder)
    for excludedPath in defExcluded:
        foldersIn = createVar(excludedPath, ["/","\\"],"/").split("/")
        for n, folder in enumerate(foldersIn):
            filePathToExclude = '/'.join(foldersIn[-(n+1):])
            if n == 0 or filePathToExclude in excludedFiles_Folder:
                continue
            excludedFiles_Folder.append(filePathToExclude)
            if createVar(filePathToExclude, ["/","\\"], "/").split("/")[-1] not in ["installer.py", "NTSModuleInstaller.py", newFileName]:
                Print(f"{YELLOW}Added {'/'.join(foldersIn[-(n+1):])} to excluded folders and files.{RESET}")
    Fpaths = ""
    if not os.path.isdir(Path) and not os.path.isdir(os.path.dirname(os.path.dirname(__file__))+"/"+Path) and not os.path.isfile(Path):
        raise IncorrectFilePathError(path=Path)
    if Path[-1] in ["/", "\\"]:
            Path = Path[:-1]
    # Path = Path.split("/")[-1]
    lines: list = []
    if os.path.isdir(Path):
        lines.append(["import os, sys, logging\n","\n                                     ",f"\ntry:"])
        foldersIn = createVar(Path, ["/","\\"],"/").split("/")
        for n, folder in enumerate(foldersIn):
            if n == 0:
                lines.append(f"\n    if not os.path.isdir('{folder}'):    os.mkdir('{folder}')")
                Print(f"{GREEN}lines created for {folder}{RESET}")
            elif n == len(foldersIn):
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n])}'):    os.mkdir('{'/'.join(foldersIn[:n])}')")
                Print(f"{GREEN}lines created for {'/'.join(foldersIn[:n])}{RESET}")
            else:
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n+1])}'):    os.mkdir('{'/'.join(foldersIn[:n+1])}')")
                Print(f"{GREEN}lines created for {'/'.join(foldersIn[:n+1])}{RESET}")
        Fpaths: dict = folderDict(Path, excludedFiles_Folder)
        for file, info in Fpaths.items():
            fileVar = createVar(f"{Path}/{file}", creatingInstallerVar=True)
            if checkPara(info, dict):
                for x in folderLines(Path, excludedFiles_Folder):
                    lines.append(x)
            elif checkPara(info, list):
                if file == "installer.py":
                    continue
                else:
                    lines.append([f"\n    with open('{Path}/{file}', 'wb') as {fileVar}:    {fileVar}.writelines({info})"])
                    Print(f"{GREEN}lines created for {Path}/{file}{RESET}")
    elif os.path.isfile(Path):
        lines.append(["import os, sys, logging\n","\n                                     ",f"\ntry:"])
        foldersIn = createVar(Path, ["/","\\"],"/").split("/")[:-1]
        for n, folder in enumerate(foldersIn):
            if n == 0:
                lines.append(f"\n    if not os.path.isdir('{folder}'):    os.mkdir('{folder}')")
                Print(f"{GREEN}lines created for {folder}{RESET}")
            elif n == len(foldersIn):
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n])}'):    os.mkdir('{'/'.join(foldersIn[:n])}')")
                Print(f"{GREEN}lines created for {'/'.join(foldersIn[:n])}{RESET}")
            else:
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n+1])}'):    os.mkdir('{'/'.join(foldersIn[:n+1])}')")
                Print(f"{GREEN}lines created for {'/'.join(foldersIn[:n+1])}{RESET}")
        lines.append([f"\n    if not os.path.isfile('{Path}'):\n        with open('{Path}', 'w'): ..."])
        fileVar = createVar(Path, creatingInstallerVar=True)
        lines.append(f"\n    with open('{Path}','wb') as {fileVar}: {fileVar}.writelines({{}})".format(getFileLines(Path, "rb")))
        Print(f"{GREEN}lines created for {fileVar}{RESET}")
    lines.append("\n    print('Successfully created files and folders!')\nexcept WindowsError as e:\n    print('Please run this file in a python runner, something like IDLE or VisualStudio.')\n    print(f'Actual error: {e}')\n    input()")
    newLines = []
    for line in lines:
        if line in newLines:
            continue
        else:
            newLines.append(line)
    lines = newLines
    Print(f"{YELLOW}Creating file {BLACK}{newFileName}{RESET}.")
    try:
        with open(newFileName, "w") as installerWrite, open(newFileName, "r+") as installerAppend:
            installerWrite.writelines([""])
            for line in lines:
                installerAppend.writelines(line)
        Print(f"{GREEN}Successfully created file {BLACK}{newFileName}{RESET}, failed files/folders: {RED}{failed}{RESET}.")
    except Exception as excep:
        Print(f"{RED} Failed to create file {BLACK}{newFileName}{RED}, this message is not supposed to ever display and if it is displayed a new file called {BLACK}crashReport.log{RED} must've been created, if you are in contact with the owner of this module, please do send him the logs.{RESET}\n{YELLOW}If you would like to see the error, it should be in {os.path.abspath('crashReport.log')} line 1{RESET}")
        if os.path.isfile("crashReport.log"):
            with open("crashReport.log", "w") as crashFile:
                crashFile.write("")
        crashReport = logging.getLogger()
        crashReport.addHandler(logging.FileHandler("crashReport.log"))
        crashReport.setLevel(logging.DEBUG)
        crashReport.critical(excep)
        crashReport.critical(newFileName)
        crashReport.critical(Path)
        crashReport.critical(lines)
    return Fpaths if Fpaths != "" else {f'{Path}' : lines}

@overload
def createModuleInstaller() -> CreatesInstaller: ...
@overload
def createModuleInstaller(newFileName: str | filePath) -> CreatesInstaller: ...
@logC(installerLogger)
def createModuleInstaller(newFileName: str | filePath = "NTSModuleInstaller") -> CreatesInstaller:
    """Creates this module's installer in a file named 'NTSModuleInstaller.py'"""
    return createInstaller("NTSModule", ["NTSModule/__pycache__", "NTSModule/pygameNTS/__pycache__","NTSModule/pygameNTS/ButtonClasses/__pycache__", "NTSModule/Loggers", "NTSModule/Loggers/logger.log", "NTSModule/Loggers/onetimelogger.log", "NTSModule/Loggers/backups", "NTSModule/Loggers/installerLogger.log"], newFileName)

if __name__ == '__main__':
    ...