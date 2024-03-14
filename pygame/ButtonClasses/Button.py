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
from Print import Print
from pygVariables import *
from pygFuncs import *


class Button:
    @overload
    def __init__(self, text:str, buttonColor: ColorRBG, pos: Coordinate) -> None: ...
    @overload
    def __init__(self, text: str, buttonColor: ColorRBG, pos: Coordinate, width: int, height: int, elevation: int) -> None: ...
    @overload
    def __init__(self, text: str, buttonColor: ColorRBG, pos: Coordinate, fontName: str, fontSize: int, fontColor: ColorRBG) -> None: ...
    def __init__(
            self,
            text: str,
            buttonColor: ColorRBG,
            pos: Coordinate,
            width: int = 100,
            height: int = 50,
            fontName: Optional[Font] = None,
            fontSize: int = 20,
            fontColor: ColorRBG = (0,0,0),
            elevation: Optional[int] = None
    ) -> None:
        # Font
        self.font: Font = pygame.font.SysFont(fontName, fontSize)
        # Button
        self.buttonRect: Rect = pygame.Rect((0, 0),(width, height))
        self.buttonRect.center = pos
        self.ORButtonRectY = self.buttonRect.y
        self.buttonColor: ColorRBG = buttonColor
        self.ORbuttonColor = buttonColor
        # Text
        self.text: Surface = self.font.render(text, True, fontColor)
        self.textRect: Rect = self.text.get_rect()
        # Elevation
        self.elevation: int = elevation
        self.dElev: int = elevation
        if self.elevation is not None:
            self.EleRect: Rect = pygame.Rect((0,0), (width, height))
        # Extra variables
        self.pos: Coordinate = pos
        self.clicked = False
        

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

        self.__elevation(surface, edge)

        self.textRect.center = self.buttonRect.center
        pygame.draw.rect(surface, self.buttonColor, self.buttonRect, border_radius=edge)
        surface.blit(self.text, self.textRect)

        self.__drawBorder(surface, edge, borderWidth)
        self.__hover(hoverColor)
        self.click()

    def __elevation(
            self,
            surface: Surface,
            edge: int
    ) -> None:
            if self.elevation is not None:
                if type(self.elevation) is not int:
                    raise IncorrectArgsError(f"Variable '{CYAN}elevation{RESET}' can only be type {DGREEN}int{RESET} not {DGREEN}{type(self.elevation).__name__}{RESET}.")
                self.buttonRect.y = self.ORButtonRectY - self.elevation
                self.EleRect.height = self.buttonRect.height + self.elevation
                self.EleRect.midtop = self.buttonRect.midtop
                pygame.draw.rect(surface, (0,0,0), self.EleRect, border_radius=edge)
                self.__changingElev()

    def __changingElev(self) -> None:
        if self.buttonRect.collidepoint(variables()[0]) and variables()[1][0]:
            self.elevation = 0
        else:
            self.elevation = self.dElev

    def __drawBorder(
            self, 
            surface: Surface, 
            edge: int, 
            borderWidth: int
    ) -> None:
        if borderWidth > 0:
            borderRect: Rect = pygame.Rect((0,0), (self.buttonRect.width,self.buttonRect.height))
            borderRect.center = self.buttonRect.center
            pygame.draw.rect(surface, (0,0,0), borderRect, border_radius=edge, width=borderWidth)

    def __hover(
            self,
            hoverColor: ColorRBG
    ) -> None:
        if self.buttonRect.collidepoint(variables()[0]):
            self.buttonColor = hoverColor
        else:
            self.buttonColor = self.ORbuttonColor


    def click(self) -> bool:
        if self.buttonRect.collidepoint(variables()[0]) and variables()[1][0] and self.clicked is False:
            self.clicked = True
            return True
        else:
            if variables()[1][0] is False:
                self.clicked = False
                return False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    center: Coordinate = pygame.display.get_window_size()[0]/2, pygame.display.get_window_size()[1]/2
    x = Button("test", (255,0,255), center, fontName="Arial", elevation=10)
    run = True
    while run:
        screen.fill((255,255,255))
        
        if x.click():
            print("BOOM")

        x.draw(screen, borderWidth=1, hoverColor=hoverColorFunc((255,0,255), allColors=True))
        #print(x.buttonRect.center, x.elevation)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
