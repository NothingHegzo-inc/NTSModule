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


widthEach = int
heightEach = int
frameStartEach = int


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
            raise IncorrectArgsError

    @overload
    def strip(self, width: int, height: int) -> Surface: ...
    @overload
    def strip(self, width: int, height: int, frameStart: int) -> Surface: ...
    @overload
    def strip(self, listOfImages: list[tuple[widthEach, heightEach, frameStartEach]]) -> list[Surface]: ...

    def strip(
            self,
            width: Optional[int] = None,
            height: Optional[int] = None,
            frameStart: int = 0,
            listOfImages: Optional[list[tuple[widthEach, heightEach, frameStartEach]]] = None
    ) -> Surface:
        if listOfImages is None:
            if width is None or height is None:
                raise UnknownVars(f"Variables '{CYAN}width{RESET}' or '{CYAN}{height}{RESET}' were not given.")
            strippedImage: Surface = pygame.Surface((width, height))
            strippedImage.blit(self.imageInput, (0,0), ((frameStart, 0), (width, height)))
            strippedImage.set_colorkey((0,0,0))
            return strippedImage
        elif type(listOfImages) is list:
            listOfSurfaces = []
            for info in listOfImages:
                w = info[0]
                h = info[1]
                f = info[2]
                image: Surface = pygame.Surface((w,h))
                image.blit(self.imageInput, (0,0), ((f, 0), (w,h)))
                image.set_colorkey((0,0,0))
                listOfSurfaces.append(image)
            return listOfSurfaces

