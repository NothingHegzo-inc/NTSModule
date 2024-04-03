import os, sys, logging
sys.path.append(os.path.dirname(__file__))
from imports import overload, logC, IncorrectArgsError, CYAN, RESET, RED, Optional, checkPara, UnknownVars, IncompatableArgsError



@overload
def createVar(text: str) -> str: """Use the default excluded characters to create the text.\n   The default excluded characters: ["`", "|", "/", "-", "$", "!", '"', "'", "£", "&", "%", "^", "*", "(", ")", "[", "]", "{", "}", ";", ",", "#", ".","@", ":", "<", ">","\\", " "]"""
@overload
def createVar(text: str, excludedCharacters: list) -> str: """Add custom excluded characters, this will override the default."""
@overload
def createVar(text: str, excludedCharacters: list, changeInto: str) -> str: """What to change the excluded character into\nFor example:\n    'C:/drive/path/file'\n      excludedCharacters = [':','/']  changeInto = '_'\n    result = 'C__drive_path_file'"""
@overload
def createVar(text: str, excludedCharacters: list, changeInto: str, creatingInstallerVar: bool) -> str: """This variables was created for the custom function 'fileTypeFinder()', which takes the last 4 paths of a filePath.\nFor example:\n    'C:/drive/parentFolder/subFolder/file' -> 'drive/parentFolder/subFolder/file'"""
@overload
def createVar(text: str, excludedCharacters: list, changeInto: str, delete: bool) -> str: """Instead of changing it into a different string, it completely excludees and deletes the character from the text. By default this is set to False."""

def createVar(
    text: str, 
    excludedCharacters: list = ["`", "|", "/", "-", "$", "!", '"', "'", "£", "&", "%", "^", "*", "(", ")", "[", "]", "{", "}", ";", ",", "#", ".","@", ":", "<", ">","\\", " "], 
    changeInto: Optional[str] = None, 
    creatingInstallerVar: bool = False,
    delete: bool = False
) -> str:
    text = os.path.splitext(text)[0]
    if creatingInstallerVar:
        text = "/".join(createVar(text, ["/", "\\"], "/").split("/")[-4:])
    newPath = ""
    if delete and not checkPara(changeInto, None):
        raise IncompatableArgsError(argumentNames=["delete", "changeInto"])
    elif checkPara(changeInto, None) and creatingInstallerVar and excludedCharacters == ["`", "|", "/", "-", "$", "!", '"', "'", "£", "&", "%", "^", "*", "(", ")", "[", "]", "{", "}", ";", ",", "#", ".","@", ":", "<", ">","\\", " "]:
        changeInto = "_"
    elif checkPara(changeInto, None) and not creatingInstallerVar and not delete:
        raise UnknownVars(variables="changeInto")
    for char in excludedCharacters:
        if len(char) <= 1:
            continue
        else:
            raise IncorrectArgsError(f"Characters in argument '{CYAN}excludedCharacters{RESET}' have to be 1 letter or character not multipled like '{RED}{char}{RESET}'.")
    for letter in text:
        if letter in excludedCharacters and delete:
            continue
        elif letter in excludedCharacters:
            newPath+=changeInto
        else:
            newPath+=letter
    return newPath