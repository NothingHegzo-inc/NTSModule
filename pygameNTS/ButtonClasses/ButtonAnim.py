import pygame, sys, os, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
pygame.init()
from imports import *
from pygVariables import *
from pygFuncs import *
from Print import Print
from ButtonClasses.ButtonImage import ButtonImage

class ButtonAnim:
    def __init__(
            self,
            imageUp: ButtonImage,
            imageDown: ButtonImage
    ) -> None:
        if type(imageUp) is not ButtonImage:
            raise IncorrectTypesError(arguments="imageUp", argumentTypes=ButtonImage)#raise IncorrectArgsError(f"Variables '{CYAN}imageUp{RESET}' has to be type {DGREEN}{ButtonImage.__name__}{RESET} not type {DGREEN}{type(imageUp).__name__}{RESET}.")
        elif type(imageDown) is not ButtonImage:
            raise IncorrectTypesError(arguments="imageDown", argumentTypes=ButtonImage)#raise IncorrectArgsError(f"Variables '{CYAN}imageDown{RESET}' has to be type {DGREEN}{ButtonImage.__name__}{RESET} not type {DGREEN}{type(imageUp).__name__}{RESET}.")
        # Variables
        self.imageUp = imageUp
        self.imageDown = imageDown
        self.clicked = False
        self.rect: Rect = pygame.Rect((self.imageUp.imageRect.x, self.imageUp.imageRect.y), (self.imageUp.imageRect.width, self.imageUp.imageRect.height))
    def call(self, surface) -> None:
        self.imageUp._click()
        if self.imageUp.clicked:
            self.imageDown.draw(surface)
        else:
            self.imageUp.draw(surface)
        self.clicked = self.imageUp.clicked
    def click(self) -> bool:
        return self.imageUp.click()

if __name__ == '__main__':
    ButtonAnim("hiu","hi")