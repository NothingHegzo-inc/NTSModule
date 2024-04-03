import pygame, sys, os, logging
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(__file__))
pygame.init()
from imports import *
from pygVariables import *
from pygFuncs import *
from Print import Print
from ButtonClasses.ButtonImage import ButtonImage

pygame.init()

class Base:
    @property
    def screenColor(self) -> ColorRBG: self.centeralize()
    @property
    def quitImageOption(self) -> bool: ...
    @property
    def defaultColor(self) -> None: ...
    screenColor: Optional[ColorRBG] = None
    quitImageOption: bool = False
    defaultColor: ColorRBG = None    
    def __init__(self, function) -> None:
        self._Checkfunc(function)
        try:
            self.surface: Surface = pygame.display.get_surface()
            self.width: int = pygame.display.get_window_size()[0]
            self.height : int = pygame.display.get_window_size()[1]
            Base.center: Coordinate = int(pygame.display.get_window_size()[0]/2),int(pygame.display.get_window_size()[1]/2)
        except pygame.error:
            raise UnknownVars(f"Please make sure that your pygame window is initialised/opened before calling on this decorator.")
        Base.defaultColor = self.screenColor

    def _Checkfunc(self, function) -> None:
        def nothing() -> None: ...
        if type(function) is type(nothing):
            self.function = function
        else:
            raise IncorrectTypesError(arguments="function", argumentTypes=type(nothing))#raise IncorrectArgsError(f"Variable '{CYAN}function{RESET}' is supposed to be type {DGREEN}function{RESET} not type {DGREEN}{type(function).__name__}{RESET}.")
    
    def _Checkgame(self) -> None:
        if self.quitImageOption is True:
            width, height = pygame.display.get_window_size()
            quitImage = ButtonImage(str(os.path.dirname(os.path.realpath(__file__))) + "/Quit.png", (0,0), 0.5)
            quitImage.imageRect.topright = (width, 0)
            quitImage.draw(self.surface)
            quitImage._click()
            if quitImage.clicked:
                logging.info("Quit")
                sys.exit()

    def __call__(self, *args, **kwargs) -> object:
        if self.screenColor is None:
            raise UnknownVars(f"Variable '{CYAN}screenColor{RESET}' was not specified. To specify it use '{DGREEN}Base{WHITE}.{CYAN}screenColor{WHITE} = {GREEN}yourScreenColor{WHITE}'.")
        self.surface.fill(self.screenColor)
        self._Checkgame()
        returnValue = self.function(*args, **kwargs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        return returnValue
    
    def changeColor(color: ColorRBG) -> None:
        """Used in a while loop to change the screen color."""
        while Base.screenColor != color:
            Base.screenColor = color
            logging.debug(f"Screen color changed to {Base.screenColor}")
    
    def defaultScreenColor() -> None:
        """Used in a while loop to change the screen color back to the first color set in 'Base.screenColor' property."""
        while Base.screenColor != Base.defaultColor:
            Base.screenColor = Base.defaultColor
            logging.debug(f"Screen color changed to the deault color. Screen color: {Base.screenColor}. Default screen color {Base.defaultColor}")


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