import sys
import os
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(f"{appendingSys}")

from variables import *
from getFileLines import getFileLines
from clear import clear
from Print import Print
from invalidOption import invalidOption
from question import question
from errorClasses import *

clear()
Print(f"Module {GREEN}NTSModule{RESET} has been successfully imported!\nEnjoy!")

del sys