import os, sys, time, logging
sys.path.append(os.path.dirname(__file__))
from imports import *
from Print import Print
from clear import clear

@overload
def invalidOption() -> None : ...
@overload
def invalidOption(animation: bool) -> None : ...
@overload
def invalidOption(answer: Any) -> None: ...
@overload
def invalidOption(system: str) -> None : ...
@overload
def invalidOption(answer: Any, animation: bool = False) -> None: ...
@overload
def invalidOption(system: str, animation: bool = False) -> None : ...
@logC()
def invalidOption(
        *args,
        answer: Optional[Any] = None,
        system: Optional[str] = None,
        animation: bool = False
) -> None:
    """
    Must use keyword inputs into this function.
    Example:
        invalidOption() -> print("That is not one of the options. Try again.")
    or
        invalidOption(answer=1) -> print("1 is not one of the options. Try again.")
    or
        invalidOption(system="System") -> print("System system has not been impleminted just yet.")

    Variable 'animation' is for animation typing, test it out to know what it does!
    How to use it?
        invalidOption(animation=True) -> Print("That is not one of the options. Try again.", True)
    """
    try:
        args[0]
        raise PositionalArgError(f"Function {YELLOW}invalidOption{WHITE}(){RESET} cannot be given positional arguments, and can only have keyword arguments.")
    except IndexError:
        logging.info(f"{IndexError.__name__} as should.")
        if not checkPara(system, None) and checkPara(answer, None):
            Print(f"{GREEN}{system}{RESET} system has not been impleminted just yet.", animation=animation)
        elif checkPara(system, None) and not checkPara(answer, None):
            Print(f"'{RED}{answer}{RESET}' is not one of the options. Try again.", animation=animation)
        elif checkPara(system, None) and checkPara(answer, None):
            Print(f"That is not one of the options. Try again.", animation=animation)
        elif not checkPara(system, None) and not checkPara(answer, None):
            raise IncompatableArgsError(f"Variables '{CYAN}answer{RESET}' and '{CYAN}system{RESET}' cannot both be given a value.")
    
    time.sleep(2)

if __name__ == '__main__':
    ...