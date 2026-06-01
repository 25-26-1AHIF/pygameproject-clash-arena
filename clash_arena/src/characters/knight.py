import pygame
from clash_arena.src.screen_variables.screen_variables import ScreenVariables
from clash_arena.src.sprite.sprite import Sprite


class Knight:
    def __init__(self, screen: pygame.Surface, screenwidth, screenheight, xpos, ypos, size, player_type, damage, fps,
                 clock):
        self.screen = screen
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        self.counter = 0

        self.punch_dict: dict = {"thrown": False,
                                 "range": 48,
                                 "xpos": 0,
                                 "ypos": 0,
                                 "width": 48}

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

        self.special_dict: dict = {'type': "Heavy-Strike",
                                   'used': False,
                                   'list': [],
                                   'damage': 10,
                                   'sword health': 8,
                                   'ignore next': False,
                                   'counter' : 0,
                                   'range' : 48,
                                   'xpos' : 0,
                                   'ypos': 0}

        self.name = ""

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

            if pressed_keys[pygame.K_q]:
                if self.special_dict['sword health'] <= 0:
                    pass

                elif self.special_dict['used'] == True:
                    pass

                else:
                    self.special_dict['used'] = True
                    self.special_dict['sword health'] -= 1


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

            if pressed_keys[pygame.K_m]:
                self.blocking = True

            else:
                self.blocking = False

            if pressed_keys[pygame.K_u]:
                if self.special_dict['sword health'] <= 0:
                    pass

                elif self.special_dict['used'] == True:
                    pass

                else:
                    self.special_dict['used'] = True
                    self.special_dict['sword health'] -= 1

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
                self.special_dict['xpos'] = self.xpos - self.punch_dict['range']

        else:
            return

        if self.special_dict['counter'] == 45:
            self.special_dict['counter'] = 0
            self.special_dict['used'] = False




    def check_punch_collision(self, enemy):

        if enemy.punch_dict['thrown'] == True:

            if self.skip_next_punch == False:

                if enemy.punch_dict['xpos'] <= self.xpos <= enemy.punch_dict['xpos'] + enemy.punch_dict['range'] and \
                        enemy.punch_dict['ypos'] <= self.ypos:

                    if self.blocking == True and self.last_direction == "left":
                        pass
                    else:
                        self.hp -= enemy.damage
                        self.skip_next_punch = True

                if enemy.punch_dict['xpos'] <= self.xpos + self.size <= enemy.xpos and enemy.punch_dict[
                    'ypos'] <= self.ypos:

                    if self.blocking == True and self.last_direction == "right":
                        pass

                    else:
                        self.hp -= enemy.damage
                        self.skip_next_punch = True

        else:
            self.skip_next_punch = False

    def draw_healthbar(self):
        self.SV.init()
        bar_length = self.hp * 4

        if self.player_type == 1:
            pygame.draw.rect(surface=self.screen, rect=(132, 32, bar_length, 48), color="red")
            stars_text = self.SV.FONT_SMALL.render(f"Verbleibende Sterne: {self.special_dict['stars-left']}", True,
                                                "dark blue")

            stars_rect = stars_text.get_rect(center=(290, 100))

            self.screen.blit(source=stars_text, dest=stars_rect)

        elif self.player_type == 2:
            pygame.draw.rect(surface=self.screen, rect=(self.screenwidth - 532, 32, bar_length, 48), color="red")

            stars_text = self.SV.FONT_SMALL.render(f"Haltbarkeit des Schwertes: {self.special_dict['sword health']}", True,
                                                   "dark blue")

            stars_rect = stars_text.get_rect(center=(self.screenwidth - 365, 100))

            self.screen.blit(source=stars_text, dest=stars_rect)

    def check_if_dead(self) -> bool:
        if self.hp <= 0:
            return True

        else:
            return False

    def jump(self):
        if self.jump_counter > 100:
            self.jumping = False
            self.jump_counter = 0
            self.ypos = self.screenheight - self.size - 100

        elif 0 <= self.jump_counter <= 50:
            self.ypos -= 5

        elif self.jump_counter > 50:
            self.ypos += 5

    def check_special_collision(self, special_dict):
        if special_dict['type'] == "Ninja-Star":

            if len(special_dict['list']) > 0:
                if self.xpos <= special_dict['list'][0].xpos <= self.xpos + self.size or special_dict['list'][
                    0].xpos <= self.xpos <= special_dict['list'][0].xpos + special_dict['list'][0].size:

                    if self.ypos <= special_dict['list'][0].ypos <= self.ypos + self.size:

                        if self.special_dict['ignore next'] == False:
                            self.hp -= special_dict['damage']

                            self.special_dict['ignore next'] = True

                else:
                    self.special_dict['ignore next'] = False

    def update_and_draw(self, enemy) -> str | None:
        self.inputs()
        self.punch()
        pygame.draw.rect(surface=self.screen, rect=(self.xpos, self.ypos, self.size, self.size), color="red", width=1)

        if self.punch_dict['thrown'] == True:
            pygame.draw.rect(surface=self.screen,
                             rect=(self.punch_dict['xpos'], self.ypos + self.size / 4, self.punch_dict['range'],
                                   self.punch_dict['width']), color="blue")

        if self.special_dict['used'] == True:
            pygame.draw.rect(surface=self.screen,
                             rect=(self.special_dict['xpos'], self.ypos + self.size / 4, self.special_dict['range'],
                                   self.special_dict['range']), color="blue")

        self.draw_healthbar()

        if self.jumping == True:
            self.jump()
            self.jump_counter += 1

        self.special_attack()