import sys, os, logging
sys.path.append(os.path.dirname(__file__))
from imports import Optional, Any, overload, logC
from errorClasses import *


@overload
def checkPara(parameter: Any, correctTypes: type) -> bool : ...
@overload
def checkPara(listOfParameters: list[Any], listOfTypes: list[type]) -> bool : ...
@overload
def checkPara(dictOfParams: dict[Any, type]) -> bool : ...
@logC()
def checkPara(
    parameter: Optional[Any] = ...,
    correctTypes: type = ...,
    listOfParameters: Optional[list[Any]] = ...,
    listOfTypes: Optional[list[type]] = ...,
    dictOfParams: Optional[dict[Any, type]] = ...
) -> bool:
    if (
        (parameter is not ... and listOfParameters is not ...)
        or
        (parameter is not ... and dictOfParams is not ...)
        or
        (listOfParameters is not ... and dictOfParams is not ...)
    ):
        raise IncompatableArgsError([f"parameter", f"listOfParameters", f"dictOfParams"])
    if parameter is ... and listOfParameters is ... and dictOfParams is ...:
        logging.error(f"{TypeError.__name__}")
        raise TypeError(f"{YELLOW}{checkPara.__name__}{WHITE}(){RESET} did not get any correct arguments.")
    elif (listOfParameters is not ... and listOfTypes is ...) or (listOfParameters is ... and listOfTypes is not ...):
        raise IncompatableArgsError(f"Arguments '{CYAN}listOfParameters{RESET}' and '{CYAN}listOfTypes{RESET}' both need to be given at the same time not one a time.")
    elif (parameter is ... and correctTypes is not ...) or (parameter is not ... and correctTypes is ...):
        raise IncompatableArgsError(f"Arguments '{CYAN}parameter{RESET}' and '{CYAN}correctTypes{RESET}' both need to be given at the same time not one a time.")
    elif (listOfParameters is not ... and listOfTypes is not ...) and (checkPara(listOfTypes, list) is False or checkPara(listOfParameters, list) is False):
        raise IncorrectTypesError(arguments=["listOfParameters","listOfTypes"], argumentTypes=[list,list])#raise TypeError(f"Arguments '{CYAN}listOfParameters{RESET}' and/or '{CYAN}listOfTypes{RESET}' need to be type {DGREEN}list{RESET}.")
    elif dictOfParams is not ... and checkPara(dictOfParams, dict) is False:
        raise IncorrectTypesError(arguments="dictOfParams", argumentTypes=dict)
    elif listOfParameters is not ... and listOfTypes is not ... and len(listOfTypes) != len(listOfParameters):
        raise IncorrectArgsError(f"Arguments '{CYAN}listOfParameters{RESET}' and '{CYAN}listOfTypes{RESET}' need to have the same amount of variables.")
    if parameter is not ...:
        if type(correctTypes) is list:
            if None in correctTypes:
                correctTypes.append(type(None))
            return [True if type(parameter) in correctTypes else False][0]
        else:
            if correctTypes == None: correctTypes = type(None)
            return [True if type(parameter) is correctTypes else False][0]
    elif listOfParameters is not ...:
        returnBool: bool
        for x in [True if type(para) == listOfTypes[num] else True if type(para) is type(None) and para in listOfTypes else False for num, para in enumerate(listOfParameters)]:
            if x is True:
                returnBool = True
            else:
                returnBool = False
                break
        return returnBool
    elif dictOfParams is not ...:
        returnBool: bool
        for para, typeOfPara in dictOfParams.items():
            if type(para) is typeOfPara:
                returnBool = True
            elif typeOfPara is None:
                if type(para) is type(typeOfPara):
                    returnBool = True
            else:
                returnBool = False
                break
        return returnBool
            
            


if __name__ == '__main__':
    ...