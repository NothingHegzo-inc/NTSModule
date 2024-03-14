import os, platform, sys
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(f"{appendingSys}")
del appendingSys
from imports import *
from variables import *
from Print import Print


#def _clearWrapper(clearFunc):


@overload
def clear() -> None: """Uses the default system to find the operating system's clear keyword."""
@overload
def clear(specifier: str) -> None: """Lets you use a different specified keyword instead of the system finding it itself."""
@overload
def clear(permaSpecifier: str) -> None: """Lets you add a permenant specifier that will be used over all the clear called functions. When calling this function with that argument, it will not run but just specify the specifier."""

permaAdded: bool = False
def clear(
        specifier: Optional[str] = None,
        permaSpecifier: Optional[str] = None
) -> None:
    if permaSpecifier is not None:
        if type(permaSpecifier) is str:
            global permaAdded
            if permaAdded is False:
                global permanentSpecifier
                permanentSpecifier = permaSpecifier
                permaAdded = True
            else:
                raise CannotOverride(f"'{CYAN}permaSpecifier{RESET}' variable has already been specified and cannot be overriden.")
        else:
            raise IncorrectArgsError(f"Variable '{CYAN}permaSpecifier{RESET}' has to be type {DGREEN}str{RESET} not {DGREEN}{type(permaSpecifier).__name__}{RESET}.")
    else:
        if specifier is None and permaAdded is False:
            if platform.system() == "Windows":
                os.system("cls")
            elif platform.system() == "Linux" :
                os.system("clear")
            else:
                Print(f"Clear system not functional on this operating system. If your operating system has a different command for clearing the terminal use {YELLOW}clear{WHITE}({CYAN}permaSpecifier {WHITE}= '{GREEN}yourCommand{WHITE}'){RESET} to permanentaly specify what command the {YELLOW}clear{WHITE}(){RESET} function should use when called.")
        elif specifier is not None:
            if type(specifier) is str:
                print(f"If you can see this, function '{YELLOW}clear{WHITE}(){RESET}' did not work because '{BLUE}specifier{RESET} : {RED}{specifier}{RESET}' is incorrect or in-operable.")
                os.system(specifier)
            else:
                raise IncorrectArgsError(f"Variable '{CYAN}specifier{RESET}' has to be type {DGREEN}str{RESET} not {DGREEN}{type(specifier).__name__}{RESET}.")
        elif permaAdded is True:
            Print(f"If you can see this, function '{YELLOW}clear{WHITE}(){RESET}' did not work because '{BLUE}permaSpecifier{RESET} : {RED}{permanentSpecifier}{RESET}' is incorrect or in-operable.")
            os.system(permanentSpecifier)
        else:
            raise UnknownError(f"This error was given by function {YELLOW}clear{WHITE}(){RESET}.")


if __name__ == '__main__':
    clear()