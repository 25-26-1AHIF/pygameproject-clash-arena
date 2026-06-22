import pygame
from clash_arena.src.screen_variables.screen_variables import ScreenVariables
from clash_arena.src.sprite.sprite import Sprite


class Knight:
    def __init__(self, screen: pygame.Surface, screenwidth, screenheight, xpos, ypos, size, player_type, damage, fps, clock):
        self.screen = screen
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        self.counter = 0
        self.ignore = False

        self.punch_dict: dict = {"thrown" : False,
                            "range": 48,
                            "xpos" : 0,
                            "ypos" : 0}

        self.player_type: int = player_type

        self.xpos: float = xpos
        self.ypos: float = ypos
        self.size: float = size * 2.5
        self.last_direction: str = ""

        self.hit_rect = pygame.Rect(self.xpos + 128 / 2, self.ypos + 64, 128, 192)


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
        self.special_dict: dict = {'type': "Stab",
                                   'used': False,
                                   'list' : [],
                                   'durability': 8,
                                   'damage': 8,
                                   'ignore next': False,
                                   'xpos' : 0,
                                   'ypos' : 0,
                                   'range' : 48,
                                   'counter' : 0}

        self.ult = False
        self.ult_counter = 0
        self.ult_bar = 0
        self.name = ""

        self.jump_sound = pygame.mixer.Sound("assets/jump_sound_effect.mp3")
        self.punch_sound = pygame.mixer.Sound("assets/knight/knight_punch_sound_effect.mp3")
        self.special_sound_effect = pygame.mixer.Sound("assets/knight/heavy_strike_sound_effect.mp3")


        self.walk_right_animation = Sprite(filepath="assets/knight/walk.png", image_count=7,
                                           image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.walk_right_animation.load_spritesheet(2.5, False)

        self.walk_left_animation = Sprite(filepath="assets/knight/walk.png", image_count=7,
                                          image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.walk_left_animation.load_spritesheet(2.5, True)


        self.idle_right_animation = Sprite(filepath="assets/knight/idle.png", image_count=4,
                                           image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.idle_right_animation.load_spritesheet(2.5, False)

        self.idle_left_animation = Sprite(filepath="assets/knight/idle.png", image_count=4,
                                          image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.idle_left_animation.load_spritesheet(2.5, True)


        self.punch_right_animation = Sprite(filepath="assets/knight/attack.png", image_count=5,
                                            image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.punch_right_animation.load_spritesheet(2.5, False)

        self.punch_left_animation = Sprite(filepath="assets/knight/attack.png", image_count=5,
                                           image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.punch_left_animation.load_spritesheet(2.5, True)


        self.block_right_animation = Sprite(filepath="assets/knight/block.png", image_count=5,
                                            image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.block_right_animation.load_spritesheet(2.5, False)

        self.block_left_animation = Sprite(filepath="assets/knight/block.png", image_count=5,
                                           image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.block_left_animation.load_spritesheet(2.5, True)


        self.jump_right_animation = Sprite(filepath="assets/knight/jump.png", image_count=6,
                                           image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.jump_right_animation.load_spritesheet(2.5, False)

        self.jump_left_animation = Sprite(filepath="assets/knight/jump.png", image_count=6,
                                          image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=6)
        self.jump_left_animation.load_spritesheet(2.5, True)


        self.special_left_animation = Sprite(filepath="assets/knight/special.png", image_count=4,
                                             image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=4)
        self.special_left_animation.load_spritesheet(2.5, True)

        self.special_right_animation = Sprite(filepath="assets/knight/special.png", image_count=4,
                                              image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=4)
        self.special_right_animation.load_spritesheet(2.5, False)

        self.punch_right_fire_animation = Sprite(filepath="assets/knight/attack_feuer_mode.png", image_count=5,
                                                 image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=4)
        self.punch_right_fire_animation.load_spritesheet(2.5, False)

        self.punch_left_fire_animation = Sprite(filepath="assets/knight/attack_feuer_mode.png", image_count=5,
                                                image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=4)
        self.punch_left_fire_animation.load_spritesheet(2.5, True)

        self.blitz = Sprite(filepath="assets/knight/blitz.png", image_count=5,
                            image_rect=pygame.Rect(0, 0, 256, 512), animation_speed=8)
        self.blitz.load_spritesheet(1, False)

        self.charge = Sprite(filepath="assets/knight/attack_blitz_charge.png", image_count=5,
                             image_rect=pygame.Rect(0, 0, 128, 128), animation_speed=8)
        self.charge.load_spritesheet(2.5, False)

        self.frame_counter = 0

        self.animation_playing = ""


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

            if pressed_keys[pygame.K_f]:
                self.blocking = True

            else:
                self.blocking = False

            if pressed_keys[pygame.K_a]:
                if self.xpos <= 0:
                    pass
                elif self.blocking == True:
                    pass
                else:

                    self.xpos -= 7
                    self.last_direction = "left"

                    if self.animation_playing != "walking left":
                        self.frame_counter = 0
                    self.animation_playing = "walking left"

            elif pressed_keys[pygame.K_d]:
                if self.xpos >= self.screenwidth - self.size:
                    pass
                elif self.blocking == True:
                    pass
                else:
                    self.xpos += 7
                    self.last_direction = "right"

                    if self.animation_playing != "walking right":
                        self.frame_counter = 0
                    self.animation_playing = "walking right"

            elif pressed_keys[pygame.K_e]:
                if self.counter > 0:
                    pass
                elif self.blocking == True:
                    pass
                else:
                    self.punch_dict['thrown'] = True
                    self.punch_sound.play()
                    self.frame_counter = 0


            elif pressed_keys[pygame.K_w]:
                if self.jumping == True:
                    pass

                else:
                    self.jumping = True
                    self.jump_sound.play()
                    self.frame_counter = 0
                    self.animation_playing = "jump"

            elif pressed_keys[pygame.K_s]:

                if self.blocking == True:
                    pass
                elif self.ult_bar < 100:
                    pass
                else:
                    self.ult = True
                    self.ult_bar = 0

            elif pressed_keys[pygame.K_q]:
                if self.special_dict['used'] == True:
                    pass
                elif self.special_dict['counter'] > 0:
                    pass
                elif self.blocking == True:
                    pass
                elif self.special_dict['durability'] <= 0:
                    pass
                else:
                    self.special_dict['used'] = True
                    self.special_dict['durability'] -= 1
                    self.special_sound_effect.play()
                    self.frame_counter = 0


            else:
                if self.animation_playing != "idle":
                    self.frame_counter = 0
                self.animation_playing = "idle"

        elif self.player_type == 2:

            if pressed_keys[pygame.K_m]:
                self.blocking = True

            else:
                self.blocking = False

            if pressed_keys[pygame.K_j]:
                if self.xpos <= 0:
                    pass
                elif self.blocking == True:
                    pass
                else:
                    self.xpos -= 7
                    self.last_direction = "left"

                    if self.animation_playing != "walking left":
                        self.frame_counter = 0
                    self.animation_playing = "walking left"

            elif pressed_keys[pygame.K_l]:
                if self.xpos >= self.screenwidth - self.size:
                    pass
                elif self.blocking == True:
                    pass
                else:
                    self.xpos += 7
                    self.last_direction = "right"

                    if self.animation_playing != "walking right":
                        self.frame_counter = 0
                    self.animation_playing = "walking right"

            elif pressed_keys[pygame.K_o]:
                if self.counter > 0:
                    pass
                elif self.blocking == True:
                    pass
                else:
                    self.punch_dict['thrown'] = True
                    self.punch_sound.play()

            elif pressed_keys[pygame.K_i]:
                if self.jumping == True:
                    pass

                else:
                    self.jumping = True
                    self.jump_sound.play()

            elif pressed_keys[pygame.K_k]:

                if self.blocking == True:
                    pass
                elif self.ult_bar < 100:
                    pass
                else:
                    self.ult = True
                    self.ult_bar = 0

            elif pressed_keys[pygame.K_u]:
                if self.special_dict['used'] == True:
                    pass
                elif self.special_dict['counter'] > 0:
                    pass
                elif self.blocking == True:
                    pass
                elif self.special_dict['durability'] <= 0:
                    pass
                else:
                    self.special_dict['used'] = True
                    self.special_dict['durability'] -= 1
                    self.special_sound_effect.play()
                    self.frame_counter = 0

            else:
                if self.animation_playing != "idle":
                    self.frame_counter = 0
                self.animation_playing = "idle"


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
                 self.special_dict['xpos'] = self.xpos + 128

             elif self.last_direction == "left":
                 self.special_dict['xpos'] = self.xpos + 128 + 16

        else:
            return

        if self.special_dict['counter'] == 50:
            self.special_dict['counter'] = 0
            self.special_dict['used'] = False

    def check_punch_collision(self, enemy):
        if enemy.punch_dict['thrown'] == True:

            if self.skip_next_punch == False:

                if self.blocking == False:

                    punch_rect = pygame.Rect(enemy.punch_dict['xpos'], enemy.punch_dict['ypos'], enemy.punch_dict['range'],enemy.punch_dict['range'])
                    #pygame.draw.rect(surface=self.screen, rect=self.hit_rect, color="white", width=1)

                    if punch_rect.colliderect(self.hit_rect):
                        self.hp -= enemy.damage
                        self.skip_next_punch = True
                        if enemy.ult_bar < 100:
                            enemy.ult_bar += 5
        else:
            self.skip_next_punch = False

    def draw_healthbar(self):
        self.SV.init()
        bar_length = self.hp * 4

        if self.player_type == 1:
            pygame.draw.rect(surface=self.screen, rect = (132, 32, bar_length, 48), color="red")
            pygame.draw.rect(surface=self.screen, rect=(132, 132, self.ult_bar * 4, 48), color="blue")
            name = self.SV.FONT_MIDDLE.render(f"{self.name}", True, "white")
            ult_text = self.SV.FONT_SMALL.render(f"ULT: {self.ult_bar}%", True, "white")
            self.screen.blit(ult_text, (132, 128))
            self.screen.blit(name, (128, 28))
            stars_text = self.SV.FONT_SMALL.render(f"Haltbarkeit des Schwertes: {self.special_dict['durability']}", True,
                                                    "dark red")
            stars_rect = stars_text.get_rect(center=(290, 100))

            self.screen.blit(source = stars_text, dest = stars_rect)

        elif self.player_type == 2:
            pygame.draw.rect(surface=self.screen, rect = (self.screenwidth - 532, 32, bar_length, 48), color="red")
            pygame.draw.rect(surface=self.screen, rect=(self.screenwidth-532, 132, self.ult_bar * 4, 48), color="blue")
            name = self.SV.FONT_MIDDLE.render(f"{self.name}", True, "white")
            self.screen.blit(name, (self.screenwidth - 532, 28))
            ult_text = self.SV.FONT_SMALL.render(f"ULT: {self.ult_bar}%", True, "white")
            self.screen.blit(ult_text, (self.screenwidth - 532, 128))
            stars_text = self.SV.FONT_SMALL.render(f"Haltbarkeit des Schwertes: {self.special_dict['durability']}", True,
                                                    "dark red")

            stars_rect = stars_text.get_rect(center=(self.screenwidth - 375, 100))

            self.screen.blit(source = stars_text, dest = stars_rect)

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

                if star_rect.colliderect(self.hit_rect):
                    self.hp -= enemy.special_dict['damage']
                    enemy.special_dict['list'] = []
                    enemy.special_dict['used'] = False

        if enemy.special_dict['type'] == "Stab":
            if enemy.special_dict['used'] == True:

                if self.special_dict['ignore next'] == False:

                    strike_rect = pygame.Rect(enemy.special_dict['xpos'], enemy.special_dict['ypos'], enemy.special_dict['range'], enemy.special_dict['range'])

                    if strike_rect.colliderect(self.hit_rect):
                        self.hp -= enemy.special_dict['damage']
                        self.special_dict['ignore next'] = True

            else:
                self.special_dict['ignore next'] = False

        if enemy.special_dict['type'] == "Blood-Suck":

            if enemy.special_dict['used'] == True:

                if self.special_dict['ignore next'] == False:

                    strike_rect = pygame.Rect(enemy.special_dict['xpos'], enemy.special_dict['ypos'], enemy.special_dict['range'], enemy.special_dict['range'])

                    if strike_rect.colliderect(self.hit_rect):
                        self.hp -= enemy.special_dict['damage']
                        enemy.hp += enemy.special_dict['damage']

                        if enemy.hp > 100:
                            enemy.hp = 100

                        enemy.special_dict['blood level'] += 20

                        self.special_dict['ignore next'] = True

            else:
                self.special_dict['ignore next'] = False

    def update_and_draw(self, enemy) -> str|None:
        self.inputs()
        self.punch()

        if self.ult == True:

            self.damage = 8
            self.ult_bar = 0
            if self.ult_counter <= 60:
                self.charge.draw(self.screen, self.xpos, self.ypos, self.frame_counter)
                self.blitz.draw(self.screen, self.xpos - 64, self.ypos - 332, self.frame_counter)
                self.ult_counter += 1

            elif self.ult_counter >= 180:
                self.ult = False
                self.ult_counter = 0
                self.ignore = False

            else:
                self.ult_counter += 1

        else:
            if self.ignore == False:
                self.damage = 2
                self.ignore = True

        if self.ult == True:
            punch_right_animation = self.punch_right_fire_animation
            punch_left_animation = self.punch_left_fire_animation
        else:
            punch_right_animation = self.punch_right_animation
            punch_left_animation = self.punch_left_animation

        if 0 < self.ult_counter <= 60:
            pass

        elif self.punch_dict['thrown'] == True and self.last_direction == "right":
            punch_right_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.punch_dict['thrown'] == True and self.last_direction == "left":
            punch_left_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.blocking == True and self.last_direction == "right":
            self.block_right_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.blocking == True and self.last_direction == "left":
            self.block_left_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.jumping == True and self.last_direction == "right":
            self.jump_right_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.jumping == True and self.last_direction == "left":
            self.jump_left_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.special_dict['used'] == True and self.last_direction == "right":
            self.special_right_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.special_dict['used'] == True and self.last_direction == "left":
            self.special_left_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.animation_playing == "walking right":
            self.walk_right_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        elif self.animation_playing == "walking left":
            self.walk_left_animation.draw(self.screen, self.xpos, self.ypos, self.frame_counter)

        elif self.animation_playing == "idle" and self.last_direction == "right":
            self.idle_right_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        else:
            self.idle_left_animation.draw(self.screen, self.xpos, self.ypos, frame_counter=self.frame_counter)

        #pygame.draw.rect(surface=self.screen, rect=rect, color="red", width=1)


        if self.last_direction == "right":
            self.hit_rect = pygame.Rect(self.xpos, self.ypos + 128, 128, 192)

        elif self.last_direction == "left":
            self.hit_rect = pygame.Rect(self.xpos + 192, self.ypos + 128, 128, 192)


        if self.punch_dict['thrown'] == True:
            if self.last_direction == "left":
                self.punch_dict['xpos'] = self.xpos + 128 + 16
            else:
                self.punch_dict['xpos'] = self.xpos + 128

            self.punch_dict['ypos'] = self.ypos + self.size / 4 + 96

            #pygame.draw.rect(surface=self.screen, rect=(self.punch_dict['xpos'], self.punch_dict['ypos'], self.punch_dict['range'], self.punch_dict['range']), color="blue")


        if self.special_dict['used'] == True:
            if self.last_direction == "left":
                self.special_dict['xpos'] = self.xpos + 128 + 16
            else:
                self.special_dict['xpos'] = self.xpos + 128

            self.special_dict['ypos'] = self.ypos + self.size / 4 + 96


            # pygame.draw.rect(surface=self.screen, rect=(self.special_dict['xpos'], self.special_dict['ypos'], self.special_dict['range'], self.special_dict['range']), color="green")

        self.draw_healthbar()

        if self.jumping == True:
            self.jump()
            self.jump_counter += 1



        self.special_attack()
        self.frame_counter += 1