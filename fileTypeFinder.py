import os, sys, logging
sys.path.append(os.path.dirname(__file__))
from getFileLines import getFileLines
from Print import Print
from clear import clear
from imports import *
from io import TextIOWrapper
from functools import cache, wraps

fileType = str
file = str
status = str | bool
@overload
def fileTypes(Path: filePath) -> dict[file , fileType] | dict[file, status]: """"""
@overload
def fileTypes(Path: filePath, subFolders: bool) -> dict[file , fileType] | dict[file, status]: """Finds the files and folders inside the subFolders inside the folder given. By default this is set to False."""

def fileTypes(Path: filePath, subFolders: bool = False) -> dict[file , fileType] | dict[file, status]:
    if Path[-1] in ["/", "\\"," "]:
        Path = createVar("/".join(createVar(Path, ["/","\\"], "/").split("/")[:-1]), [" ", ""], delete=True)
    try:
        if not os.path.exists(Path):
            raise IncorrectFilePathError(path=Path)
        if os.path.isfile(Path) and subFolders:
            raise IncompatableArgsError(argumentNames=["Path as file", "subFolders"])
        elif os.path.isfile(Path):
            return {f"{Path}" : "file"}
        else:
            fileTypesDict = {}
            fileTypesDictPath = {}
            for file in os.listdir(Path):
                if file[0] == ".":
                    continue
                if os.path.isfile(f"{Path}/{file}"):
                    fileTypesDict[f"{Path}/{file}"] = "file"
                elif os.path.isdir(f"{Path}/{file}") and subFolders:
                    fileTypesDict[f"{Path}/{file}"] = fileTypes(f"{{}}/{file}".format('/'.join(createVar(Path, ["/","\\"], "/").split('/'))), subFolders)
                elif os.path.isdir(f"{Path}/{file}") and not subFolders:
                    fileTypesDict[f"{Path}/{file}"] = "folder"
            fileTypesDictPath[f"{Path}"] = fileTypesDict
            return fileTypesDictPath
    except:
        try:
            return {f"{Path}/{file}" : "Failed"}
        except:
            try:
                return {f"{Path}" : "Failed"}
            except:
                return {f"Unknown filepath" : "Failed"}

if __name__ == '__main__':
    Print(fileTypes("C:/Users/jwjnt/Desktop/GitLab/NTSModuleWorkingSpace/"))