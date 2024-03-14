import sys, os
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(f"{appendingSys}")
del appendingSys
from typing import Optional, overload, Any
from variables import *
from errorClasses import *
from functools import cache