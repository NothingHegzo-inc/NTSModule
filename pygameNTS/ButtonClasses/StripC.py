import pygame, os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
pygame.init()
from imports import *
from pygVariables import *
from pygFuncs import *
from Print import Print


widthEach = int
heightEach = int
frameStartEach = Coordinate



class StripC:
    image: filePath | Surface
    width : int
    height: int
    frameStart : int
    @overload
    def __init__(self, image: filePath) -> None: ...
    @overload
    def __init__(self, image: Surface) -> None: ...
    def __init__(
            self,
            image: Surface | filePath
    ) -> None:
        if type(image) is Surface:
            self.imageInput = image
        elif type(image) is str:
            self.imageInput: Surface = pygame.image.load(image).convert_alpha()
        else:
             raise IncorrectTypesError(arguments="image", argumentTypes=Surface)#raise IncorrectArgsError(f"Argument '{CYAN}image{RESET}' has to be type {DGREEN}pygame.Surface{RESET} or {DGREEN}str{RESET} not type {DGREEN}{type(image).__name__}{RESET}.")

    @overload
    def strip(self, width: int, height: int) -> Surface: """"""
    @overload
    def strip(self, width: int, height: int, frameStart: Coordinate) -> Surface: """"""
    @overload
    def strip(self, listOfImages: list[tuple[widthEach: int, heightEach: int, frameStartEach: Coordinate]]) -> list[Surface]: """Must use keyword argument 'listOfImages' and no other arguments."""

    def strip(
            self,
            width: Optional[int] = None,
            height: Optional[int] = None,
            frameStart: Coordinate = (0,0),
            listOfImages: Optional[list[tuple[widthEach, heightEach, frameStartEach]]] = None
    ) -> Surface:
        if listOfImages is None:
            if width is None or height is None:
                raise UnknownVars(variables=["width", "height"])
            strippedImage: Surface = pygame.Surface((width, height))
            strippedImage.blit(self.imageInput, (0,0), (frameStart, (width, height)))
            strippedImage.set_colorkey((0,0,0))
            return strippedImage
        elif type(listOfImages) is list:
            if width is not None or height is not None or frameStart != (0,0):
                raise IncompatableArgsError(f"Arguments '{CYAN}width{RESET}', '{CYAN}height{RESET}' and/or '{CYAN}frameStart{RESET}' cannot be given while '{CYAN}listOfImages{RESET}' is given.")
            listOfSurfaces = []
            for w,h,f in listOfImages:
                image: Surface = pygame.Surface((w,h))
                image.blit(self.imageInput, (0,0), (f, (w,h)))
                image.set_colorkey((0,0,0))
                listOfSurfaces.append(image)
            return listOfSurfaces
        elif type(listOfImages) is not list:
            raise IncorrectArgsError(f"Argument '{CYAN}listOfImages{RESET}' has to be type {DGREEN}list{WHITE}[{DGREEN}tuple{WHITE}[{DGREEN}int{WHITE}, {DGREEN}int{WHITE}, {CYAN}Coordinate{WHITE}]{WHITE}]{RESET} not type {DGREEN}{type(listOfImages).__name__}{RESET}")
        else:
            raise UnknownError(functionName=StripC.strip)

if __name__ == '__main__':
    ...