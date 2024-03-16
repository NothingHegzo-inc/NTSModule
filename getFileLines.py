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
def getFileLines(filePath: str, lineNum: int) -> str: ...
def getFileLines(
        filePath: str,
        lineNum: Optional[int] = None
) -> list[str] | str:
    try:
        with open(filePath, "r") as openedFile:
            readlines = openedFile.readlines()
        
        readlinesSplit = []
        for line in readlines:
            try:
                readlinesSplit.append(line.split("\n")[0])
            except:
                readlinesSplit.append(line)
        if lineNum is None:
            return readlinesSplit
        elif lineNum is not None:
            if type(lineNum) is not int:
                logging.error(f"{TypeError.__name__}")
                TypeError(f"Variable '{CYAN}line{RESET}' type has to be {DGREEN}int{RESET} not {DGREEN}{type(lineNum).__name__}{RESET}.")
            elif type(lineNum) is int:
                if lineNum > len(readlinesSplit):
                    logging.error(f"{IndexError.__name__}")
                    raise IndexError(f"Variable '{CYAN}lineNum{RESET}' is higher than the maximum number of lines in the file.")
                elif lineNum < -1 * len(readlinesSplit):
                    logging.error(f"{IndexError.__name__}")
                    raise IndexError(f"Variable '{CYAN}lineNum{RESET}' is higher than the maximum number of lines in the file.")
                return readlinesSplit[lineNum]
    except FileNotFoundError:
        logging.error(f"{IncorrectFilePathError.__name__}")
        raise IncorrectFilePathError(f"File path {GREEN}{filePath}{RESET} not found, please make sure it is the correct file path.")



if __name__ == '__main__':
    print(getFileLines("C:/Users/jwjnt/Desktop/GitLab/NTS_Module2/NTS_Module2/getFileLines.py", 11))
        