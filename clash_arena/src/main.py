import pygame
from characters.ninja import Ninja
# from characters.thief import Thief
# from characters.vampire import Vampire
from screens.screens import Screens

from screen_variables.screen_variables import ScreenVariables as SV

def play_screen(clock, screen, FPS, player_1, player_2):
    pygame.display.set_caption("Clash Arena")

    running = True
    # Die Main Loop (Game Loop)
    while running:

        # Jedes Ereignis (Event) durchgehen

        for event in pygame.event.get():

            # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

            if event.type == pygame.QUIT:
                running = False


        screen.fill("black")

        # Das Display updaten

        player_1.update_and_draw()
        player_2.update_and_draw()

        player_1.check_punch_collision(player_2)
        player_2.check_punch_collision(player_1)

        if player_1.check_if_dead() == True:
            return "Player 2"

        if player_2.check_if_dead() == True:
            return "Player 1"

        pygame.display.flip()

        # FPS überwachen

        clock.tick(FPS)

    # PyGame sauber beenden (cleanup)

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

def main(screens, player_1, player_2):
    next_screen: str = ""

    while True:

        if next_screen == "spielen":
            next_screen = screens.play_screen(player_1, player_2)

        elif next_screen == "beenden":
            return

        elif next_screen == "steuerung":
            next_screen = screens.todo()
            # TODO

        elif next_screen == "laden":
            next_screen = screens.todo()
            # TODO

        elif next_screen == "menü":
            next_screen = screens.menu()

        else:
            next_screen = screens.menu()

if __name__ == "__main__":
    SV.init()
    FPS = SV.FPS
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SV.width, SV.height))

    screens = Screens(FPS, screen, clock, SV.width, SV.height, SV)

    player_1 = Ninja(screen, SV.width, SV.height, 0, SV.height, 64, 1, 5)
    player_1.ypos -= player_1.size

    player_2 = Ninja(screen, SV.width, SV.height, 0, SV.height, 64, 2, 5)
    player_2.ypos -= player_2.size
    player_2.change_x_pos()

    # menu ist nicht fertig, muss von alex noch gemacht werden
    main(screens, player_1, player_2)

    # screens.play_screen(player_1, player_2)


    pygame.quit()