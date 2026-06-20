import pygame
import json

from clash_arena.src.characters.knight import Knight
from clash_arena.src.characters.ninja import Ninja
from clash_arena.src.characters.vampire import Vampire

def sort(liste) -> list:
    stoppen: bool = False

    while stoppen == False:

        stoppen = True
        for index in range(len(liste[0: - 1])):
            element = liste[index]
            element_next = liste[index + 1]

            if element[1][0] < element_next[1][0]:

                liste[index] = element_next
                liste[index + 1] = element

                stoppen = False

    return liste

class Screens:
    def __init__(self, fps, screen, clock, screenwidth, screenheight, screenvariablen):
        self.FPS = fps
        self.screen = screen
        self.clock = clock
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.SV = screenvariablen

    def error_message(self, message: str):
        message = self.SV.FONT_BIG.render(message, True, "dark red")
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

    def choose_character(self, player: int) -> str:

        text = self.SV.FONT_MIDDLE.render(f"Spieler {player}:", True, "dark red")
        text_rect = text.get_rect(center=(self.screenwidth/2, 150))

        ninja_select = pygame.image.load("assets/ninja/ninja_select.png").convert()
        ninja_rect = pygame.Rect(250, 300, 128*2, 128*2)
        width, height = ninja_select.get_size()

        ninja_hit_rect = pygame.Rect(250 + 128/2, 300+64, 128, 192)
        scaled_ninja = pygame.transform.scale(ninja_select, (width*2, height*2))

        knight_select = pygame.image.load("assets/knight/knight_select.png").convert()
        knight_rect = pygame.Rect((self.screenwidth/2 - 100), 270, 128*2.3, 128*2.3)
        knight_hit_rect = pygame.Rect((self.screenwidth/2 - 100) + 128/1.7, 270+102, 128, 192)

        width, height = knight_select.get_size()
        scaled_knight = pygame.transform.scale(knight_select, (width*2.3, height*2.3))

        vampire_select = pygame.image.load("assets/vampire/vampire_select.png").convert()

        vampire_rect = pygame.Rect(self.screenwidth-350, 300, 128*2, 128*2)
        vampire_hit_rect = pygame.Rect((self.screenwidth-350) + 128/2, 300+64, 128, 192)

        width, height = vampire_select.get_size()
        scaled_vampire = pygame.transform.scale(vampire_select, (width*2, height*2))

        while True:

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if ninja_hit_rect.collidepoint(event.pos):
                        print("ninja")
                        return "ninja"

                    if knight_hit_rect.collidepoint(event.pos):
                        print("knight")
                        return "knight"

                    if vampire_hit_rect.collidepoint(event.pos):
                        print("vampire")
                        return "vampire"


            self.screen.fill("black")

            self.screen.blit(text, text_rect)

            self.screen.blit(scaled_ninja, ninja_rect)
            pygame.draw.rect(surface=self.screen, rect=ninja_hit_rect, color="white", width=1)

            self.screen.blit(scaled_knight, knight_rect)
            pygame.draw.rect(surface=self.screen, rect=knight_hit_rect, color="white", width=1)

            self.screen.blit(scaled_vampire, vampire_rect)
            pygame.draw.rect(surface=self.screen, rect=vampire_hit_rect, color="white", width=1)


            pygame.display.flip()



    # KI-Anfang
    # KI: Claude Code
    # Prompt: füge zu dem spiel hinzu, dass nach den charakter-auswahlen, immer ein screen kommt, um den namen des spielers einzugeben. Also: man wählt seinen charakter aus, dann muss man seinen namen eingeben. Markiere den anfang von allem, was du änderst mit "# KI-Anfang" und das ende mit "# KI-Ende"
    def enter_name(self, player: int) -> str:

        name = ""

        prompt_text = self.SV.FONT_MIDDLE.render(f"Spieler {player}: Gib deinen Namen ein", True, "dark red")
        prompt_rect = prompt_text.get_rect(center=(self.screenwidth/2, 150))

        hinweis_text = self.SV.FONT_SMALL.render("Drücke Enter zum Bestätigen", True, "dark red")
        hinweis_rect = hinweis_text.get_rect(center=(self.screenwidth/2, 700))

        input_rect = pygame.Rect(self.screenwidth/2 - 300, 400, 600, 80)

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return f"Spieler {player}"

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        if name.strip() == "":
                            return f"Spieler {player}"
                        return name

                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    elif event.unicode.isprintable() and len(name) < 15:
                        name += event.unicode

            self.screen.fill("black")

            self.screen.blit(prompt_text, prompt_rect)
            self.screen.blit(hinweis_text, hinweis_rect)

            pygame.draw.rect(surface=self.screen, rect=input_rect, color="white", width=2)

            name_text = self.SV.FONT_MIDDLE.render(name, True, "white")
            name_rect = name_text.get_rect(center=input_rect.center)
            self.screen.blit(name_text, name_rect)

            pygame.display.flip()
    # KI-Ende

    def draw_menu(self):

        neuer_kampf_text = self.SV.FONT_MIDDLE.render("Neuer Kampf", True, "dark red")
        neuer_kampf_rect = neuer_kampf_text.get_rect(center=(self.screenwidth/2, 490))

        kampf_laden_text = self.SV.FONT_MIDDLE.render("Kampf laden", True, "dark red")
        kampf_laden_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 580))

        steuerung_text = self.SV.FONT_MIDDLE.render("Steuerung", True, "dark red")
        steuerung_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 670))

        highscore_text = self.SV.FONT_MIDDLE.render("Leaderboard", True, "dark red")
        highscore_rect = highscore_text.get_rect(center=(self.screenwidth/2, 760))

        beenden_text = self.SV.FONT_MIDDLE.render("Beenden", True, "dark red")
        beenden_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 840))

        pygame.draw.rect(surface=self.screen, rect=neuer_kampf_rect, color="black")
        self.screen.blit(source=neuer_kampf_text, dest=neuer_kampf_rect)

        pygame.draw.rect(surface=self.screen, rect=kampf_laden_rect, color="black")
        self.screen.blit(source=kampf_laden_text, dest=kampf_laden_rect)

        pygame.draw.rect(surface=self.screen, rect=steuerung_rect, color="black")
        self.screen.blit(source=steuerung_text, dest=steuerung_rect)

        pygame.draw.rect(surface=self.screen, rect=beenden_rect, color="black")
        self.screen.blit(source=beenden_text, dest=beenden_rect)

        pygame.draw.rect(surface=self.screen, rect=highscore_rect, color="black")
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

        text = self.SV.FONT_BIG.render("Spieler 1", True, "dark red")
        text_rect = text.get_rect(center=(self.screenwidth / 2, 300))

        text2 = self.SV.FONT_BIG.render("Spieler 2", True, "dark red")
        text2_rect = text.get_rect(center=(self.screenwidth / 2, 400))

        zurueck = self.SV.FONT_BIG.render("Zurück", True, "dark red")
        zurueck_rect = zurueck.get_rect(center=(self.screenwidth / 2, 700))

        hintergrund = pygame.image.load("assets/steuerung_hintergrund.png").convert()

        spezialattacken = self.SV.FONT_BIG.render("Spezialattacken erklärung", True, "dark red")
        spezialattacken_rect = spezialattacken.get_rect(center=(self.screenwidth/2, 500))

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if spezialattacken_rect.collidepoint(event.pos):
                        self.spezialattacken()


            self.screen.fill("white")

            self.screen.blit(source=hintergrund, dest=(0,0))


            self.screen.blit(source=text, dest=text_rect)
            self.screen.blit(source=text2, dest=text2_rect)
            self.screen.blit(source=spezialattacken, dest=spezialattacken_rect)

            pygame.draw.rect(surface=self.screen, rect=zurueck_rect, color="black")
            self.screen.blit(source=zurueck, dest=zurueck_rect)

            pygame.display.flip()

    def laden(self, screen, SV, clock, FPS) -> tuple | str:
        try:
            dict_list: list[dict] = []
            with open("saved_game/saved_game.json", "r") as fp:
                dict_list = json.load(fp)

            player_1_dict = dict_list[0]
            player_2_dict = dict_list[1]

            if player_1_dict['special_dict']['type'] == "Ninja-Star":
                player_1 = Ninja(screen, SV.width, SV.height, 0, SV.height - 100, 128, player_1_dict['player type'], 2, FPS, clock)
                player_1.hp = player_1_dict['hp']
                player_1.xpos = player_1_dict['xpos']
                player_1.ypos -= player_1.size
                player_1.special_dict = player_1_dict['special_dict']
                player_1.name = player_1_dict['name']

            elif player_1_dict['special_dict']['type'] == "Stab":
                player_1 = Knight(screen, SV.width, SV.height, 0, SV.height - 100, 128, player_1_dict['player type'], 2, FPS, clock)
                player_1.hp = player_1_dict['hp']
                player_1.xpos = player_1_dict['xpos']
                player_1.ypos -= player_1.size

                player_1.special_dict = player_1_dict['special_dict']
                player_1.name = player_1_dict['name']

            else:
                player_1 = Vampire(screen, SV.width, SV.height, 0, SV.height - 100, 128, player_1_dict['player type'], 2, FPS, clock)
                player_1.hp = player_1_dict['hp']
                player_1.xpos = player_1_dict['xpos']
                player_1.ypos -= player_1.size

                player_1.special_dict = player_1_dict['special_dict']
                player_1.name = player_1_dict['name']

            if player_2_dict['special_dict']['type'] == "Ninja-Star":
                player_2 = Ninja(screen, SV.width, SV.height, 0, SV.height - 100, 128, player_2_dict['player type'], 2, FPS, clock)
                player_2.hp = player_2_dict['hp']
                player_2.xpos = player_2_dict['xpos']
                player_2.ypos -= player_2.size
                player_2.special_dict = player_2_dict['special_dict']
                player_2.name = player_2_dict['name']

            elif player_2_dict['special_dict']['type'] == "Stab":
                player_2 = Knight(screen, SV.width, SV.height, 0, SV.height - 100, 128, player_2_dict['player type'], 2, FPS, clock)
                player_2.hp = player_2_dict['hp']
                player_2.xpos = player_2_dict['xpos']
                player_2.ypos -= player_2.size

                player_2.special_dict = player_2_dict['special_dict']
                player_2.name = player_2_dict['name']

            else:
                player_2 = Vampire(screen, SV.width, SV.height, 0, SV.height - 100, 128, player_2_dict['player type'],
                                   2, FPS, clock)
                player_2.hp = player_2_dict['hp']
                player_2.xpos = player_2_dict['xpos']
                player_2.ypos -= player_2.size

                player_2.special_dict = player_2_dict['special_dict']
                player_2.name = player_2_dict['name']

            background = dict_list[2]

            return player_1, player_2, background

        except:
            self.error_message("Spielstand konnte nicht geladen werden!")
            return "menü"



    def steuerung_anzeigen(self, spieler):

        if spieler == 1:
            springen_text = self.SV.FONT_MIDDLE.render("W -> Springen", True, "dark red")
            springen_text_rect = springen_text.get_rect(center=(self.screenwidth / 2, 150))

            links_text = self.SV.FONT_MIDDLE.render("A -> links laufen", True, "dark red")
            links_text_rect = links_text.get_rect(center=(self.screenwidth / 2, 250))

            rechts_text = self.SV.FONT_MIDDLE.render("D -> rechts laufen", True, "dark red")
            rechts_text_rect = rechts_text.get_rect(center=(self.screenwidth / 2, 350))

            attacke_text = self.SV.FONT_MIDDLE.render("E -> normale Attacke", True, "dark red")
            attacke_text_rect = attacke_text.get_rect(center=(self.screenwidth / 2, 450))

            spezial_text = self.SV.FONT_MIDDLE.render("Q -> Spezialattacke", True, "dark red")
            spezial_text_rect = spezial_text.get_rect(center=(self.screenwidth / 2, 550))

            blocken_text = self.SV.FONT_MIDDLE.render("F -> Blocken", True, "dark red")
            blocken_text_rect = blocken_text.get_rect(center=(self.screenwidth / 2, 650))

            zurueck_text = self.SV.FONT_MIDDLE.render("Zurück", True, "dark red")
            zurueck_text_rect = zurueck_text.get_rect(center=(self.screenwidth / 2, 750))

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

                    pygame.draw.rect(surface=self.screen, rect=springen_text_rect, color="black")
                    self.screen.blit(source=springen_text, dest=springen_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=links_text_rect, color="black")
                    self.screen.blit(source=links_text, dest=links_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=rechts_text_rect, color="black")
                    self.screen.blit(source=rechts_text, dest=rechts_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=attacke_text_rect, color="black")
                    self.screen.blit(source=attacke_text, dest=attacke_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=spezial_text_rect, color="black")
                    self.screen.blit(source=spezial_text, dest=spezial_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=blocken_text_rect, color="black")
                    self.screen.blit(source=blocken_text, dest=blocken_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=zurueck_text_rect, color="black")
                    self.screen.blit(source=zurueck_text, dest=zurueck_text_rect)

                    pygame.display.update()


        elif spieler == 2:
            springen_text = self.SV.FONT_MIDDLE.render("I -> Springen", True, "dark red")
            springen_text_rect = springen_text.get_rect(center=(self.screenwidth / 2, 150))

            links_text = self.SV.FONT_MIDDLE.render("J -> links laufen", True, "dark red")
            links_text_rect = links_text.get_rect(center=(self.screenwidth / 2, 250))

            rechts_text = self.SV.FONT_MIDDLE.render("L -> rechts laufen", True, "dark red")
            rechts_text_rect = rechts_text.get_rect(center=(self.screenwidth / 2, 350))

            attacke_text = self.SV.FONT_MIDDLE.render("O -> normale Attacke", True, "dark red")
            attacke_text_rect = attacke_text.get_rect(center=(self.screenwidth / 2, 450))

            spezial_text = self.SV.FONT_MIDDLE.render("U -> Spezialattacke", True, "dark red")
            spezial_text_rect = spezial_text.get_rect(center=(self.screenwidth / 2, 550))

            blocken_text = self.SV.FONT_MIDDLE.render("M -> Blocken", True, "dark red")
            blocken_text_rect = blocken_text.get_rect(center=(self.screenwidth / 2, 650))

            zurueck_text = self.SV.FONT_MIDDLE.render("Zurück", True, "dark red")
            zurueck_text_rect = zurueck_text.get_rect(center=(self.screenwidth / 2, 750))

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


                    pygame.draw.rect(surface=self.screen, rect=springen_text_rect, color="black")
                    self.screen.blit(source=springen_text, dest=springen_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=links_text_rect, color="black")
                    self.screen.blit(source=links_text, dest=links_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=rechts_text_rect, color="black")
                    self.screen.blit(source=rechts_text, dest=rechts_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=attacke_text_rect, color="black")
                    self.screen.blit(source=attacke_text, dest=attacke_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=spezial_text_rect, color="black")
                    self.screen.blit(source=spezial_text, dest=spezial_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=blocken_text_rect, color="black")
                    self.screen.blit(source=blocken_text, dest=blocken_text_rect)

                    pygame.draw.rect(surface=self.screen, rect=zurueck_text_rect, color="black")
                    self.screen.blit(source=zurueck_text, dest=zurueck_text_rect)

                    pygame.display.update()

    def pausemenu(self, player_1, player_2, background):

        self.SV.init()

        text = self.SV.FONT_BIG.render("Weiterspielen", True, "dark red")
        text_rect = text.get_rect(center=(self.screenwidth / 2, 200))

        text2 = self.SV.FONT_BIG.render("Steuerung", True, "dark red")
        text2_rect = text2.get_rect(center=(self.screenwidth / 2, 300))

        text3 = self.SV.FONT_BIG.render("Speichern und Zurück zum Menü", True, "dark red")
        text3_rect = text3.get_rect(center=(self.screenwidth/2, 400))

        zurueck = self.SV.FONT_BIG.render("Zurück zum Menü", True, "dark red")
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

                            player_list: list = [save_player_1, save_player_2, background]

                            with open("saved_game/saved_game.json", "w") as fp:
                                json.dump(player_list, fp, indent=2)

                            print("Erfolgreich gespeichert!")
                            return "menü"

                        except:
                            print("Speichern fehlgeschlagen!")
                            self.error_message("Spiel konnte nicht gespeichert werden")
                            return "weiter"




                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if zurueck_rect.collidepoint(event.pos):
                        return "menü"

            self.screen.fill("black")

            self.screen.blit(source=text, dest=text_rect)
            self.screen.blit(source=text2, dest=text2_rect)
            self.screen.blit(source=text3, dest=text3_rect)

            pygame.draw.rect(surface=self.screen, rect=zurueck_rect, color="black")
            self.screen.blit(source=zurueck, dest=zurueck_rect)

            pygame.display.flip()

    def play_screen(self, player_1, player_2, background_filepath) -> str:
        pygame.display.set_caption("Clash Arena")
        play_map = pygame.image.load(background_filepath).convert()

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
                next_screen = self.pausemenu(player_1, player_2, background_filepath)

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

            player_1.check_special_collision(player_2)
            player_2.check_special_collision(player_1)

            if player_1.check_if_dead() == True:
                if player_2.special_dict['type'] == "Ninja-Star":
                    return player_2.name

                elif player_2.special_dict['type'] == "Stab":
                    return player_2.name

                else:
                    return player_2.name

            if player_2.check_if_dead() == True:
                if player_1.special_dict['type'] == "Ninja-Star":
                    return player_1.name

                elif player_1.special_dict['type'] == "Stab":
                    return player_1.name

                else:
                    return player_1.name

            pygame.display.flip()

            # FPS überwachen

            self.clock.tick(self.FPS)

        # PyGame sauber beenden (cleanup)

    def highscores(self, leaderboard):

        background = pygame.image.load("assets/highscore_hintergrund.png")

        zurueck_text = self.SV.FONT_MIDDLE.render("Zurück zum Menü", True, "dark red")
        zurueck_rect = zurueck_text.get_rect(center=(self.screenwidth / 2, 840))

        character_list: list = []

        # KI-Anfang
        # KI: ChatGPT
        # prompt: wie kann ich in python mit einer for-schleife durch ein dictionary gehen, und dabei die keys und values als variablen bekommen?
        for idx, (key, value) in enumerate(leaderboard.items()):

            if idx >= 5:
                break
            try:
                character_list.append((key, value))
            except:
                break
        # KI-Ende

        character_list = sort(character_list)

        while True:

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if zurueck_rect.collidepoint(event.pos):
                        return

            self.screen.fill("black")
            self.screen.blit(source=background, dest=(0,0))

            for i in range(0, len(character_list) * 100, 100):
                text = self.SV.FONT_MIDDLE.render(f"{character_list[i//100][0]}: Level {character_list[i//100][1][0]}", True, "dark red")
                text_rect = text.get_rect(center=(self.screenwidth/2, 300 +i ))
                self.screen.blit(source=text, dest=text_rect)

            self.screen.blit(source=zurueck_text, dest=zurueck_rect)



            pygame.display.flip()

    def spezialattacken(self):
        tipp = self.SV.FONT_MIDDLE.render("Tipp: Spezialattacken können nicht geblockt werden.", True, "dark red")
        tipp_rect = tipp.get_rect(center=(self.screenwidth/2, self.screenheight - 75))

        ninja = self.SV.FONT_MIDDLE.render("Ninja", True, "dark red")
        ninja_rect = ninja.get_rect(center=(self.screenwidth/2, 200))

        knight = self.SV.FONT_MIDDLE.render("Knight", True, "dark red")
        knight_rect = knight.get_rect(center=(self.screenwidth/2, 350))

        vampire = self.SV.FONT_MIDDLE.render("Vampire", True, "dark red")
        vampire_rect = vampire.get_rect(center=(self.screenwidth/2, 500))

        zurueck = self.SV.FONT_MIDDLE.render("Zurück", True, "dark red")
        zurueck_rect = zurueck.get_rect(center=(self.screenwidth / 2, 775))

        background = pygame.image.load("assets/steuerung_hintergrund.png").convert()

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "beenden"

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if ninja_rect.collidepoint(event.pos):
                        self.explain_special_attacks("Ninja-Star")

                    if knight_rect.collidepoint(event.pos):
                        self.explain_special_attacks("Stab")

                    if vampire_rect.collidepoint(event.pos):
                        self.explain_special_attacks("else")

                    if zurueck_rect.collidepoint(event.pos):
                        return ""

            self.screen.fill("black")
            self.screen.blit(source=background, dest=(0,0))

            pygame.draw.rect(surface=self.screen, rect=tipp_rect, color="black")
            self.screen.blit(tipp, tipp_rect)

            self.screen.blit(source=zurueck, dest=zurueck_rect)
            self.screen.blit(source=ninja, dest = ninja_rect)
            self.screen.blit(source=knight, dest=knight_rect)
            self.screen.blit(source=vampire, dest=vampire_rect)

            pygame.display.flip()


    def explain_special_attacks(self, type):

        zurueck = self.SV.FONT_MIDDLE.render("Zurück", True, "dark red")
        zurueck_rect = zurueck.get_rect(center=(self.screenwidth / 2, 800))

        background = pygame.image.load("assets/steuerung_hintergrund.png").convert()


        if type == "Stab":

            text = self.SV.FONT_MIDDLE.render("Ein starker Stich mit dem Schwert,", True, "dark red")
            text_rect = text.get_rect(center=(self.screenwidth / 2 + 100, 300))

            text2 = self.SV.FONT_MIDDLE.render("welcher deinem Gegner 8 Schaden zufügt.", True, "dark red")
            text2_rect = text2.get_rect(center = (self.screenwidth/2 + 100, 350))

            text3 = self.SV.FONT_MIDDLE.render("Jede Ausführung der Attacke nutzt deine Klinge ab.", True, "dark red")
            text3_rect = text3.get_rect(center=(self.screenwidth/2 + 100, 400))

            text4 = self.SV.FONT_MIDDLE.render("Diese Attacke kann maximal 8 Mal ausgeführt werden.", True, "dark red")
            text4_rect = text4.get_rect(center=(self.screenwidth/2 + 100, 450))

            image = pygame.image.load("assets/knight/sword_for_special_attack_explanation.png").convert_alpha()

        elif type == "Ninja-Star":
            text = self.SV.FONT_MIDDLE.render("Ein Wurf eines Ninja-Sternes, welcher deinem ", True, "dark red")
            text_rect = text.get_rect(center=(self.screenwidth / 2 + 100, 300))

            text2 = self.SV.FONT_MIDDLE.render("Gegner bei einem Treffer 5 Schaden zufügt.", True, "dark red")
            text2_rect = text2.get_rect(center=(self.screenwidth/2 + 100, 350))

            text3 = self.SV.FONT_MIDDLE.render("Diese Attacke kannst du maximal 10 Mal benutzen,", True, "dark red")
            text3_rect = text3.get_rect(center=(self.screenwidth / 2 + 100, 400))

            text4 = self.SV.FONT_MIDDLE.render("dann hast du keine Ninja-Sterne mehr übrig.", True, "dark red")
            text4_rect = text4.get_rect(center=(self.screenwidth/2 + 100, 450))

            image: pygame.surface.Surface = pygame.image.load("assets/ninja/ninja_star_for_special_attack_explanation.png").convert_alpha()

        else:
            text = self.SV.FONT_MIDDLE.render("Mit dieser Attacke ziehst du deinem Gegner 10 hp", True, "dark red")
            text_rect = text.get_rect(center=(self.screenwidth / 2 + 100, 300))

            text2 = self.SV.FONT_MIDDLE.render("ab und regenerierst dich um 10 hp.", True, "dark red")
            text2_rect = text2.get_rect(center=(self.screenwidth / 2 + 100, 350))

            text3 = self.SV.FONT_MIDDLE.render("Diese Attacke kannst du maximal 5 Mal benutzen,", True, "dark red")
            text3_rect = text3.get_rect(center=(self.screenwidth / 2 + 100, 400))

            text4 = self.SV.FONT_MIDDLE.render("bevor dein Blut-Level zu hoch wird", True, "dark red")
            text4_rect = text4.get_rect(center=(self.screenwidth / 2 + 100, 450))

            image: pygame.surface.Surface = pygame.image.load("assets/vampire/bat_for_special_attack_explanation.png").convert_alpha()

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "beenden"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if zurueck_rect.collidepoint(event.pos):
                        return ""

            self.screen.fill("black")
            self.screen.blit(source=background, dest=(0,0))

            pygame.draw.rect(surface=self.screen, rect=text_rect, color="black")
            pygame.draw.rect(surface=self.screen, rect=text2_rect, color="black")
            pygame.draw.rect(surface=self.screen, rect=text3_rect, color="black")
            pygame.draw.rect(surface=self.screen, rect=text4_rect, color="black")

            self.screen.blit(source=text, dest= text_rect)
            self.screen.blit(source=text2, dest = text2_rect)
            self.screen.blit(source=text3, dest=text3_rect)
            self.screen.blit(source=text4, dest=text4_rect)

            self.screen.blit(source=zurueck, dest=zurueck_rect)

            self.screen.blit(image, (0, 300))

            pygame.display.flip()


    def choose_background(self) -> str:
        text = self.SV.FONT_MIDDLE.render(f"Map:", True, "dark red")
        text_rect = text.get_rect(center=(self.screenwidth / 2, 150))

        ninja_select = pygame.image.load("assets/ninja/ninja_select.png").convert()
        ninja_rect = pygame.Rect(250, 300, 128 * 2, 128 * 2)
        width, height = ninja_select.get_size()

        ninja_hit_rect = pygame.Rect(250 + 128 / 2, 300 + 64, 128, 192)
        scaled_ninja = pygame.transform.scale(ninja_select, (width * 2, height * 2))

        knight_select = pygame.image.load("assets/knight/knight_select.png").convert()
        knight_rect = pygame.Rect((self.screenwidth / 2 - 100), 270, 128 * 2.3, 128 * 2.3)
        knight_hit_rect = pygame.Rect((self.screenwidth / 2 - 100) + 128 / 1.7, 270 + 102, 128, 192)

        width, height = knight_select.get_size()
        scaled_knight = pygame.transform.scale(knight_select, (width * 2.3, height * 2.3))

        vampire_select = pygame.image.load("assets/vampire/vampire_select.png").convert()

        vampire_rect = pygame.Rect(self.screenwidth - 350, 300, 128 * 2, 128 * 2)
        vampire_hit_rect = pygame.Rect((self.screenwidth - 350) + 128 / 2, 300 + 64, 128, 192)

        width, height = vampire_select.get_size()
        scaled_vampire = pygame.transform.scale(vampire_select, (width * 2, height * 2))

        while True:

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if ninja_hit_rect.collidepoint(event.pos):
                        print("ninja")
                        return "assets/play_map2.png"

                    if knight_hit_rect.collidepoint(event.pos):
                        print("knight")
                        return "assets/play_map.png"

                    if vampire_hit_rect.collidepoint(event.pos):
                        print("vampire")
                        return "assets/play_map3.png"

            self.screen.fill("black")

            self.screen.blit(text, text_rect)

            self.screen.blit(scaled_ninja, ninja_rect)
            pygame.draw.rect(surface=self.screen, rect=ninja_hit_rect, color="white", width=1)

            self.screen.blit(scaled_knight, knight_rect)
            pygame.draw.rect(surface=self.screen, rect=knight_hit_rect, color="white", width=1)

            self.screen.blit(scaled_vampire, vampire_rect)
            pygame.draw.rect(surface=self.screen, rect=vampire_hit_rect, color="white", width=1)

            pygame.display.flip()



    def menu(self) -> str:

        try:
            with open("leaderboard.json", "r") as fp:
                leaderboard = json.load(fp)

        except:
            pass

        neuer_kampf_text = self.SV.FONT_MIDDLE.render("Neuer Kampf", True, "dark red")
        neuer_kampf_rect = neuer_kampf_text.get_rect(center=(self.screenwidth / 2, 490))

        kampf_laden_text = self.SV.FONT_MIDDLE.render("Kampf laden", True, "dark red")
        kampf_laden_rect = kampf_laden_text.get_rect(center=(self.screenwidth / 2, 580))

        steuerung_text = self.SV.FONT_MIDDLE.render("Steuerung", True, "dark red")
        steuerung_rect = steuerung_text.get_rect(center=(self.screenwidth / 2, 670))

        highscore_text = self.SV.FONT_MIDDLE.render("Leaderboard", True, "dark red")
        highscore_rect = highscore_text.get_rect(center=(self.screenwidth / 2, 760))

        beenden_text = self.SV.FONT_MIDDLE.render("Beenden", True, "dark red")
        beenden_rect = beenden_text.get_rect(center=(self.screenwidth / 2, 840))

        hintergrund = pygame.image.load("assets/clash_arena_menu.png").convert()

        pygame.mixer.music.load("assets/title_music.mp3")
        pygame.mixer.music.play(-1)

        while True:

            # Jedes Ereignis (Event) durchgehen
            for event in pygame.event.get():

                # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte

                if event.type == pygame.QUIT:
                    return "beenden"


                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if neuer_kampf_rect.collidepoint(event.pos):
                        print("Starten gedrückt")
                        pygame.mixer.music.stop()
                        return "character select"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if kampf_laden_rect.collidepoint(event.pos):
                        print("Laden gedrückt")
                        pygame.mixer.music.stop()
                        return "laden"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if steuerung_rect.collidepoint(event.pos):
                        print("Steuerung gedrückt")
                        self.steuerung()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if highscore_rect.collidepoint(event.pos):
                        print("Highscores gedrückt")

                        try:
                            with open("leaderboard.json", "r") as fp:
                                leaderboard = json.load(fp)

                            self.highscores(leaderboard)

                        except:
                            self.error_message("Fehler: Leaderboard konnte nicht geladen werden")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # klickposition = event.pos (x, y)
                    if beenden_rect.collidepoint(event.pos):
                        print("Beenden gedrückt")
                        return "beenden"

            self.screen.fill("white")
            self.screen.blit(hintergrund, (0, 0))

            self.draw_menu()
            pygame.display.flip()