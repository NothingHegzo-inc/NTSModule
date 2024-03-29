import os, sys
sys.path.append(os.path.dirname(__file__))
from imports import *
from Print import Print
from clear import clear
from invalidOption import invalidOption
import logging

@overload
def getFileLines(filePath: str) -> list[str]: ...
@overload
def getFileLines(filePath: str, mode: str) -> str: ...
@overload
def getFileLines(filePath: str, mode:str, lineNum: int) -> str: ...
#@logC()
def getFileLines(
        filePath: str,
        mode: str = "r",
        lineNum: Optional[int] = None
) -> list[str] | str:
    try:
        with open(filePath, mode) as openedFile:
            readlines = openedFile.readlines()
        
        readlinesSplit = [line.split("\n")[0] if line[-1] == "\n" else line for line in readlines][lineNum if type(lineNum) is int else 0:len([line.split("\n")[0] if line[-1] == "\n" else line for line in readlines])]
        if lineNum is None:
            return readlinesSplit
        elif lineNum is not None:
            if not checkPara(lineNum, int):
                raise IncorrectTypesError(arguments="line", argumentTypes=int)#TypeError(f"Variable '{CYAN}line{RESET}' type has to be {DGREEN}int{RESET} not {DGREEN}{type(lineNum).__name__}{RESET}.")
            elif checkPara(lineNum, int):
                if lineNum > len(readlinesSplit) or lineNum < -1 * len(readlinesSplit):
                    logging.error(f"{IndexError.__name__}")
                    raise IndexError(f"Variable '{CYAN}lineNum{RESET}' is higher than the maximum number of lines in the file.")
                return readlinesSplit[lineNum]
    except FileNotFoundError:
        raise IncorrectFilePathError(path=filePath)



if __name__ == '__main__':
    print(getFileLines(".asd"))
        