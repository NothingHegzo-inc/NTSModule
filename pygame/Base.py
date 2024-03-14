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
from ButtonClasses.ButtonImage import ButtonImage

pygame.init()

class Base:
    screenColor: Optional[ColorRBG] = None
    quitImageOption: bool = False
    def __init__(self, function) -> None:
        self._Checkfunc(function)
        try:
            self.surface: Surface = pygame.display.get_surface()
            self.width: int = pygame.display.get_window_size()[0]
            self.height : int = pygame.display.get_window_size()[1]
        except pygame.error:
            raise UnknownVars(f"Please make sure that your pygame window is initialised/opened before calling on this decorator.")
    
    def _Checkfunc(self, function) -> None:
        def nothing() -> None: ...
        if type(function) is type(nothing):
            self.function = function
        else:
            raise IncorrectArgsError(f"Variable '{CYAN}function{RESET}' is supposed to be type {DGREEN}function{RESET} not type {DGREEN}{type(function).__name__}{RESET}.")
    
    def _Checkgame(self) -> None:
        if self.quitImageOption is True:
            width, height = pygame.display.get_window_size()
            quitImage = ButtonImage(str(os.path.dirname(os.path.realpath(__file__))) + "/Quit.png", (0,0), 0.5)
            quitImage.imageRect.topright = (width, 0)
            quitImage.draw(self.surface)
            quitImage.click()
            if quitImage.clicked:
                sys.exit()
        else:
            pass

    def __call__(self, *args, **kwargs) -> object:
        if self.screenColor is None:
            raise UnknownVars(f"Variable '{CYAN}screenColor{RESET}' was not specified. To specify it use '{DGREEN}Base{WHITE}.{CYAN}screenColor{WHITE} = {GREEN}yourScreenColor{WHITE}'.")
        self.surface.fill(self.screenColor)
        self._Checkgame()
        self.function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import sys
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    center: Coordinate = pygame.display.get_window_size()[0]/2, pygame.display.get_window_size()[1]/2
    Base.screenColor = (255,255,255)
    Base.quitImageOption = True
    @Base
    def game() -> None: ...
    run = True
    while run:
        game()
        #print(Base.cache_info())