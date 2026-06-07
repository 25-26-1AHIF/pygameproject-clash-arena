import pygame

from characters.ninja import Ninja
from characters.vampire import Vampire
from characters.knight import Knight
from screens.screens import Screens

from screen_variables.screen_variables import ScreenVariables as SV

def game_over_screen(clock, FPS, winner, screen):

    game_over_text = SV.FONT_BIG.render(f"{winner} gewinnt!", True, "white")
    game_over_rect = game_over_text.get_rect(center=(SV.width / 2, SV.height / 2))

    menu_text = SV.FONT_MIDDLE.render("Zurück zum Menü", True, "white")
    menu_text_rect = menu_text.get_rect(center=(SV.width/2, SV.height - 100))

    running = True

    while running:

        # Jedes Ereignis (Event) durchgehen

        for event in pygame.event.get():

            # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if menu_text_rect.collidepoint(event.pos):
                    print("Zurück zum Menü")

        screen.fill("black")

        screen.blit(source=game_over_text, dest = game_over_rect)

        # Das Display updaten

        pygame.display.flip()

        # FPS überwachen

        clock.tick(FPS)

def menu(clock, FPS, screen):



    running = True

    while running:

        # Jedes Ereignis (Event) durchgehen

        for event in pygame.event.get():

            # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.K_ESCAPE:
                while True:
                    pass




        screen.fill("black")


        # Das Display updaten

        pygame.display.flip()

        # FPS überwachen

        clock.tick(FPS)

def main(screens, screen, SV, clock, FPS):
    next_screen: str = ""

    while True:

        if next_screen == "":
            next_screen = screens.menu()

        elif next_screen == "beenden":
            return

        elif next_screen == "steuerung":
            next_screen = screens.steuerung()

        elif next_screen == "laden":
            player_tuple = screens.laden(screen, SV, clock, FPS)

            if player_tuple == "menü":
                next_screen = "menü"

            else:
                player_1 = player_tuple[0]
                player_2 = player_tuple[1]

                next_screen = screens.play_screen(player_1, player_2)

        elif next_screen == "menü":
            next_screen = screens.menu()

        elif next_screen == "spielen":
            player_1 = Ninja(screen, SV.width, SV.height, 0, SV.height - 100, 128, 1, 2, FPS, clock)
            player_1.ypos -= player_1.size
            player_1.change_last_direction()

            player_2 = Vampire(screen, SV.width, SV.height, 0, SV.height - 100, 128, 2, 2, FPS, clock)
            player_2.ypos -= player_2.size
            player_2.change_x_pos()
            player_2.change_last_direction()
            next_screen = screens.play_screen(player_1, player_2)

        elif next_screen == "character select":
            character_1 = screens.choose_character(1)

            if character_1 == "ninja":
                player_1 = Ninja(screen, SV.width, SV.height, 0, SV.height - 100, 128, 1, 2, FPS, clock)
                player_1.ypos -= player_1.size
                player_1.change_last_direction()

            elif character_1 == "knight":
                player_1 = Knight(screen, SV.width, SV.height, 0, SV.height - 100, 128, 1, 2, FPS, clock)
                player_1.ypos -= player_1.size
                player_1.change_last_direction()

            else:
                player_1 = Vampire(screen, SV.width, SV.height, 0, SV.height - 100, 128, 1, 2, FPS, clock)
                player_1.ypos -= player_1.size
                player_1.change_last_direction()

            character_2 = screens.choose_character(2)

            if character_2 == "ninja":
                player_2 = Ninja(screen, SV.width, SV.height, 0, SV.height - 100, 128, 2, 2, FPS, clock)
                player_2.ypos -= player_2.size
                player_2.change_x_pos()
                player_2.change_last_direction()

            elif character_2 == "knight":
                player_2 = Knight(screen, SV.width, SV.height, 0, SV.height - 100, 128, 2, 2, FPS, clock)
                player_2.ypos -= player_2.size
                player_2.change_x_pos()
                player_2.change_last_direction()

            else:
                player_2 = Vampire(screen, SV.width, SV.height, 0, SV.height - 100, 128, 2, 2, FPS, clock)
                player_2.ypos -= player_2.size
                player_2.change_x_pos()
                player_2.change_last_direction()

            next_screen = screens.play_screen(player_1, player_2)


if __name__ == "__main__":
    SV.init()
    FPS = SV.FPS
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SV.width, SV.height))

    screens = Screens(FPS, screen, clock, SV.width, SV.height, SV)

    #player_1 = Ninja(screen, SV.width, SV.height, 0, SV.height - 100, 128, 1, 2, FPS, clock)
    #player_1.ypos -= player_1.size
    #player_1.change_last_direction()

    #player_2 = Knight(screen, SV.width, SV.height, 0, SV.height - 100, 128, 2, 2, FPS, clock)
    #player_2.ypos -= player_2.size
    #player_2.change_x_pos()
    #player_1.change_last_direction()

    main(screens, screen, SV, clock, FPS)

    # screens.play_screen(player_1, player_2)

    pygame.quit()