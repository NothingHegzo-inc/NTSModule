import sys, os
sys.path.append(os.path.dirname(__file__))
from typing import Optional, overload, Any
from variables import *
from errorClasses import *
from functools import cache
from logger import logC
from validationChecker import checkPara
from createVar import createVar