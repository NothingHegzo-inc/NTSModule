import sys, os
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(f"{appendingSys}")
del appendingSys
from imports import *
from clear import clear
from Print import Print
from invalidOption import invalidOption

import time

@overload
def question(question: str, maxOptions: int) -> int: ...
@overload
def question(question: str, extraOptions: list[str] | dict[str , int]) -> int | str: ...
@overload
def question(question: str, maxOptions: int, animation: bool) -> int: ...
@overload
def question(question: str, maxOptions: int, zeroIsOption: bool) -> int: ...
@overload
def question(question: str, maxOptions: int, startClear: bool) -> int: ...
@overload
def question(question: str, maxOptions: int, extraOptions: list[str] | dict[str , int]) -> int | str: ...
@overload
def question(question: str, maxOptions: int, zeroIsOption: bool, animation: bool, startClear: bool, extraOptions: list[str] | dict[str , int]) -> int | str: ...
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
            if type(extraOptions) is not list and type(extraOptions) is not dict:
                raise IncorrectArgsError(f"Variable '{CYAN}extraOptions{RESET}' has to be type {DGREEN}list{PINK}[{DGREEN}str{PINK}]{RESET} or type {DGREEN}dict{PINK}[{DGREEN}str{RESET}, {DGREEN}int{PINK}]{RESET}. {BLACK}(even if there is one option){RESET}")
    if maxOptions is None and (type(extraOptions) is not list and type(extraOptions) is not dict):
        raise IncompatableArgsError(f"If variable '{CYAN}maxOptions{RESET}' is not given, then variable '{CYAN}extraOptions{RESET}' has to be a {DGREEN}list{PINK}[{DGREEN}str{PINK}]{RESET} or {DGREEN}dict{PINK}[{DGREEN}str{RESET}, {DGREEN}int{PINK}]{RESET} not a {RED}{type(extraOptions).__name__}{RESET}.")
    if animation is True and ('end' in kwargs or 'flush' in kwargs):
        raise IncompatableArgsError(f"Variables '{CYAN}end{RESET}' or '{CYAN}flush{RESET}' cannot be given with variable '{CYAN}animation{RESET}' being {BLUE}True{RESET}.")
    if strict:
        if type(extraOptions) is list:
            for option in extraOptions:
                if type(option) is not str:
                    raise IncorrectArgsError(f"Options in variable '{CYAN}extraOptions{RESET}' must be type {DGREEN}str{RESET} not {DGREEN}{type(option).__name__}{RESET}.")
                else:
                    continue
        elif type(extraOptions) is dict:
            for option, output in extraOptions.items():
                if type(option) is not str:
                    raise IncorrectArgsError(f"Keys in dict '{CYAN}extraOptions{RESET}' must be type {DGREEN}str{RESET} not {DGREEN}{type(option).__name__}{RESET}.")
                if type(output) is not int:
                    raise IncorrectArgsError(f"Values in dict '{CYAN}extraOptions{RESET}' must be type {DGREEN}int{RESET} not {DGREEN}{type(option).__name__}{RESET}.")
    # Actual system
    if maxOptions is not None:
        while True:
            if startClear is True:
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
                if extraOptions is not None and type(extraOptions) is list:
                    for option in extraOptions:
                        if answer.casefold() == option.casefold():
                            return option
                        else:
                            continue
                    invalidOption(answer=answer)
                elif extraOptions is not None and type(extraOptions) is dict:
                    for option, output in extraOptions.items():
                        if answer.casefold() == option.casefold():
                            return output
                        else:
                            continue
                    invalidOption(answer=answer)
                else:
                    invalidOption(answer=answer)
    elif maxOptions is None and type(extraOptions) is list:
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
                    if type(option) is int:
                        if int(answer) == option:
                            return option
                    else:
                        raise IncompatableArgsError(f"Variable '{CYAN}extraOptions{RESET}' has a {DGREEN}{type(option).__name__}{RESET} which is incompatable with this function.")
            invalidOption(answer=answer)
    elif maxOptions is None and type(extraOptions) is dict:
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
                    if type(option) is int:
                        if int(answer) == option:
                            return output
                    else:
                        raise IncompatableArgsError(f"Variable '{CYAN}extraOptions{RESET}' has a {DGREEN}{type(option).__name__}{RESET} which is incompatable with this function.")
            invalidOption(answer=answer)
        





    


if __name__ == '__main__':
    Print(question("Test", extraOptions={"1" : 2, "2" : 1}, strict=False))