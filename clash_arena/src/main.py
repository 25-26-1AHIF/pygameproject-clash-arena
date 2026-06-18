import pygame

from characters.ninja import Ninja
from characters.vampire import Vampire
from characters.knight import Knight
from screens.screens import Screens
import json

from screen_variables.screen_variables import ScreenVariables as SV

def game_over_screen(clock, FPS, winner, screen):

    game_over_text = SV.FONT_BIG.render(f"Spieler {winner} gewinnt!", True, "dark red")
    game_over_rect = game_over_text.get_rect(center=(SV.width / 2, SV.height / 2))

    text2 = SV.FONT_BIG.render(f"+10 xp!", True, "dark red")
    rect2 = game_over_text.get_rect(center=(SV.width / 2, SV.height / 2 + 100))

    menu_text = SV.FONT_MIDDLE.render("Zurück zum Menü", True, "dark red")
    menu_text_rect = menu_text.get_rect(center=(SV.width/2, SV.height - 100))

    hintergrund = pygame.image.load("assets/highscore_hintergrund.png").convert()

    running = True

    while running:

        # Jedes Ereignis (Event) durchgehen

        for event in pygame.event.get():

            # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if menu_text_rect.collidepoint(event.pos):
                    return

        screen.fill("black")

        screen.blit(hintergrund, (0,0))

        screen.blit(source=game_over_text, dest = game_over_rect)
        pygame.draw.rect(surface=screen, rect=menu_text_rect, color="black")
        screen.blit(source=text2, dest=rect2)
        screen.blit(source=menu_text, dest = menu_text_rect)

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

    try:
        with open("leaderboard.json", "r") as fp:
            leaderboard = json.load(fp)

    except:
        screens.error_message("Hinweis: Leaderboard konnte nicht geladen werden")

        leaderboard: dict = {}

        with open("leaderboard.json", "w") as fp:
            json.dump(leaderboard, fp)


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
                filepath = player_tuple[2]

                winner = screens.play_screen(player_1, player_2, filepath)

                if winner[0] == 1:
                    game_over_screen(clock, FPS, 1, screen)

                    leaderboard[winner[1]] += 1

                    with open("leaderboard.json", "w") as fp:
                        json.dump(leaderboard, fp)

                elif winner[0] == 2:
                    game_over_screen(clock, FPS, 2, screen)

                    leaderboard[winner[1]] += 1

                    with open("leaderboard.json", "w") as fp:
                        json.dump(leaderboard, fp)

                winner = ()
                next_screen = "menü"

                continue

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

            # KI-Anfang
            # KI: Claude Code
            # Prompt: füge zu dem spiel hinzu, dass nach den charakter-auswahlen, immer ein screen kommt, um den namen des spielers einzugeben. Also: man wählt seinen charakter aus, dann muss man seinen namen eingeben. Markiere den anfang von allem, was du änderst mit "# KI-Anfang" und das ende mit "# KI-Ende"
            player_1.name = screens.enter_name(1)
            # KI-Ende

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

            # KI-Anfang
            # KI: Claude Code
            # Prompt: füge zu dem spiel hinzu, dass nach den charakter-auswahlen, immer ein screen kommt, um den namen des spielers einzugeben. Also: man wählt seinen charakter aus, dann muss man seinen namen eingeben. Markiere den anfang von allem, was du änderst mit "# KI-Anfang" und das ende mit "# KI-Ende"
            player_2.name = screens.enter_name(2)
            # KI-Ende

            filepath = screens.choose_background()

            winner = screens.play_screen(player_1, player_2, filepath)

            if winner != "menü":
                game_over_screen(clock, FPS, winner, screen)

                try:
                    leaderboard[winner][1] += 10

                    if leaderboard[winner][1] >= 100 * leaderboard[winner][0]:
                        leaderboard[winner][1] = 0
                        leaderboard[winner][0] += 1

                except:
                    leaderboard[winner] = [1, 10]

                with open("leaderboard.json", "w") as fp:
                    json.dump(leaderboard, fp)

            winner = ""
            next_screen = "menü"
            continue

if __name__ == "__main__":
    SV.init()
    FPS = SV.FPS
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SV.width, SV.height))

    screens = Screens(FPS, screen, clock, SV.width, SV.height, SV)

    main(screens, screen, SV, clock, FPS)

    pygame.quit()