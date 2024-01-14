import pygame
from typing import *

try:
    from printers import *
except (ModuleNotFoundError, NameError, FileNotFoundError):
    from equationtracer.printers import *


class Button:
    def __init__(self, rect: Tuple[int, int, int, int], *, fillColor: Tuple[int, int, int] = (64, 64, 64),
                 hoverFillColor: Tuple[int, int, int] = None, hoverBorderColor: Tuple[int, int, int] = None,
                 borderColor: Tuple[int, int, int] = (0, 0, 0), borderThickness: int = 3, render: Union[str, pygame.SurfaceType] = None,
                 collisionTexture: Union[str, pygame.SurfaceType] = None, font: pygame.font.Font = None, fontColor: Tuple[int, int, int] = (0, 0, 0)) -> None:

        ButtonManager.buttons.append(self)

        self.font = font
        self.rect = rect
        self.texture = render
        self.fillColor = fillColor
        self.fontColor = fontColor
        self.borderColor = borderColor
        self.x, self.y, self.w, self.h = rect
        self.borderThickness = borderThickness
        self.centre = (self.x + self.w // 2, self.y + self.h // 2)
        self.hoverFillColor = hoverFillColor if hoverFillColor is not None else fillColor
        self.hoverBorderColor = hoverBorderColor if hoverBorderColor is not None else borderColor
        self.collisionTexture = render if collisionTexture is None and render is not None else collisionTexture

    def update(self) -> None:
        self.rect = (self.x, self.y, self.w, self.h)
        self.centre = (self.x + self.w // 2, self.y + self.h // 2)

    def draw(self, mousePos: Tuple[int, int]) -> None:
        self.update()

        if collision(mousePos, self.rect):
            if self.collisionTexture is None:
                pygame.draw.rect(ButtonManager.screen, self.hoverFillColor, self.rect)
            elif type(self.collisionTexture) is str:
                pygame.draw.rect(ButtonManager.screen, self.hoverFillColor, self.rect)
                centredPrint(ButtonManager.screen, self.font, self.collisionTexture, self.centre, self.fontColor)
            else:
                ButtonManager.screen.blit(self.collisionTexture, self.centre, self.fontColor)

            if self.borderThickness > 0:
                pygame.draw.rect(ButtonManager.screen, self.hoverBorderColor, self.rect, self.borderThickness)

        else:
            if self.texture is None:
                pygame.draw.rect(ButtonManager.screen, self.fillColor, self.rect)
            elif type(self.texture) is str:
                pygame.draw.rect(ButtonManager.screen, self.hoverFillColor, self.rect)
                centredPrint(ButtonManager.screen, self.font, self.texture, self.centre, self.fontColor)
            else:
                ButtonManager.screen.blit(self.texture, self.centre)

            if self.borderThickness > 0:
                pygame.draw.rect(ButtonManager.screen, self.borderColor, self.rect, self.borderThickness)

    def check(self) -> bool:
        return collision(ButtonManager.mousePos, self.rect)


def collision(point: Tuple[int, int], rect: Tuple[int, int, int, int]) -> bool:
    return rect[0] <= point[0] < rect[0] + rect[2] and rect[1] <= point[1] < rect[1] + rect[3]


class ButtonManager:
    buttons: List[Button] = []
    screen: pygame.Surface = None
    mousePos: Tuple[int, int] = (-1, -1)

    def __init__(self, surface: pygame.Surface) -> None:
        ButtonManager.screen = surface

    def __len__(self) -> int:
        return len(ButtonManager.buttons)


def updateButtons(mousePos: Tuple[int, int] = None, active: List[Button] = None, *, updateScreen: bool = False) -> List[str]:
    executeCommands = []
    ButtonManager.mousePos = pygame.mouse.get_pos() if mousePos is None else mousePos

    if active is None:
        active = ButtonManager.buttons

    for button in active:
        button.draw(mousePos)

    if updateScreen:
        pygame.display.update()

    return executeCommands
