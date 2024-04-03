import os, sys, platform, logging
sys.path.append(os.path.dirname(__file__))
from imports import *
from Print import Print

@overload
def clear() -> None: """Uses the default system to find the operating system's clear keyword."""
@overload
def clear(specifier: str) -> None: """Lets you use a different specified keyword instead of the system finding it itself."""
@overload
def clear(permaSpecifier: str) -> None: """Lets you add a permenant specifier that will be used over all the clear called functions. When calling this function with that argument, it will not run but just specify the specifier."""

permaAdded: bool = False
@logC()
def clear(
        specifier: Optional[str] = None,
        permaSpecifier: Optional[str] = None
) -> None:
    if permaSpecifier is not None:
        if checkPara(permaSpecifier, str):
            global permaAdded
            if permaAdded is False:
                global permanentSpecifier
                permanentSpecifier = permaSpecifier
                permaAdded = True
            else:
                raise CannotOverwrite('permaSpecifier')
        else:
            raise IncorrectTypesError(arguments="permaSpecifier", argumentTypes=str)#raise IncorrectArgsError(f"Variable '{CYAN}permaSpecifier{RESET}' has to be type {DGREEN}str{RESET} not {DGREEN}{type(permaSpecifier).__name__}{RESET}.")
    else:
        if checkPara(specifier, None) and permaAdded is False:
            if platform.system() == "Windows":
                os.system("cls")
            elif platform.system() == "Linux" :
                os.system("clear")
            else:
                Print(f"Clear system not functional on this operating system. If your operating system has a different command for clearing the terminal use {YELLOW}clear{WHITE}({CYAN}permaSpecifier {WHITE}= '{GREEN}yourCommand{WHITE}'){RESET} to permanentaly specify what command the {YELLOW}clear{WHITE}(){RESET} function should use when called.")
        elif not checkPara(specifier, None):
            if type(specifier) is str:
                print(f"If you can see this, function '{YELLOW}clear{WHITE}(){RESET}' did not work because '{BLUE}specifier{RESET} : {RED}{specifier}{RESET}' is incorrect or in-operable.")
                os.system(specifier)
            else:
                raise IncorrectTypesError(arguments="specifier", argumentTypes=str)#raise IncorrectArgsError(f"Variable '{CYAN}specifier{RESET}' has to be type {DGREEN}str{RESET} not {DGREEN}{type(specifier).__name__}{RESET}.")
        elif permaAdded:
            Print(f"If you can see this, function '{YELLOW}clear{WHITE}(){RESET}' did not work because '{BLUE}permaSpecifier{RESET} : {RED}{permanentSpecifier}{RESET}' is incorrect or in-operable.")
            os.system(permanentSpecifier)
        else:
            raise UnknownError(functionName=clear)


if __name__ == '__main__':
    clear()