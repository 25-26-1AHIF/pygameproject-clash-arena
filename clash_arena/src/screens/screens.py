import pygame
import json

class Screens:
    def __init__(self, fps, screen, clock, screenwidth, screenheight, screenvariablen):
        self.FPS = fps
        self.screen = screen
        self.clock = clock
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.SV = screenvariablen

    def error_message(self):
        message = self.SV.FONT_BIG.render("Spiel konnte nicht gespeichert werden!", True, "dark red")
        message_rect = message.get_rect(center=(self.screenwidth/2, 500))

        return_message = self.SV.FONT_MIDDLE.render("Zurück", True, "dark red")
        return_rect = return_message.get_rect(center=(self.screenwidth/2, 700))

        while True:

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_rect.collidepoint(event.pos):
                        return

            self.screen.fill("black")

            self.screen.blit(source=message, dest=message_rect)
            self.screen.blit(source=return_message, dest=return_rect)

            pygame.display.flip()


    def draw_menu(self):

        neuer_kampf_text = self.SV.FONT_MIDDLE.render("Neuer Kampf", True, "dark red")
        neuer_kampf_rect = neuer_kampf_text.get_rect(center=(self.screenwidth/2, 490))

        kampf_laden_text = self.SV.FONT_MIDDLE.render("Kampf laden", True, "dark red")
        kampf_laden_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 580))

        steuerung_text = self.SV.FONT_MIDDLE.render("Steuerung", True, "dark red")
        steuerung_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 670))

        highscore_text = self.SV.FONT_MIDDLE.render("Highscores", True, "dark red")
        highscore_rect = highscore_text.get_rect(center=(self.screenwidth/2, 760))

        beenden_text = self.SV.FONT_MIDDLE.render("Beenden", True, "dark red")
        beenden_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 840))

        #pygame.draw.rect(surface=self.screen, rect=neuer_kampf_rect, color="black")
        self.screen.blit(source=neuer_kampf_text, dest=neuer_kampf_rect)

        #pygame.draw.rect(surface=self.screen, rect=kampf_laden_rect, color="black")
        self.screen.blit(source=kampf_laden_text, dest=kampf_laden_rect)

        #pygame.draw.rect(surface=self.screen, rect=steuerung_rect, color="black")
        self.screen.blit(source=steuerung_text, dest=steuerung_rect)

        #pygame.draw.rect(surface=self.screen, rect=beenden_rect, color="black")
        self.screen.blit(source=beenden_text, dest=beenden_rect)

        self.screen.blit(source=highscore_text, dest=highscore_rect)

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

    def steuerung(self):

        text = self.SV.FONT_BIG.render("Spieler 1", True, "dark blue")
        text_rect = text.get_rect(center=(self.screenwidth / 2, 150))

        text2 = self.SV.FONT_BIG.render("Spieler 2", True, "dark blue")
        text2_rect = text.get_rect(center=(self.screenwidth / 2, 200))

        zurueck = self.SV.FONT_BIG.render("Zurück", True, "dark blue")
        zurueck_rect = zurueck.get_rect(center=(self.screenwidth / 2, 350))

        hintergrund = pygame.image.load("assets/steuerung_hintergrund.png").convert()

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
                        self.steuerung_anzeigen(2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if text_rect.collidepoint(event.pos):
                        self.steuerung_anzeigen(1)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if zurueck_rect.collidepoint(event.pos):
                        return "menü"


            self.screen.fill("white")

            self.screen.blit(source=hintergrund, dest=(0,0))


            self.screen.blit(source=text, dest=text_rect)
            self.screen.blit(source=text2, dest=text2_rect)

            pygame.draw.rect(surface=self.screen, rect=zurueck_rect, color="light blue")
            self.screen.blit(source=zurueck, dest=zurueck_rect)

            pygame.display.flip()

    def steuerung_anzeigen(self, spieler):

        if spieler == 1:
            springen_text = self.SV.FONT_MIDDLE.render("W -> Springen", True, "dark blue")
            springen_text_rect = springen_text.get_rect(center=(self.screenwidth / 2, 50))

            links_text = self.SV.FONT_MIDDLE.render("A -> links laufen", True, "dark blue")
            links_text_rect = links_text.get_rect(center=(self.screenwidth / 2, 100))

            rechts_text = self.SV.FONT_MIDDLE.render("D -> rechts laufen", True, "dark blue")
            rechts_text_rect = rechts_text.get_rect(center=(self.screenwidth / 2, 150))

            attacke_text = self.SV.FONT_MIDDLE.render("E -> normale Attacke", True, "dark blue")
            attacke_text_rect = attacke_text.get_rect(center=(self.screenwidth / 2, 200))

            spezial_text = self.SV.FONT_MIDDLE.render("Q -> Spezialattacke", True, "dark blue")
            spezial_text_rect = spezial_text.get_rect(center=(self.screenwidth / 2, 250))

            blocken_text = self.SV.FONT_MIDDLE.render("F -> Blocken", True, "dark blue")
            blocken_text_rect = blocken_text.get_rect(center=(self.screenwidth / 2, 300))

            zurueck_text = self.SV.FONT_MIDDLE.render("Zurück", True, "dark blue")
            zurueck_text_rect = zurueck_text.get_rect(center=(self.screenwidth / 2, 400))

            hintergrund = pygame.image.load("assets/steuerung_hintergrund.png").convert()

            while True:
                for event in pygame.event.get():

                    # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                    if event.type == pygame.QUIT:
                        return

                    if event.type == pygame.KEYDOWN:

                        if event.type == pygame.K_ESCAPE:
                            return

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # klickposition = event.pos (x, y)
                        if zurueck_text_rect.collidepoint(event.pos):
                            return

                    self.screen.fill("white")

                    self.screen.blit(source=hintergrund, dest=(0, 0))

                    pygame.draw.rect(surface=self.screen, rect=springen_text_rect, color="light blue")
                    self.screen.blit(source=springen_text, dest=springen_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=links_text_rect, color="light blue")
                    self.screen.blit(source=links_text, dest=links_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=rechts_text_rect, color="light blue")
                    self.screen.blit(source=rechts_text, dest=rechts_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=attacke_text_rect, color="light blue")
                    self.screen.blit(source=attacke_text, dest=attacke_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=spezial_text_rect, color="light blue")
                    self.screen.blit(source=spezial_text, dest=spezial_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=blocken_text_rect, color="light blue")
                    self.screen.blit(source=blocken_text, dest=blocken_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=zurueck_text_rect, color="light blue")
                    self.screen.blit(source=zurueck_text, dest=zurueck_text_rect)

                    pygame.display.update()


        elif spieler == 2:
            springen_text = self.SV.FONT_MIDDLE.render("I -> Springen", True, "dark blue")
            springen_text_rect = springen_text.get_rect(center=(self.screenwidth / 2, 50))

            links_text = self.SV.FONT_MIDDLE.render("J -> links laufen", True, "dark blue")
            links_text_rect = links_text.get_rect(center=(self.screenwidth / 2, 100))

            rechts_text = self.SV.FONT_MIDDLE.render("L -> rechts laufen", True, "dark blue")
            rechts_text_rect = rechts_text.get_rect(center=(self.screenwidth / 2, 150))

            attacke_text = self.SV.FONT_MIDDLE.render("O -> normale Attacke", True, "dark blue")
            attacke_text_rect = attacke_text.get_rect(center=(self.screenwidth / 2, 200))

            spezial_text = self.SV.FONT_MIDDLE.render("U -> Spezialattacke", True, "dark blue")
            spezial_text_rect = spezial_text.get_rect(center=(self.screenwidth / 2, 250))

            blocken_text = self.SV.FONT_MIDDLE.render("M -> Blocken", True, "dark blue")
            blocken_text_rect = blocken_text.get_rect(center=(self.screenwidth / 2, 300))

            zurueck_text = self.SV.FONT_MIDDLE.render("Zurück", True, "dark blue")
            zurueck_text_rect = zurueck_text.get_rect(center=(self.screenwidth / 2, 400))

            hintergrund = pygame.image.load("assets/steuerung_hintergrund.png").convert()

            while True:
                for event in pygame.event.get():

                    # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                    if event.type == pygame.QUIT:
                        return

                    if event.type == pygame.KEYDOWN:

                        if event.type == pygame.K_ESCAPE:
                            return

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # klickposition = event.pos (x, y)
                        if zurueck_text_rect.collidepoint(event.pos):
                            return

                    self.screen.fill("white")

                    self.screen.blit(source=hintergrund, dest=(0, 0))


                    pygame.draw.rect(surface=self.screen, rect=springen_text_rect, color="light blue")
                    self.screen.blit(source=springen_text, dest=springen_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=links_text_rect, color="light blue")
                    self.screen.blit(source=links_text, dest=links_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=rechts_text_rect, color="light blue")
                    self.screen.blit(source=rechts_text, dest=rechts_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=attacke_text_rect, color="light blue")
                    self.screen.blit(source=attacke_text, dest=attacke_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=spezial_text_rect, color="light blue")
                    self.screen.blit(source=spezial_text, dest=spezial_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=blocken_text_rect, color="light blue")
                    self.screen.blit(source=blocken_text, dest=blocken_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=zurueck_text_rect, color="light blue")
                    self.screen.blit(source=zurueck_text, dest=zurueck_text_rect)


                    pygame.display.update()


    def pausemenu(self, player_1, player_2):

        self.SV.init()

        text = self.SV.FONT_BIG.render("Weiterspielen", True, "dark blue")
        text_rect = text.get_rect(center=(self.screenwidth / 2, 200))

        text2 = self.SV.FONT_BIG.render("Steuerung", True, "dark blue")
        text2_rect = text2.get_rect(center=(self.screenwidth / 2, 300))

        text3 = self.SV.FONT_BIG.render("Speichern und Zurück zum Menü", True, "dark red")
        text3_rect = text3.get_rect(center=(self.screenwidth/2, 400))

        zurueck = self.SV.FONT_BIG.render("Zurück zum Menü", True, "dark blue")
        zurueck_rect = zurueck.get_rect(center=(self.screenwidth / 2, 500))

        while True:

            for event in pygame.event.get():

                # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                if event.type == pygame.QUIT:
                    return "beenden"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if text2_rect.collidepoint(event.pos):
                        self.steuerung()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if text_rect.collidepoint(event.pos):
                        return "weiter"

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if text3_rect.collidepoint(event.pos):


                        try:
                            save_player_1: dict = {'player type' : player_1.player_type,
                                                'hp' : player_1.hp,
                                                'xpos' : player_1.xpos,
                                                'ypos' : player_2.ypos,
                                                'special_dict' : player_1.special_dict,
                                                'name' : player_1.name}

                            save_player_2: dict = {'player type': player_2.player_type,
                                                'hp': player_2.hp,
                                                'xpos': player_2.xpos,
                                                'ypos': player_2.ypos,
                                                'special_dict': player_2.special_dict,
                                                'name' : player_2.name}

                            player_list: list = [save_player_1, save_player_2]

                            with open("saved_game/saved_game.json", "w") as fp:
                                json.dump(player_list, fp, indent=2)

                            print("Erfolgreich gespeichert!")
                            return "menü"

                        except:
                            print("Speichern fehlgeschlagen!")
                            self.error_message()
                            return "weiter"




                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if zurueck_rect.collidepoint(event.pos):
                        return "menü"

            self.screen.fill("white")

            self.screen.blit(source=text, dest=text_rect)
            self.screen.blit(source=text2, dest=text2_rect)
            self.screen.blit(source=text3, dest=text3_rect)

            pygame.draw.rect(surface=self.screen, rect=zurueck_rect, color="light blue")
            self.screen.blit(source=zurueck, dest=zurueck_rect)

            pygame.display.flip()

    def play_screen(self, player_1, player_2):
        pygame.display.set_caption("Clash Arena")
        play_map = pygame.image.load("assets/play_map.png").convert()

        vs_text = self.SV.FONT_BIG.render("VS", True, "dark red")
        vs_rect = vs_text.get_rect(center=(self.screenwidth/2, 64))

        running = True
        # Die Main Loop (Game Loop)
        while running:

            # Jedes Ereignis (Event) durchgehen

            for event in pygame.event.get():

                # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                next_screen = self.pausemenu(player_1, player_2)

                if next_screen == "menü":
                    return "menü"

            self.screen.fill("white")

            # Das Display updaten
            self.screen.blit(play_map, (0, 0))
            self.screen.blit(source=vs_text, dest=vs_rect)

            player_1.update_and_draw(player_2)
            player_2.update_and_draw(player_1)

            player_1.check_punch_collision(player_2)
            player_2.check_punch_collision(player_1)

            player_1.check_special_collision(player_2.special_dict)
            player_2.check_special_collision(player_1.special_dict)

            if player_1.check_if_dead() == True:
                return "Player 2"

            if player_2.check_if_dead() == True:
                return "Player 1"

            pygame.display.flip()

            # FPS überwachen

            self.clock.tick(self.FPS)

        # PyGame sauber beenden (cleanup)

    def highscores(self):

        background = pygame.image.load("assets/highscore_hintergrund.png")

        zurueck_text = self.SV.FONT_MIDDLE.render("Zurück zum Menü", True, "dark red")
        zurueck_rect = zurueck_text.get_rect(center=(self.screenwidth/2, 840))

        while True:

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if zurueck_rect.collidepoint(event.pos):
                        return

            self.screen.fill("black")

            self.screen.blit(source=background, dest=(0,0))

            self.screen.blit(source=zurueck_text, dest=zurueck_rect)

            pygame.display.flip()


    def menu(self) -> str:

        neuer_kampf_text = self.SV.FONT_MIDDLE.render("Neuer Kampf", True, "dark red")
        neuer_kampf_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 490))

        kampf_laden_text = self.SV.FONT_MIDDLE.render("Kampf laden", True, "dark red")
        kampf_laden_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 580))

        steuerung_text = self.SV.FONT_MIDDLE.render("Steuerung", True, "dark red")
        steuerung_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 670))

        highscore_text = self.SV.FONT_MIDDLE.render("Highscores", True, "dark red")
        highscore_rect = highscore_text.get_rect(center=(self.screenwidth / 2, 760))

        beenden_text = self.SV.FONT_MIDDLE.render("Beenden", True, "dark red")
        beenden_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 840))

        hintergrund = pygame.image.load("assets/clash_arena_menu.png").convert()

        pygame.mixer.music.load("assets/title_music.mp3")

        pygame.mixer.music.play(-1)

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
                        pygame.mixer.music.stop()
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
                        self.steuerung()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if highscore_rect.collidepoint(event.pos):
                        print("Highscores gedrückt")
                        self.highscores()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if beenden_rect.collidepoint(event.pos):
                        print("Beenden gedrückt")
                        return "beenden"

            self.screen.fill("white")

            self.screen.blit(hintergrund, (0, 0))

            self.draw_menu()
            pygame.display.flip()