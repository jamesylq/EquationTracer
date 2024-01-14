# Imports
import pygame
import pyperclip
from numpy import *
from typing import *

try:
    from keyboard import *
except (ModuleNotFoundError, NameError, FileNotFoundError):
    from equationtracer.keyboard import *


# Pygame Setup
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("EquationTracer")
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
tinyfont = pygame.font.SysFont("Arial", 15)


# Funtions
def leftAlignPrint(screen: pygame.Surface, ft: pygame.font.Font, text: str, pos: Tuple[int, int], color: Tuple[int, int, int] = (255, 255, 255)) -> None:
    textObj = ft.render(text, True, color)
    screen.blit(textObj, textObj.get_rect(center=[pos[0] + ft.size(text)[0] / 2, pos[1]]))


def centredPrint(screen: pygame.Surface, ft: pygame.font.Font, text: str, pos: Tuple[int, int], color: Tuple[int, int, int] = (255, 255, 255)) -> None:
    textObj = ft.render(text, True, color)
    screen.blit(textObj, textObj.get_rect(center=pos))


def rightAlignPrint(screen: pygame.Surface, ft: pygame.font.Font, text: str, pos: Tuple[int, int], color: Tuple[int, int, int] = (255, 255, 255)) -> None:
    textObj = ft.render(text, True, color)
    screen.blit(textObj, textObj.get_rect(center=[pos[0] - ft.size(text)[0] / 2, pos[1]]))


def generateEquation(n, x, y, s, points):
    for m in range(len(points) - 1, -1, -1):
        points[m] = (points[m][0] - 250, 250 - points[m][1])
        points.append(points[m])

    xt = yt = ""
    M = len(points)
    r = []
    for k in range(-n, n + 1):
        cx = cy = 0
        for m in range(M):
            cx += cos(2 * pi * k * m / M) * points[m][0] + sin(2 * pi * k * m / M) * points[m][1]
            cy += cos(2 * pi * k * m / M) * points[m][1] - sin(2 * pi * k * m / M) * points[m][0]

        if k != -n:
            xt += " + "
            yt += " + "

        xt += f"{cx / M} cos({k * pi}t) - {cy / M} sin({k * pi}t)"
        yt += f"{cx / M} sin({k * pi}t) + {cy / M} cos({k * pi}t)"
        r.append((cx / M, cy / M))

    eq = f"({x} + {s}({xt}), {y} + {s}({yt}))".replace(" + -", " - ").replace(" - -", " + ")
    return eq, r


#
def main():
    term = drawing = False
    fields = [str(x[2]) for x in FIELDS]
    points = []

    x = y = delta = flashcount = 0
    selected = selectedx = -1
    s, n = 10, 25

    while True:
        mx, my = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        centredPrint(screen, font, "Parameters", (250, 20))
        centredPrint(screen, tinyfont, "Default Settings are automatically provided!", (250, 40))

        for l in range(len(FIELDS)):
            rightAlignPrint(screen, tinyfont, FIELDS[l][0] + ": ", (225, 100 + 50 * l))
            pygame.draw.rect(screen, (200, 200, 200), (240, 85 + 50 * l, 250, 30))
            leftAlignPrint(screen, tinyfont, fields[l], (245, 100 + 50 * l), (0, 0, 0))

            if l == selected and flashcount < 30:
                length = tinyfont.size(fields[l][:selectedx])[0]
                pygame.draw.line(screen, (0, 0, 0), (245 + length, 90 + 50 * l), (245 + length, 110 + 50 * l))

        pygame.draw.rect(screen, (200, 200, 200), (350, 460, 140, 30))
        if 350 <= mx <= 490 and 470 <= my <= 490:
            pygame.draw.rect(screen, (255, 255, 255), (350, 460, 140, 30), 3)
        else:
            pygame.draw.rect(screen, (100, 100, 100), (350, 460, 140, 30), 3)
        centredPrint(screen, tinyfont, "Start Drawing!", (420, 475), (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 350 <= mx <= 490 and 470 <= my <= 490:
                        term = True
                        break

                    if 240 <= mx <= 490 and (my - 85) % 50 <= 30 and 85 <= my < 65 + 50 * len(FIELDS):
                        selected = (my - 85) // 50
                        selectedx = min((mx - 240) // tinyfont.size('a')[0], len(fields[selected]))

                    elif selected != -1:
                        f = fields[selected].split('.')
                        if selected == 3:
                            fields[selected] = f[0]
                        else:
                            if len(f) > 2:
                                fields[selected] = f[0] + '.' + ''.join([f[s] for s in range(1, len(f))])
                            f = fields[selected].split('.')
                            if len(f) == 2 and int(f[1]) == 0:
                                fields[selected] = f[0]

                        while len(fields[selected]) > 1 and fields[selected][0] == '0':
                            fields[selected] = fields[selected][1:]

                        fields[selected] = str(min(max(float(fields[selected]), FIELDS[selected][1][0]), FIELDS[selected][1][1]))[:-2]
                        selected = -1

            if event.type == pygame.KEYDOWN:
                if selected != -1 and event.key in KEYS.keys():
                    fields[selected] = fields[selected][:selectedx] + KEYS[event.key] + fields[selected][selectedx:]
                    selectedx += 1

                if event.key == pygame.K_BACKSPACE:
                    delta = flashcount % 5

        if selected != -1 and selectedx:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_BACKSPACE] and (flashcount - delta) % 5 == 0:
                fields[selected] = fields[selected][:selectedx - 1] + fields[selected][selectedx:]
                selectedx -= 1

        if term:
            s, x, y, n = map(float, fields)
            n = int(n)
            s /= 250
            break

        flashcount = (flashcount + 1) % 50

        pygame.display.update()
        clock.tick(100)

    screen.fill((0, 0, 0))
    pygame.display.update()

    while True:
        term = False
        if drawing:
            points.append(tuple(pygame.mouse.get_pos()))

        centredPrint(screen, font, "Draw a Continuous Curve!", (250, 20))

        for i in range(len(points) - 1):
            pygame.draw.line(screen, (255, 255, 255), points[i], points[i + 1], 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    term = True
                    break

        if term:
            break

        pygame.display.update()
        clock.tick(100)

    T = 0
    eq, r = generateEquation(n, x, y, s, points)

    vects = []
    precomp = []
    for tm in range(1000):
        dx = 0
        dy = 0
        vect = []
        for k in range(n, -1, -1):
            cx = r[n + k][0] * cos(k * pi * tm / 1000) - r[n + k][1] * sin(k * pi * tm / 1000)
            cy = r[n + k][1] * cos(k * pi * tm / 1000) + r[n + k][0] * sin(k * pi * tm / 1000)
            dx += cx
            dy += cy
            vect.append((cx, cy))

            if k == 0:
                break

            cx = r[n - k][0] * cos(k * pi * tm / 1000) + r[n - k][1] * sin(k * pi * tm / 1000)
            cy = r[n - k][1] * cos(k * pi * tm / 1000) - r[n - k][0] * sin(k * pi * tm / 1000)
            dx += cx
            dy += cy
            vect.append((cx, cy))

        vects.append(vect)
        precomp.append((250 + dx, 250 - dy))

    while True:
        mx, my = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        centredPrint(screen, font, "Equation Generated!", (250, 20))

        prev = (250, 250)
        for k in range(-n, n + 1):
            curr = (prev[0] + vects[T][k + n][0], prev[1] - vects[T][k + n][1])
            pygame.draw.line(screen, (100, 100, 100), prev, curr, 3)
            pygame.draw.circle(screen, (150, 150, 150), curr, 2)
            prev = curr

        for i in range(T):
            pygame.draw.line(screen, (255, 255, 255), precomp[i], precomp[i + 1], 3)

        pygame.draw.rect(screen, (200, 200, 200), (350, 460, 140, 30))
        if 350 <= mx <= 490 and 470 <= my <= 490:
            pygame.draw.rect(screen, (255, 255, 255), (350, 460, 140, 30), 3)
        else:
            pygame.draw.rect(screen, (100, 100, 100), (350, 460, 140, 30), 3)
        centredPrint(screen, tinyfont, "Copy to Clipboard", (420, 475), (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pyperclip.copy(eq)

        pygame.display.update()
        clock.tick(100)

        T = (T + 1) % 1000
