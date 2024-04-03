import os, sys, logging
sys.path.append(os.path.dirname(__file__))
from getFileLines import getFileLines
from Print import Print
from clear import clear
from imports import *
from io import TextIOWrapper
from functools import cache, wraps

#createVar = lambda path: "_".join(("_".join(os.path.splitext(path)[0].split("/"))).split("-"))#"_".join(os.path.splitext(file)[0].split(" "))
failed = []

Print = cache(Print)


@overload
def folderDict(Path: filePath) -> dict: None
@overload
def folderDict(Path: filePath, excludedFiles_Folder: list[filePath]) -> dict: None
def folderDict(
        Path: filePath, 
        excludedFiles_Folder: Optional[list[filePath]] = None
) -> dict:
    FPathDict = {}
    try:
        for fileORfolder in os.listdir(Path):
            if not checkPara(excludedFiles_Folder, None) and Path+"/"+fileORfolder in excludedFiles_Folder:
                continue
            elif os.path.isfile(Path+"/"+fileORfolder):
                try:
                    FPathDict[fileORfolder] = getFileLines(Path+"/"+fileORfolder, "rb")
                except Exception as e:
                    failed.append(f"{Path}/{fileORfolder} due to Error: {e}")
            elif os.path.isdir(Path+"/"+fileORfolder):
                if fileORfolder[0] == "." or fileORfolder == "Logger":
                    continue
                FPathDict[fileORfolder] = folderDict(Path+"/"+fileORfolder, excludedFiles_Folder)
        Print(f"{GREEN}folderDict created for {Path}{RESET}")
    except Exception as e:
        failed.append(Path)
        Print(f"{RED}failed to create folderDict for {Path} due to Error: {e}{RESET}")
    return FPathDict

@overload
def folderLines(Path: filePath) -> dict: None
@overload
def folderLines(Path: filePath, excludedFiles_Folder: list[filePath]) -> list[str]: None
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
        for fileIn, infoIn in info.items():
            if checkPara(infoIn, list):
                fileVar = createVar(f"{Path}/{file}/{fileIn}", creatingInstallerVar=True)
                lines.append([f"\n    with open('{Path}/{file}/{fileIn}', 'wb') as {fileVar}:    {fileVar}.writelines({infoIn})"])
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
def createInstaller(Path: filePath, excludedFiles_Folder: list[filePath], newFileName: str) -> CreatesInstaller: None
def createInstaller(
        Path: filePath, 
        excludedFiles_Folder: Optional[list[filePath]] = [],
        newFileName: Optional[str] = None
) -> CreatesInstaller:
    """NOTE: Adding the full path of the folder/file will mess up with th functionality of this function and will 100% mess with your files, so it is recommended
     to add this module into the folder and call the folder using 1-3 /s\n
     NOTE: Folders starting with '.' will not be read as it will be considered private.""" 
    excludedFiles_Folder.append("installer.py")
    if newFileName == None:
        newFileName = "installer.py"
    else:
        try:
            if newFileName[-3:] == ".py":
                ...
            else:
                newFileName+=".py"
        except:
            newFileName+=".py"
    excludedFiles_Folder.append(newFileName)
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
            elif n == len(foldersIn):
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n])}'):    os.mkdir('{'/'.join(foldersIn[:n])}')")
            else:
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n+1])}'):    os.mkdir('{'/'.join(foldersIn[:n+1])}')")
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
    elif os.path.isfile(Path):
        lines.append(["import os, sys, logging\n","\n                                     ",f"\ntry:"])
        foldersIn = createVar(Path, ["/","\\"],"/").split("/")[:-1]
        for n, folder in enumerate(foldersIn):
            if n == 0:
                lines.append(f"\n    if not os.path.isdir('{folder}'):    os.mkdir('{folder}')")
            elif n == len(foldersIn):
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n])}'):    os.mkdir('{'/'.join(foldersIn[:n])}')")
            else:
                lines.append(f"\n    if not os.path.isdir('{'/'.join(foldersIn[:n+1])}'):    os.mkdir('{'/'.join(foldersIn[:n+1])}')")
        lines.append([f"\n    if not os.path.isfile('{Path}'):\n        with open('{Path}', 'w'): ..."])
        fileVar = createVar(Path, creatingInstallerVar=True)
        lines.append(f"\n    with open('{Path}','wb') as {fileVar}: {fileVar}.writelines({{}})".format(getFileLines(Path, "rb")))
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

def createModuleInstaller() -> CreatesInstaller:
    """Creates this module's installer in a file named 'NTSModuleInstaller.'"""
    return createInstaller("NTSModule", ["NTSModule/__pycache__", "NTSModule/pygameNTS/__pycache__","NTSModule/pygameNTS/ButtonClasses/__pycache__"], "NTSModuleInstaller")

if __name__ == '__main__':
    createInstaller("C:/Program Files/Norton Security")
