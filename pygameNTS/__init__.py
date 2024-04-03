import sys, os
sys.path.append(os.path.dirname(__file__))
import pygame

from ButtonClasses.Button import Button
from pygFuncs import hoverColorFunc, variables, animationDelay, displayTimer
from pygVariables import *
from Base import Base
from ButtonClasses.StripC import StripC
from ButtonClasses.ButtonImage import ButtonImage
from ButtonClasses.ButtonAnim import ButtonAnim
from inputBox import InputBox
from displayText import DisplayText

def pycacheDel() -> None:
    import shutil
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    if os.path.isdir("NTSModule/__pycache__"):
        shutil.rmtree("NTSModule/__pycache__")
    if os.path.isdir("__pycache__"):
        shutil.rmtree("__pycache__")
    if os.path.isdir("NTSModule/pygameNTS/__pycache__"):
        shutil.rmtree("NTSModule/pygameNTS/__pycache__")
    if os.path.isdir("NTSModule/pygameNTS/ButtonClasses/__pycache__"):
        shutil.rmtree("NTSModule/pygameNTS/ButtonClasses/__pycache__")
    del shutil
pycacheDel()
del pycacheDel