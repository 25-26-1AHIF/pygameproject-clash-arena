import pygame
from clash_arena.src.screen_variables.screen_variables import ScreenVariables

class Vampire:
    def __init__(self, screen: pygame.Surface, screenwidth, screenheight, xpos, ypos, size, player_type, damage, fps, clock):
        self.screen = screen
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        self.counter = 0

        self.punch_dict: dict = {"thrown" : False,
                            "range": 48,
                            "xpos" : 0,
                            "ypos" : 0,
                            "width" : 48}

        self.player_type: int = player_type

        self.xpos: float = xpos
        self.ypos: float = ypos
        self.size: float = size
        self.last_direction: str = ""

        self.hp: int = 100
        self.damage: int = damage

        self.skip_next_punch: bool = False

        self.blocking: bool = False

        self.jumping: bool = False

        self.SV = ScreenVariables

        self.jump_counter: int = 0

        self.pause: bool = False

        self.fps = fps
        self.clock: pygame.time.Clock = clock
        self.special_dict: dict = {'type': "Blood-Suck",
                                   'used': False,
                                   'list' : [],
                                   'blood level': 0,
                                   'damage': 10,
                                   'ignore next': False,
                                   'counter' : 0,
                                   'range' : 48}

        self.name = ""

    def get_rect(self):
        return pygame.Rect(self.xpos, self.ypos, self.size, self.size)

    def change_x_pos(self):
        if self.player_type == 2:
            self.xpos = self.screenwidth - self.size

    def change_last_direction(self):
        if self.player_type == 1:
            self.last_direction = "right"
        elif self.player_type == 2:
            self.last_direction = "left"

    def inputs(self):

        pressed_keys = pygame.key.get_pressed()
        if self.player_type == 1:

            if pressed_keys[pygame.K_a]:
                if self.xpos <= 0:
                    pass
                else:
                    self.xpos -= 5
                    self.last_direction = "left"

            if pressed_keys[pygame.K_d]:
                if self.xpos >= self.screenwidth - self.size:
                    pass
                else:
                    self.xpos += 5
                    self.last_direction = "right"

            if pressed_keys[pygame.K_e]:
                if self.counter > 0:
                    pass
                else:
                    self.punch_dict['thrown'] = True

            if pressed_keys[pygame.K_f]:
                self.blocking = True

            else:
                self.blocking = False

            if pressed_keys[pygame.K_w]:
                if self.jumping == True:
                    pass

                else:
                    self.jumping = True
                    pygame.mixer.music.load("assets/jump_sound_effect.mp3")
                    pygame.mixer.music.play()

            if pressed_keys[pygame.K_q]:
                if self.special_dict['used'] == True:
                    pass
                elif self.special_dict['blood level'] >= 100:
                    pass
                elif self.blocking == True:
                    pass
                else:
                    self.special_dict['used'] = True


        elif self.player_type == 2:
            if pressed_keys[pygame.K_j]:
                if self.xpos <= 0:
                    pass
                else:
                    self.xpos -= 5
                    self.last_direction = "left"

            if pressed_keys[pygame.K_l]:
                if self.xpos >= self.screenwidth - self.size:
                    pass
                else:
                    self.xpos += 5
                    self.last_direction = "right"

            if pressed_keys[pygame.K_o]:
                if self.counter > 0:
                    pass
                else:
                    self.punch_dict['thrown'] = True

            if pressed_keys[pygame.K_i]:
                if self.jumping == True:
                    pass

                else:
                    self.jumping = True
                    pygame.mixer.music.load("assets/jump_sound_effect.mp3")
                    pygame.mixer.music.play()

            if pressed_keys[pygame.K_m]:
                self.blocking = True

            else:
                self.blocking = False

            if pressed_keys[pygame.K_u]:
                if self.special_dict['used'] == True:
                    pass
                elif self.special_dict['blood level'] >= 100:
                    pass
                elif self.blocking == True:
                    pass
                else:
                    self.special_dict['used'] = True


    def punch(self):
        if self.punch_dict['thrown'] == True:
             self.counter += 1

             if self.last_direction == "right":
                 self.punch_dict['xpos'] = self.xpos + self.size

             elif self.last_direction == "left":
                 self.punch_dict['xpos'] = self.xpos - self.punch_dict['range']

        else:
            return

        if self.counter == 30:
            self.counter = 0
            self.punch_dict['thrown'] = False

    def special_attack(self):
        if self.special_dict['used'] == True:
            self.special_dict['counter'] += 1

            if self.last_direction == "right":
                self.special_dict['xpos'] = self.xpos + self.size

            elif self.last_direction == "left":
                self.special_dict['xpos'] = self.xpos - self.special_dict['range']

        else:
            return

        if self.special_dict['counter'] >= 15:
            self.special_dict['counter'] = 0
            self.special_dict['used'] = False

    def check_punch_collision(self, enemy):
        if enemy.punch_dict['thrown'] == True:

            if self.skip_next_punch == False:

                # if self.blocking == False:

                punch_rect = pygame.Rect(enemy.punch_dict['xpos'], enemy.punch_dict['ypos'], enemy.punch_dict['range'],enemy.punch_dict['range'])
                player_rect = pygame.Rect(self.xpos, self.ypos, self.size, self.size)

                if punch_rect.colliderect(player_rect):
                    self.hp -= enemy.damage
                    print(f"Spieler {self.player_type} wurde getroffen")
                    self.skip_next_punch = True

        else:
            self.skip_next_punch = False

    def draw_healthbar(self):
        self.SV.init()
        bar_length = self.hp * 4

        if self.player_type == 1:
            pygame.draw.rect(surface=self.screen, rect = (132, 32, bar_length, 48), color="red")
            blood_text = self.SV.FONT_SMALL.render(f"Blutlevel: {self.special_dict['blood level']}", True,
                                                    "dark blue")

            blood_rect = blood_text.get_rect(center=(290, 100))

            self.screen.blit(source = blood_text, dest = blood_rect)

        elif self.player_type == 2:
            pygame.draw.rect(surface=self.screen, rect = (self.screenwidth - 532, 32, bar_length, 48), color="red")
            blood_text = self.SV.FONT_SMALL.render(f"BLutlevel: {self.special_dict['blood level']}", True,
                                                    "dark blue")

            blood_rect = blood_text.get_rect(center=(self.screenwidth - 375, 100))

            self.screen.blit(source = blood_text, dest = blood_rect)

    def check_if_dead(self) -> bool:
        if self.hp <= 0:
            return True

        else:
            return False

    def jump(self):
        if self.jump_counter > 80:
            self.jumping = False
            self.jump_counter = 0
            self.ypos = self.screenheight - self.size - 100

        elif 0 <= self.jump_counter <= 40:
            self.ypos -= 6

        elif self.jump_counter > 40:
            self.ypos += 6

    def check_special_collision(self, enemy):
        if enemy.special_dict['type'] == "Ninja-Star":

            if len(enemy.special_dict['list']) > 0:
                star_rect = enemy.special_dict['list'][0].get_rect()
                player_rect = self.get_rect()

                if star_rect.colliderect(player_rect):
                    self.hp -= enemy.special_dict['damage']
                    enemy.special_dict['list'] = []
                    enemy.special_dict['used'] = False

        if enemy.special_dict['type'] == "Heavy-Strike":

            if enemy.special_dict['used'] == True:

                if self.special_dict['ignore next'] == False:

                    strike_rect = pygame.Rect(enemy.special_dict['xpos'], enemy.special_dict['ypos'], enemy.special_dict['range'], enemy.special_dict['range'])
                    player_rect = self.get_rect()

                    if strike_rect.colliderect(player_rect):
                        self.hp -= enemy.special_dict['damage']
                        self.special_dict['ignore next'] = True

            else:
                self.special_dict['ignore next'] = False

        if enemy.special_dict['type'] == "Blood-Suck":

            if enemy.special_dict['used'] == True:

                if self.special_dict['ignore next'] == False:

                    strike_rect = pygame.Rect(enemy.special_dict['xpos'], enemy.special_dict['ypos'], enemy.special_dict['range'], enemy.special_dict['range'])
                    player_rect = self.get_rect()

                    if strike_rect.colliderect(player_rect):
                        self.hp -= enemy.special_dict['damage']
                        enemy.hp += enemy.special_dict['damage']

                        if enemy.hp > 100:
                            enemy.hp = 100

                        enemy.special_dict['blood level'] += 20

                        self.special_dict['ignore next'] = True

            else:
                self.special_dict['ignore next'] = False





    def update_and_draw(self) -> str|None:
        self.inputs()
        self.punch()
        rect = self.get_rect()
        pygame.draw.rect(surface=self.screen, rect=rect, color="red", width=1)

        if self.punch_dict['thrown'] == True:
            if self.last_direction == "left":
                self.punch_dict['xpos'] = self.xpos - self.punch_dict['range']
            else:
                self.punch_dict['xpos'] = self.xpos + self.size

            self.punch_dict['ypos'] = self.ypos + self.size / 4

            print()
            print(self.ypos)
            print(self.xpos)
            print(self.punch_dict['xpos'])
            print(self.punch_dict['ypos'])

            pygame.draw.rect(surface=self.screen, rect=(self.punch_dict['xpos'], self.punch_dict['ypos'], self.punch_dict['range'], self.punch_dict['width']), color="blue")

        if self.special_dict['used'] == True:
            if self.last_direction == "left":
                self.special_dict['xpos'] = self.xpos - self.special_dict['range']
            else:
                self.special_dict['xpos'] = self.xpos + self.size

            self.special_dict['ypos'] = self.ypos + self.size / 4

            pygame.draw.rect(surface=self.screen,
                            rect=(self.special_dict['xpos'], self.special_dict['ypos'], self.special_dict['range'],
                                self.special_dict['range']), color="green")

        self.draw_healthbar()

        if self.jumping == True:
            self.jump()
            self.jump_counter += 1

        self.special_attack()