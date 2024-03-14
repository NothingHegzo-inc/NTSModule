import pygame
import sys, os
import platform
if platform.system() == "Windows":
    appendingSlash = "\\"
elif platform.system() == "Linux":
    appendingSlash = "/"
appendingSys: str = "/".join(str(os.path.dirname(os.path.realpath(__file__))).split(appendingSlash)[:-2])
sys.path.append(f"{appendingSys}")
appendingSys: str = "/".join(str(os.path.dirname(os.path.realpath(__file__))).split(appendingSlash)[:-1])
sys.path.append(f"{appendingSys}")
del appendingSys
from imports import *
from pygVariables import *
from pygFuncs import *
from ButtonClasses.ButtonImage import ButtonImage
pygame.init()

class ButtonAnim:
    def __init__(
            self,
            imageUp: ButtonImage,
            imageDown: ButtonImage
    ) -> None:
        if type(imageUp) is not ButtonImage:
            raise IncorrectArgsError(f"Variables '{CYAN}imageUp{RESET}' has to be type {DGREEN}{ButtonImage.__name__}{RESET} not type {DGREEN}{type(imageUp).__name__}{RESET}.")
        elif type(imageDown) is not ButtonImage:
            raise IncorrectArgsError(f"Variables '{CYAN}imageDown{RESET}' has to be type {DGREEN}{ButtonImage.__name__}{RESET} not type {DGREEN}{type(imageUp).__name__}{RESET}.")
        # Variables
        self.imageUp = imageUp
        self.imageDown = imageDown
        self.clicked = False
        self.rect: Rect = pygame.Rect((self.imageUp.imageRect.x, self.imageUp.imageRect.y), (self.imageUp.imageRect.width, self.imageUp.imageRect.height))
    def call(self, surface) -> None:
        if self.imageUp.clicked:
            self.imageDown.draw(surface)
        else:
            self.imageUp.draw(surface)
        self.imageUp.click()
        self.clicked = self.imageUp.clicked
    def click(self) -> bool:
        return self.imageUp.click()       

if __name__ == '__main__':
    ...