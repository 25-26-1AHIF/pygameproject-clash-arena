import pygame

class ScreenVariables:
    width = 640
    height = 480
    FPS = 60
    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font = None
    FONT_SMALL: pygame.font.Font = None

    @staticmethod
    def init():
        pygame.init()

        ScreenVariables.FONT_BIG = pygame.sysfont.SysFont("arial", 48, bold=True)
        ScreenVariables.FONT_MIDDLE = pygame.sysfont.SysFont("arial", 36, bold=False)
        ScreenVariables.FONT_SMALL = pygame.sysfont.SysFont("arial", 24, bold=False)