import pygame, sys, os, logging
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(__file__))
pygame.init()
from imports import *
from pygVariables import *
from pygFuncs import *
from Print import Print
from ButtonClasses.Button import Button
pygame.init()


class DisplayText(Button):
    @property
    def boxBackground(self) -> bool: False
    boxBackground: bool = False
    def __init__(self, buttonInfo: Button) -> None:
        """Uses button class as a parent class to create a subclass and make it
        display text with options instead.
        """
        ############ Copy over ##########################
        self.font = buttonInfo.font
        self.fontColor = buttonInfo.fontColor
        self.buttonColor = buttonInfo.buttonColor
        self.buttonRect = buttonInfo.buttonRect
        self.ORButtonRectY = buttonInfo.ORButtonRectY
        self.ORbuttonColor = buttonInfo.ORbuttonColor
        self.originalText = buttonInfo.originalText
        self.text = buttonInfo.text
        self.textRect = buttonInfo.textRect
        self.pos = buttonInfo.pos
        self.clicked = buttonInfo.clicked
        self.down = buttonInfo.down
        #################################################
    
    @overload
    def draw(surface: Surface) -> None: """"""
    @overload
    def draw(surface: Surface, background: bool) -> None: """Use the button as it's background."""
    @overload
    def draw(surface: Surface, background: bool, edge: int, borderWidth: int) -> None: """Use the button as it's background."""
    def draw(
            self,
            surface: Surface,
            background: Optional[bool] = None,
            edge: int = 0,
            borderWidth: int = 0
    ) -> None:
        if checkPara(background, [None, bool]) is False:
            raise IncorrectArgsError(f"Argument '{CYAN}background{RESET}' has to be type {DGREEN}bool{RESET} if given, not type {DGREEN}{type(background).__name__}{RESET}.")
        self.textRect = self.text.get_rect()
        self.textRect.center = self.pos
        surface.blit(self.text, self.textRect)
        if background:
            pygame.draw.rect(surface, self.buttonColor, self.buttonRect, border_radius=edge)
            self.__drawBorder(surface, edge, borderWidth)
    
    def __drawBorder(self, surface, edge, borderWidth) -> None:
        if borderWidth > 0:
            borderRect: Rect = pygame.Rect((0,0), (self.buttonRect.width,self.buttonRect.height))
            borderRect.center = self.buttonRect.center
            pygame.draw.rect(surface, (0,0,0), borderRect, border_radius=edge, width=borderWidth)
