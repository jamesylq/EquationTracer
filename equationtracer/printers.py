import pygame
from typing import Tuple


def leftAlignPrint(scr: pygame.Surface, ft: pygame.font.Font, text: str, pos: Tuple[int, int], color: Tuple[int, int, int] = (255, 255, 255)) -> None:
    textObj = ft.render(text, True, color)
    scr.blit(textObj, textObj.get_rect(center=[pos[0] + ft.size(text)[0] / 2, pos[1]]))


def centredPrint(scr: pygame.Surface, ft: pygame.font.Font, text: str, pos: Tuple[int, int], color: Tuple[int, int, int] = (255, 255, 255)) -> None:
    textObj = ft.render(text, True, color)
    scr.blit(textObj, textObj.get_rect(center=pos))


def rightAlignPrint(scr: pygame.Surface, ft: pygame.font.Font, text: str, pos: Tuple[int, int], color: Tuple[int, int, int] = (255, 255, 255)) -> None:
    textObj = ft.render(text, True, color)
    scr.blit(textObj, textObj.get_rect(center=[pos[0] - ft.size(text)[0] / 2, pos[1]]))
