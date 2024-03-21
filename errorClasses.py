import logging, os, sys
sys.path.append(os.path.dirname(__file__))
from variables import *
from imports import Optional, overload
class IncorrectFilePathError(Exception):
    def __init__(self, filePath: str) -> None:
        super().__init__(f"File path {RED}{filePath}{RESET} not found, please make sure it's the correct file path.")
        logging.error(f"{IncorrectFilePathError.__name__} error called for file path: '{filePath}'")
class PositionalArgError(Exception): ...
class IncompatableArgsError(Exception):
    def __init__(self, *message, firstArg: Optional[str] = None, secondArg: Optional[str] = None):
        if firstArg is not None and secondArg is not None:
            super().__init__(f"Arguments '{CYAN}{firstArg}{RESET}' and '{CYAN}{secondArg}{RESET}' are not compatable arguments.")
        else:
            super().__init__(*message)
class IncorrectArgsError(Exception): ...
class UnknownVars(Exception):
    def __init__(self, *message, arguments: Optional[str] = None):
        if arguments is not None:
            message = f"Variable{f' {CYAN}' if arguments[0] != 's' else f's {CYAN}'}{arguments if arguments[0] != 's' else arguments[1:]}{RESET} are unknown."
            if type(arguments) is not list and type(arguments) is not str:
                raise IncorrectArgsError(arguments)
        super().__init__(*message if type(message) is tuple else message)
class CannotOverride(Exception): ...
class UnknownError(Exception): ...