from pygame import *

MIN = -1e9
MAX = 1e9

FIELDS = [
    ["Size of Window as Rendered", (0, MAX), 10],
    ["x-Coordinate as Rendered", (MIN, MAX), 0],
    ["y-Coordinate as Rendered", (MIN, MAX), 0],
    ["Degree of Generated Equation", (5, 50), 25]
]

KEYS = {
    K_0: '0',
    K_1: '1',
    K_2: '2',
    K_3: '3',
    K_4: '4',
    K_5: '5',
    K_6: '6',
    K_7: '7',
    K_8: '8',
    K_9: '9',
    K_PERIOD: '.',
    K_KP_PERIOD: '.',
    K_MINUS: '-',
    K_KP_MINUS: '-',
}