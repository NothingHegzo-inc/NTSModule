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

class InputBox(Button):
    def __init__(self, buttonInfo: Button) -> None:
        """Uses button class as a parent class to create a subclass and make it
        an input box.
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
        self.textRect.center = self.buttonRect.center
        self.ORButtonRectWidth = self.buttonRect.width
        self.newText: str = ""
        if self.fontColor == (0,0,0):
            self.text = self.font.render(self.originalText, True, (128,128,128))
    
    @overload
    def draw(self, surface: Surface) -> None: ...
    @overload
    def draw(self, surface: Surface, hoverColor: ColorRBG) -> None: ...
    @overload
    def draw(self, surface: Surface, edge: int, borderWidth: int) -> None: ...
    def draw(
            self, 
            surface: Surface,
            hoverColor: Optional[ColorRBG] = None,
            edge: int = 15, 
            borderWidth: int = 1
    ) -> None:
        if hoverColor is None:
            hoverColor = hoverColorFunc(self.buttonColor)
        self.buttonRect.center = self.pos
        pygame.draw.rect(surface, self.buttonColor, self.buttonRect, border_radius=edge)
        if self.newText == "":
            surface.blit(self.text, self.textRect)
        else:
            text = self.font.render(self.newText, True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = self.buttonRect.center
            surface.blit(text, textRect)
        

        self.__inputText()
        self._Button__drawBorder(surface, edge, borderWidth)
        self._Button__hover(hoverColor)
    
    def __click(self) -> None:
        if self.buttonRect.collidepoint(variables()[0]) and variables()[1][0] and self.clicked is False:
            self.clicked = True
        else:
            if variables()[1][0] and self.buttonRect.collidepoint(variables()[0]) is False:
                self.clicked = False

    def __inputText(self) -> None:
        self.__click()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and self.clicked:
                if event.key == pygame.K_BACKSPACE:# and len([x for x in self.newText]) > 0:
                    self.newText = self.newText[:-1]
                    pygame.key.set_repeat(175)
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    self.newText += event.unicode
                    pygame.key.set_repeat(250)

    def __str__(self) -> str:
        return f"{self.newText}"


if __name__ == '__main__':
    ...#from Base import Base
    