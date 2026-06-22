import pygame

class ScreenVariables:
    width = 1668
    height = 943
    FPS = 60
    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font = None
    FONT_SMALL: pygame.font.Font = None

    @staticmethod
    def init():
        pygame.init()

        ScreenVariables.FONT_BIG = pygame.sysfont.SysFont("calisto mt", 72, bold=True)
        ScreenVariables.FONT_MIDDLE = pygame.sysfont.SysFont("century", 48, bold=True)
        ScreenVariables.FONT_SMALL = pygame.sysfont.SysFont("arial", 36, bold=False)