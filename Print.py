import sys, os
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(f"{appendingSys}")
del appendingSys
from imports import *

import time

@overload
def Print() -> None: """Scroll to find out!"""
@overload
def Print(*printText, **kwargs) -> None: """Normal print, can add normal print function keyword arguments."""
@overload
def Print(*printText, animation: bool, **kwargs) -> None: """Print with animation option, set the second input variable to true."""
@overload
def Print(*printText, animation: bool, animationDelay: int | float, **kwargs) -> None: """Adding a delay option. Can manually change the delay between each letter printed in the animation."""
def Print(
        *printText,
        animation: bool = False,
        animationDelay: Optional[int | float] = None,
        **kwargs
) -> None:
    if animation is False:
        print(*printText, **kwargs)
    elif animation is True:
        if 'end' in kwargs or 'flush' in kwargs:
            raise IncompatableArgsError(f"Variables '{CYAN}end{RESET}' or '{CYAN}flush{RESET}' cannot be given with variable '{CYAN}animation{RESET}' being {BLUE}True{RESET}.")
        else:
            if animationDelay is not None:
                pythonType(printText, delayAmount=animationDelay, **kwargs)
            elif animationDelay is None:
                pythonType(printText, **kwargs)
    else:
        raise IncorrectArgsError(f"Variable '{CYAN}animation{RESET}' has to be a {DGREEN}bool{RESET} not a {DGREEN}{type(animation).__name__}{RESET}.")

@overload
def pythonType(text: str) -> None: ...
@overload
def pythonType(text: str, delayAmount: int | float) -> None: ...
def pythonType(
        text: str, 
        delayAmount: float | int = 0.025,
        **kwargs
) -> None:
    if type(text) is tuple or type(text) is list:
        text = " ".join(list(text))
    for char in text:
        print(char, **kwargs, end='', flush=True)
        time.sleep(delayAmount)
    print()


if __name__ == '__main__':
    Print("Hi dfgg dfg dfg dfg dfg df", flush=True)