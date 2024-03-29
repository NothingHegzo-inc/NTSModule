import pygame, sys, os, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
pygame.init()
from imports import *
from pygVariables import *
from pygFuncs import *
from Print import Print


class ButtonImage:
    @overload
    def __init__(self, image: Surface, pos: Coordinate) -> None: ...
    @overload
    def __init__(self, image: filePath, pos: Coordinate) -> None: ...
    @overload
    def __init__(self, image: Surface | filePath, pos: Coordinate, scale: int) -> None: ...
    @overload
    def __init__(self, image: Surface | filePath, pos: Coordinate, scale: int, elevation: int) -> None: ...
    def __init__(
            self,
            image: Surface | filePath,
            pos : Coordinate,
            scale: int = 1,
            elevation: Optional[int] = None
    ) -> None:
        # Image
        if type(image) is Surface:
            self.image: Surface = image
        elif type(image) is str:
            self.image: Surface = pygame.image.load(image).convert_alpha()
        else:
            raise IncorrectTypesError(arguments="image", argumentTypes=Surface)#raise TypeError(f"Variable '{CYAN}image{RESET}' has to be type {DGREEN}pygame{WHITE}.{DGREEN}Surface{RESET} or {DGREEN}str{RESET} not type {DGREEN}{type(image).__name__}{RESET}.")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.imageRect = self.image.get_rect()
        self.imageMask = pygame.mask.from_surface(self.image)
        self.imageRect.center = pos
        self.ORimageRectY = self.imageRect.y
        # Elevation
        self.elevation: int = elevation
        self.dElev: int = elevation
        if self.elevation is not None:
            self.EleRect: Rect = pygame.Rect((0,0), (self.image.get_width(), self.image.get_height()))
        # Extra variables
        self.pos: Coordinate = pos
        self.clicked = False
        self.down = False
        self.scale = scale
    
    @overload
    def draw(self, surface: Surface) -> None: ...
    @overload
    def draw(self, surface: Surface, edge: int) -> None: ...
    def draw(
            self,
            surface: Surface,
            edge: int = 0
    ) -> None:
        self.__elevation(surface, edge)
        surface.blit(self.image, self.imageRect)
        self.__click()
    
    def __elevation(
            self,
            surface: Surface,
            edge: int
    ) -> None:
            if self.elevation is not None:
                if type(self.elevation) is not int:
                    raise IncorrectTypesError(arguments="elevation", argumentTypes=int)#raise IncorrectArgsError(f"Variable '{CYAN}elevation{RESET}' can only be type {DGREEN}int{RESET} not {DGREEN}{type(self.elevation).__name__}{RESET}.")
                self.imageRect.y = self.ORimageRectY - self.elevation
                self.EleRect.height = self.imageRect.height + self.elevation
                self.EleRect.midtop = self.imageRect.midtop
                pygame.draw.rect(surface, (0,0,0), self.EleRect, border_radius=edge)
                self.__changingElev()

    def __changingElev(self) -> None:
        if self.imageRect.collidepoint(variables()[0]) and variables()[1][0]:
            self.elevation = 0
        else:
            self.elevation = self.dElev
    
    def _click(self) -> None:
        """Used by other classes to change this classes variable self.clicked"""
        if self.imageRect.collidepoint(variables()[0]) and variables()[1][0] and self.clicked is False:
            self.clicked = True
        else:
            if variables()[1][0] is False:
                self.clicked = False
    
    def __click(self) -> None:
        if self.imageRect.collidepoint(variables()[0]) and variables()[1][0] and self.clicked is False:
            self.clicked = True
        else:
            if variables()[1][0] is False:
                self.clicked = False

    def click(self) -> bool:
        if self.imageRect.collidepoint(variables()[0]) and variables()[1][0] and self.down is False:
            self.down = True
        elif self.down is True and self.imageRect.collidepoint(variables()[0]) and variables()[1][0] is False:
            self.down = False
            return True
        elif self.down is True and self.imageRect.collidepoint(variables()[0]) is False:
            self.down = False
            return False
        return False
        
        

        
        

if __name__ == '__main__':
    ...

