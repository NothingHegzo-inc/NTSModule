import logging, os, sys
sys.path.append(os.path.dirname(__file__))
from variables import *
from imports import Optional, overload

class PositionalArgError(Exception):
    def __init__(self, *args: object) -> None:
        logging.error(f"{self.__class__.__name__}.")
        super().__init__(*args)
class IncompatableArgsError(Exception):
    @overload
    def __init__(self, *text) -> None: ...
    @overload
    def __init__(self, argumentNames: list[nameOfArg]) -> None: ...
    def __init__(self, *text, argumentNames: Optional[list[nameOfArg]] = None) -> None:
        try:
            text[0]
            super().__init__(*text)
        except:
            if type(argumentNames) is not list:
                raise TypeError(f"Argument '{CYAN}argumentNames{RESET}' has to be type {DGREEN}list{RESET} not type {DGREEN}{type(argumentNames).__name__}{RESET}.")
            elif type(argumentNames) is list:
                lastArg = argumentNames[len(argumentNames)-1]
                argsBefore = argumentNames[:(len(argumentNames)-1):]
                if len(argsBefore) == 1:
                    super().__init__(f"Arguments '{CYAN}{argumentNames[0]}{RESET}' and '{CYAN}{argumentNames[1]}{RESET}' are incompatable.")
                else:
                    argsBefore = "".join([f"'{CYAN}{x}{RESET}', " for x in argsBefore])
                    super().__init__(f"Arguments {argsBefore}and/or '{CYAN}{lastArg}{RESET}' are incompatable.")
        logging.error(f"{self.__class__.__name__}, Arguments: '{argumentNames}', or '{text}'")
class UnknownVars(Exception):
    @overload
    def __init__(self, *text) -> None: ...
    @overload
    def __init__(self, variables: nameOfArg) -> None: ...
    @overload
    def __init__(self, variables: list[nameOfArg]) -> None: ...
    def __init__(self, *text, variables: Optional[nameOfArg | list[nameOfArg]] = None) -> None:
        try:
            text[0]
            super().__init__(*text)
        except:
            if type(variables) not in [str, list]:
                raise TypeError(f"Argument '{CYAN}variables{RESET}' has to be type {DGREEN}str{RESET} or type {DGREEN}list{RESET} not type {DGREEN}{type(variables).__name__}{RESET}.")
            elif type(variables) is str:
                super().__init__(f"Variable '{CYAN}{variables}{RESET}' was not specified.")
            elif type(variables) is list:
                lastArg = variables[len(variables)-1]
                argsBefore = variables[:(len(variables)-1):]
                if len(argsBefore) == 1:
                    super().__init__(f"Variables '{CYAN}{variables[0]}{RESET}' and/or '{CYAN}{variables[1]}{RESET}' were not specified.")
                else:
                    argsBefore = "".join([f"'{CYAN}{x}{RESET}', " for x in argsBefore])
                    super().__init__(f"Variables {argsBefore}and/or '{CYAN}{lastArg}{RESET}' were not specified.")
        logging.error(f"{self.__class__.__name__}, Variables: '{variables}', or '{text}'")
class CannotOverwrite(Exception):
    def __init__(self, argument: nameOfArg) -> None:
        if type(argument) is not str:
            raise TypeError(f"Argument '{CYAN}argument{RESET}' has to be type {DGREEN}str{RESET} not type {DGREEN}{type(argument).__name__}{RESET}.")
        super().__init__(f"Argument '{CYAN}{argument}{RESET}' cannot be overwritten.")
class IncorrectFilePathError(Exception):
    @overload
    def __init__(self, *text) -> None: ...
    @overload
    def __init__(self, path: str) -> None: ...
    def __init__(self, *text, path: Optional[str] = None) -> None:
        try:
            text[0]
            super().__init__(*text)
        except:
            if type(path) is not str:
                raise TypeError(f"Type '{CYAN}path{RESET}' has to be type {DGREEN}str{RESET} not type {DGREEN}{type(path).__name__}{RESET}.")
            super().__init__(f"Path '{RED}{path}{RESET}' was not found or is incorrect.")
        logging.error(f"{self.__class__.__name__}, Path: '{path}', or '{text}'")
class IncorrectArgsError(Exception):
    @overload
    def __init__(self, *text) -> None: ...
    @overload
    def __init__(self, argumentNames: nameOfArg) -> None: ...
    @overload
    def __init__(self, argumentNames: list[nameOfArg]) -> None: ...
    def __init__(self, *text, argumentNames: Optional[nameOfArg | list[nameOfArg]] = None) -> None:
        try:
            text[0]
            super().__init__(*text)
        except:
            if type(argumentNames) not in [str, list]:
                raise TypeError(f"Argument '{CYAN}argumentNames{RESET}' has to be type {DGREEN}str{RESET} or type {DGREEN}list{RESET} not type {DGREEN}{type(argumentNames).__name__}{RESET}.")
            elif type(argumentNames) is str:
                super().__init__(f"Argument '{CYAN}{argumentNames}{RESET}' is incorrect.")
            elif type(argumentNames) is list:
                lastArg = argumentNames[len(argumentNames)-1]
                argsBefore = argumentNames[:(len(argumentNames)-1):]
                if len(argsBefore) == 1:
                    super().__init__(f"Arguments '{CYAN}{argumentNames[0]}{RESET}' and '{CYAN}{argumentNames[1]}{RESET}' are incorrect.")
                else:
                    argsBefore = "".join([f"'{CYAN}{x}{RESET}', " for x in argsBefore])
                    super().__init__(f"Arguments {argsBefore}and '{CYAN}{lastArg}{RESET}' are incorrect.")
        logging.error(f"{self.__class__.__name__}, Arguments: '{argumentNames}', or '{text}'")
class IncorrectTypesError(Exception):
    @overload
    def __init__(self, *text) -> None: ...
    @overload
    def __init__(self, arguments: nameOfArg, argumentTypes: type) -> None: ...
    @overload
    def __init__(self, arguments: nameOfArg, argumentTypes: list[type]) -> None: ...
    @overload
    def __init__(self, arguments: list[nameOfArg], argumentTypes: list[type]) -> None: ...
    def __init__(
        self, 
        *text, 
        arguments: Optional[nameOfArg | list[nameOfArg]] = None, 
        argumentTypes: Optional[type | list[type]] = None
    ) -> None:
        try:
            text[0]
            super().__init__(*text)
        except:
            if type(arguments) not in [str, list]:
                raise TypeError(f"Argument '{CYAN}arguments{RESET}' has to be type {DGREEN}str{RESET} or type {DGREEN}list{RESET} not type {DGREEN}{type(arguments).__name__}{RESET}.")
            elif type(arguments) is list and type(argumentTypes) is not list:
                raise TypeError(f"If argument '{CYAN}arguments{RESET}' is type {DGREEN}list{RESET} then argument '{CYAN}argumentTypes{RESET}' has to be type {DGREEN}list{RESET} not type {DGREEN}{type(argumentTypes).__name__}{RESET}.")
            elif type(arguments) is str and type(argumentTypes) is list:
                if None in argumentTypes:
                    argumentTypes.pop(argumentTypes.index(None))
                    argumentTypes.append(type(None))
                lastType = argumentTypes[len(argumentTypes)-1]
                typesBefore = argumentTypes[:len(argumentTypes)-1:]
                if len(typesBefore) == 1:
                    super().__init__(f"Argument '{CYAN}{arguments}{RESET}' has to be type {DGREEN}{argumentTypes[0].__name__}{RESET} or type {DGREEN}{argumentTypes[1].__name__}{RESET}.")
                else:
                    typesBefore = "".join([f"{DGREEN}{x.__name__}{RESET}, " for x in typesBefore])
                    super().__init__(f"Argumen '{CYAN}{arguments}{RESET}' has to be type {typesBefore}or type {DGREEN}{lastType.__name__}{RESET}.")
            elif (type(arguments) is list and type(argumentTypes) is list) and len(arguments) != len(argumentTypes):
                raise TypeError(f"Arguments '{CYAN}arguments{RESET}' and '{CYAN}argumentTypes{RESET}' have to have the same amount of variables.")
            elif type(arguments) is list and type(argumentTypes) is list:
                newDict = {}
                for n, arg in enumerate(arguments):
                    newDict[arg] = argumentTypes[n]
                message = f""
                for parameter, typeOfPara in newDict.items():
                    if typeOfPara is None:
                        typeOfPara = type(typeOfPara)
                    message+=f"'{CYAN}{parameter}{RESET}' : {DGREEN}{typeOfPara.__name__}{RESET}\n"
                super().__init__(f"Some argument types were incorrect, the argument's types should be as follows.\n{YELLOW}Legend{RESET} - '{CYAN}Argument{RESET}' : {DGREEN}Type{RESET}\n{message.strip()}")
            elif type(arguments) is str:
                if argumentTypes is None:
                    argumentTypes = type(argumentTypes)
                super().__init__(f"Argument '{CYAN}{arguments}{RESET}' has to be type {DGREEN}{argumentTypes.__name__}{RESET}.")
        logging.error(f'{self.__class__.__name__}, Arguments: "{arguments}","{argumentTypes}" or "{text}"')
class UnknownError(Exception):
    @overload
    def __init__(self, *text) -> None: ...
    @overload
    def __init__(self, functionName: function) -> None: ...
    def __init__(self, *text, functionName: function) -> None:
        def nothing(): ...
        try:
            text[0]
            super().__init__(*text)
        except:
            if type(functionName) is not type(nothing):
                raise TypeError(f"Argument '{CYAN}functionName{RESET}' has to be type {DGREEN}{type(nothing).__name__}{RESET}.")
            elif type(functionName) is type(nothing):
                super().__init__(f"This error was called by function {YELLOW}{functionName.__qualname__}{WHITE}(){RESET}.")
        logging.error(f"{self.__class__.__name__}")

if __name__ == '__main__':
    ...
   
    