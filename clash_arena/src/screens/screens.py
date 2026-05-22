import pygame

class Screens:
    def __init__(self, fps, screen, clock, screenwidth, screenheight, screenvariablen):
        self.FPS = fps
        self.screen = screen
        self.clock = clock
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.SV = screenvariablen

    def play_screen(self, player_1, player_2) -> str:
        pygame.display.set_caption("Clash Arena")

        running = True
        # Die Main Loop (Game Loop)
        while running:

            # Jedes Ereignis (Event) durchgehen

            for event in pygame.event.get():

                # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                if event.type == pygame.QUIT:
                    return "beenden"

            self.screen.fill("black")

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

            self.clock.tick(self.FPS)

    def draw_menu(self):
        title_text = self.SV.FONT_BIG.render("Clash Arena", True, "dark blue")
        title_text_rect = title_text.get_rect(center=(self.screenwidth/2, 50))

        neuer_kampf_text = self.SV.FONT_MIDDLE.render("Neuer Kampf", True, "dark blue")
        neuer_kampf_rect = neuer_kampf_text.get_rect(center=(self.screenwidth/2, 125))

        kampf_laden_text = self.SV.FONT_MIDDLE.render("Kampf laden", True, "dark blue")
        kampf_laden_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 175))

        steuerung_text = self.SV.FONT_MIDDLE.render("Steuerung", True, "dark blue")
        steuerung_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 225))

        beenden_text = self.SV.FONT_MIDDLE.render("Beenden", True, "dark blue")
        beenden_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 275))

        pygame.draw.rect(surface=self.screen, rect=(0, self.screenheight-75, self.screenwidth, 100), color="green")

        self.screen.blit(source=title_text, dest=title_text_rect)

        pygame.draw.rect(surface=self.screen, rect=neuer_kampf_rect, color="light blue")
        self.screen.blit(source=neuer_kampf_text, dest=neuer_kampf_rect)

        pygame.draw.rect(surface=self.screen, rect=kampf_laden_rect, color="light blue")
        self.screen.blit(source=kampf_laden_text, dest=kampf_laden_rect)

        pygame.draw.rect(surface=self.screen, rect=steuerung_rect, color="light blue")
        self.screen.blit(source=steuerung_text, dest=steuerung_rect)

        pygame.draw.rect(surface=self.screen, rect=beenden_rect, color="light blue")
        self.screen.blit(source=beenden_text, dest=beenden_rect)




    def menu(self) -> str:

        title_text = self.SV.FONT_BIG.render("Clash Arena", True, "dark blue")
        title_text_rect = title_text.get_rect(center=(self.screenwidth / 2, 50))

        neuer_kampf_text = self.SV.FONT_MIDDLE.render("Neuer Kampf", True, "dark blue")
        neuer_kampf_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 125))

        kampf_laden_text = self.SV.FONT_MIDDLE.render("Kampf laden", True, "dark blue")
        kampf_laden_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 175))

        steuerung_text = self.SV.FONT_MIDDLE.render("Steuerung", True, "dark blue")
        steuerung_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 225))

        beenden_text = self.SV.FONT_MIDDLE.render("Steuerung", True, "dark blue")
        beenden_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 275))

        while True:

            # Jedes Ereignis (Event) durchgehen
            for event in pygame.event.get():

                # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                if event.type == pygame.QUIT:
                    return "beenden"

                if event.type == pygame.KEYDOWN:

                    if event.type == pygame.K_ESCAPE:
                        return "beenden"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if neuer_kampf_rect.collidepoint(event.pos):
                        print("Starten gedrückt")
                        return "spielen"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if kampf_laden_rect.collidepoint(event.pos):
                        print("Laden gedrückt")
                        return "laden"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if steuerung_rect.collidepoint(event.pos):
                        print("Steuerung gedrückt")
                        return "steuerung"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if beenden_rect.collidepoint(event.pos):
                        print("Beenden gedrückt")
                        return "beenden"

            self.screen.fill("white")
            self.draw_menu()

            pygame.display.flip()

    def todo(self) -> str:

        text = self.SV.FONT_BIG.render("Noch nicht fertig", True, "dark blue")
        text_rect = text.get_rect(center=(self.screenwidth / 2, 50))

        text2 = self.SV.FONT_BIG.render("Zurück zum Menü", True, "dark blue")
        text2_rect = text.get_rect(center=(self.screenwidth / 2, self.screenheight / 2))

        while True:

            for event in pygame.event.get():

                # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                if event.type == pygame.QUIT:
                    return "beenden"

                if event.type == pygame.KEYDOWN:

                    if event.type == pygame.K_ESCAPE:
                        return "beenden"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if text2_rect.collidepoint(event.pos):
                        print("Starten gedrückt")
                        return "menü"

            self.screen.fill("white")

            self.screen.blit(source=text, dest=text_rect)
            self.screen.blit(source=text2, dest=text2_rect)

            pygame.display.flip()
