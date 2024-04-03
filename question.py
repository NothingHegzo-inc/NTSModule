import os, sys, time, logging
sys.path.append(os.path.dirname(__file__))
from imports import *
from Print import Print
from clear import clear
from invalidOption import invalidOption

@overload
def question(question: str, maxOptions: int) -> int: """Default function, ask a question with a number of options."""
@overload
def question(question: str, extraOptions: list[str] | dict[str , int]) -> int | str: """This will return an int if a dict is used and a str if a list is used."""
@overload
def question(question: str, maxOptions: int, animation: bool) -> int: """Animation using the 'Print' function. By default this is set to False."""
@overload
def question(question: str, maxOptions: int, zeroIsOption: bool) -> int: """Choose if zero is one of the options or not. By default this is set to False."""
@overload
def question(question: str, maxOptions: int, startClear: bool) -> int: """Start the questioning with a 'clear' function. By default this is set to False."""
@overload
def question(question: str, maxOptions: int, extraOptions: list[str] | dict[str , int]) -> int | str: """Either use maxOptions and extraOptions or just extraOption. """
@overload
def question(question: str, maxOptions: int, zeroIsOption: bool, animation: bool, startClear: bool, extraOptions: list[str] | dict[str , int]) -> int | str: """All the arguments for this function in order."""
@overload
def question(question: str, maxOptions: int, zeroIsOption: bool, animation: bool, startClear: bool, extraOptions: list[str] | dict[str , int], **kwargs) -> int | str: """Add any keyword arguments used for a normal print function."""
@logC()
def question(
        question: str,
        maxOptions: Optional[int] = None,
        zeroIsOption: bool = False,
        animation: bool = False,
        startClear: bool = False,
        extraOptions: Optional[list[str] | dict[str , int]] = None,
        strict: bool = True,
        **kwargs
) -> int | str| Any:
    """
    Keyword arguments can be inputed for normal print function.
    Keywords are recommended to be used for this function. Otherwise the sequence of variables is, 
    \nquestion, 
    \nmaxOptions, 
    \nzeroIsOption, 
    \nanimation, 
    \nstartClear, 
    \nextraOptions, 
    \n**kwargs
    \nKwargs are for print function added keyword arguments.
    \nUsing a dict in 'extraOptions' will return the given value you've selected. 
    \nFor example extraOptions={"Test" : 1} if the user types in 'Test', the value returned will be '1'.
    \nVariable 'strict' is a backLog only use, if you understand the code you may use it.
    """
    # Checking correct variables have the correct type
    if extraOptions is not None:
            if not checkPara(extraOptions, [dict, list]):
                raise IncorrectTypesError(arguments="extraOptions", argumentTypes=[list, dict])#raise IncorrectArgsError(f"Variable '{CYAN}extraOptions{RESET}' has to be type {DGREEN}list{PINK}[{DGREEN}str{PINK}]{RESET} or type {DGREEN}dict{PINK}[{DGREEN}str{RESET}, {DGREEN}int{PINK}]{RESET}. {BLACK}(even if there is one option){RESET}")
    if checkPara(maxOptions, None) and (not checkPara(extraOptions, [dict, list])):
        raise UnknownVars(f"If variable '{CYAN}maxOptions{RESET}' is not given, then variable '{CYAN}extraOptions{RESET}' has to be a {DGREEN}list{PINK}[{DGREEN}str{PINK}]{RESET} or {DGREEN}dict{PINK}[{DGREEN}str{RESET}, {DGREEN}int{PINK}]{RESET} not a {RED}{type(extraOptions).__name__}{RESET}.")
    if animation is True and ('end' in kwargs or 'flush' in kwargs):
        raise IncompatableArgsError(f"Variables '{CYAN}end{RESET}' or '{CYAN}flush{RESET}' cannot be given with variable '{CYAN}animation{RESET}' being {BLUE}True{RESET}.")
    if strict:
        if checkPara(extraOptions, list):
            for option in extraOptions:
                if not checkPara(option, str):
                    raise type(f"Options in variable '{CYAN}extraOptions{RESET}' must be type {DGREEN}str{RESET} not {DGREEN}{type(option).__name__}{RESET}.")
                else:
                    continue
        elif checkPara(extraOptions, dict):
            for option, output in extraOptions.items():
                if not checkPara(option, str):
                    raise IncorrectArgsError(f"Keys in dict '{CYAN}extraOptions{RESET}' must be type {DGREEN}str{RESET} not {DGREEN}{type(option).__name__}{RESET}.")
                if not checkPara(output, int):
                    raise IncorrectArgsError(f"Values in dict '{CYAN}extraOptions{RESET}' must be type {DGREEN}int{RESET} not {DGREEN}{type(option).__name__}{RESET}.")
    # Actual system
    if not checkPara(maxOptions, None):
        while True:
            if startClear:
                clear()
            Print(question, animation=animation, **kwargs)
            answer = input("> ")
            try:
                answer = int(answer)
                for num in range(maxOptions + 1):
                    if num == 0:
                        if answer == 0 and zeroIsOption == True:
                            return 0
                        else:
                            continue
                    elif answer == num:
                        return answer
                    else:
                        continue
                invalidOption(answer=answer)
            except:
                if not checkPara(extraOptions, None) and checkPara(extraOptions, list):
                    for option in extraOptions:
                        if answer.casefold() == option.casefold():
                            return option
                        else:
                            continue
                    invalidOption(answer=answer)
                elif not checkPara(extraOptions, None) and checkPara(extraOptions, dict):
                    for option, output in extraOptions.items():
                        if answer.casefold() == option.casefold():
                            return output
                        else:
                            continue
                    invalidOption(answer=answer)
                else:
                    invalidOption(answer=answer)
    elif checkPara(maxOptions, None) and checkPara(extraOptions, list):
        while True:
            if startClear:
                clear()
            Print(question, animation=animation, **kwargs)
            answer = input("> ")
            for option in extraOptions:
                try:
                    if answer.casefold() == option.casefold():
                        return option
                    else:
                        continue
                except AttributeError:
                    logging.info(f"{AttributeError.__name__} as should.")
                    if type(option) is int:
                        if int(answer) == option:
                            return option
                    else:
                        logging.error(f"{IncompatableArgsError.__name__}")
                        raise IncompatableArgsError(f"Variable '{CYAN}extraOptions{RESET}' has a {DGREEN}{type(option).__name__}{RESET} which is incompatable with this function.")
            invalidOption(answer=answer)
    elif checkPara(maxOptions, None) and checkPara(extraOptions, dict):
        while True:
            if startClear:
                clear()
            Print(question, animation=animation, **kwargs)
            answer = input("> ")
            for option, output in extraOptions.items():
                try:
                    if answer.casefold() == str(option).casefold():
                        return output
                    else:
                        continue
                except AttributeError:
                    logging.info(f"{AttributeError.__name__} as should.")
                    if checkPara(option, int):
                        if int(answer) == option:
                            return output
                    else:
                        raise IncompatableArgsError(f"Variable '{CYAN}extraOptions{RESET}' has a {DGREEN}{type(option).__name__}{RESET} which is incompatable with this function.")
            invalidOption(answer=answer)
        





    


if __name__ == '__main__':
    ...