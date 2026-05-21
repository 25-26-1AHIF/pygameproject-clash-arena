import pygame
from characters.ninja import Ninja
# from characters.thief import Thief
# from characters.vampire import Vampire

from screen_variables.screen_variables import ScreenVariables as SV

SV.init()
pygame.display.set_caption("Clash Arena")
screen = pygame.display.set_mode((SV.width, SV.height))
# Clock für die FPS Überwachung erstellen

FPS = SV.FPS
clock = pygame.time.Clock()

player_1 = Ninja(screen, SV.width, SV.height, 0, SV.height, 64, 1, 5)
player_1.ypos -= player_1.size

player_2 = Ninja(screen, SV.width, SV.height, 0, SV.height, 64, 2, 5)
player_2.ypos -= player_2.size
player_2.change_x_pos()

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
        winner = "Player 2"
        break

    if player_2.check_if_dead() == True:
        winner = "Player 1"
        break

    pygame.display.flip()

    # FPS überwachen

    clock.tick(FPS)

    # PyGame sauber beenden (cleanup)

game_over_text = SV.FONT_BIG.render(f"{winner} gewinnt!", True, "white")
game_over_rect = game_over_text.get_rect(center=(SV.width / 2, SV.height / 2))

running = True

while running:

    # Jedes Ereignis (Event) durchgehen

    for event in pygame.event.get():

        # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_ESCAPE:
            running = False

    screen.fill("black")

    screen.blit(source=game_over_text, dest = game_over_rect)

    # Das Display updaten

    pygame.display.flip()

    # FPS überwachen

    clock.tick(FPS)

    # PyGame sauber beenden (cleanup)

pygame.quit()
