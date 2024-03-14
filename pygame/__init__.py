import sys, os
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(f"{appendingSys}")
del appendingSys
import pygame

from ButtonClasses.Button import Button
from pygFuncs import hoverColorFunc, variables
from pygVariables import *
from Base import Base
from ButtonClasses.StripC import StripC
from ButtonClasses.ButtonImage import ButtonImage
from ButtonClasses.ButtonAnim import ButtonAnim