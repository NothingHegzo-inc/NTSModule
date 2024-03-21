import sys, os, logging
sys.path.append(os.path.dirname(__file__))
from imports import Optional, Any, overload, logC
from errorClasses import *

@overload
def checkPara(parameter: Any, correctType: type) -> bool : ...
@overload
def checkPara(listOfParameters: list[Any], listOfTypes: list[type]) -> bool : ...
@overload
def checkPara(dictOfParams: dict[Any, type]) -> bool : ...
@logC()
def checkPara(
    parameter: Optional[Any] = None,
    correctType: type = None,
    listOfParameters: Optional[list[Any]] = None,
    listOfTypes: Optional[list[type]] = None,
    dictOfParams: Optional[dict[Any, type]] = None
) -> bool:
    if (
        (parameter is not None and listOfParameters is not None)
        or
        (parameter is not None and dictOfParams is not None)
        or
        (listOfParameters is not None and dictOfParams is not None)
    ):
        logging.error(f"{IncompatableArgsError.__name__}")
        raise IncompatableArgsError(f"Incompatable arguments given.")
    if parameter is None and listOfParameters is None and dictOfParams is None:
        logging.error(f"{TypeError.__name__}")
        raise TypeError(f"{YELLOW}{checkPara.__name__}{WHITE}(){RESET} did not get any correct arguments.")
    elif (listOfParameters is not None and listOfTypes is None) or (listOfParameters is None and listOfTypes is not None):
        logging.error(f"{IncompatableArgsError.__name__}")
        raise IncompatableArgsError(f"Arguments '{CYAN}listOfParameters{RESET}' and '{CYAN}listOfTypes{RESET}' both need to be given at the same time not one a time.")
    elif (parameter is None and correctType is not None) or (parameter is not None and correctType is None):
        logging.error(f"{IncompatableArgsError.__name__}")
        raise IncompatableArgsError(f"Arguments '{CYAN}parameter{RESET}' and '{CYAN}correctType{RESET}' both need to be given at the same time not one a time.")
    elif (listOfParameters is not None and listOfTypes is not None) and (checkPara(listOfTypes, list) is False or checkPara(listOfParameters, list) is False):
        logging.error(f"{TypeError.__name__}")
        raise TypeError(f"Arguments '{CYAN}listOfParameters{RESET}' or/and '{CYAN}listOfTypes{RESET}' need to be type {DGREEN}list{RESET}.")
    elif dictOfParams is not None and checkPara(dictOfParams, dict) is False:
        logging.error(f"{TypeError.__name__}")
        raise TypeError(f"Arguments '{CYAN}dictOfParams{RESET}' has to be type {DGREEN}dict{RESET} not type {DGREEN}{type(dictOfParams).__name__}{RESET}.")
    elif listOfParameters is not None and listOfTypes is not None and len(listOfTypes) != len(listOfParameters):
        logging.error(f"{IncorrectArgsError.__name__}")
        raise IncorrectArgsError(f"Arguments '{CYAN}listOfParameters{RESET}' and '{CYAN}listOfTypes{RESET}' need to have the same amount of variables.")
    if parameter is not None:
        if type(parameter) is correctType:
            return True
        else:
            return False
    elif listOfParameters is not None:
        returnBool: bool
        for x in [True if type(para) is listOfTypes[num] else False for num, para in enumerate(listOfParameters)]:
            if x is True:
                returnBool = True
            else:
                returnBool = False
                break
        return returnBool
    elif dictOfParams is not None:
        returnBool: bool
        for para, typeOfPara in dictOfParams.items():
            if type(para) is typeOfPara:
                returnBool = True
            else:
                returnBool = False
                break
        return returnBool
            
            


if __name__ == '__main__':
    ...
    