import pygame

class Ninja:
    def __init__(self, screen: pygame.Surface, screenwidth, screenheight, xpos, ypos, size, player_type, damage):
        self.model = pygame.image.load("assets/ninji.png").convert()
        self.screen = screen
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        self.counter = 0

        self.punch_dict: dict = {"thrown" : False,
                            "range": 32,
                            "xpos" : 0,
                            "ypos" : 0}

        self.player_type = player_type

        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.last_direction: str = ""

        self.hp = 100
        self.damage = damage

        self.skip_next_punch = False

        self.blocking = False

        self.jumping = False

    def change_x_pos(self):
        if self.player_type == 2:
            self.xpos = self.screenwidth - self.size


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


    def check_punch_collision(self, enemy):

        if enemy.punch_dict['thrown'] == True:

            if self.skip_next_punch == False:

                if enemy.punch_dict['xpos'] <= self.xpos <= enemy.punch_dict['xpos'] + enemy.punch_dict['range']:
                    self.hp -= enemy.damage
                    self.skip_next_punch = True

                if enemy.punch_dict['xpos'] <= self.xpos + self.size <= enemy.xpos:

                    if self.blocking == True:
                        pass

                    else:
                        self.hp -= enemy.damage
                        self.skip_next_punch = True

        else:
            self.skip_next_punch = False


    def draw_healthbar(self):
        bar_length = self.hp * 2

        if self.player_type == 1:
            pygame.draw.rect(surface=self.screen, rect = (32, 32, bar_length, 32), color="red")

        elif self.player_type == 2:
            pygame.draw.rect(surface=self.screen, rect = (self.screenwidth - 232, 32, bar_length, 32), color="red")

    def check_if_dead(self) -> bool:
        if self.hp <= 0:
            return True

        else:
            return False


    def update_and_draw(self):
        self.inputs()
        self.punch()
        pygame.draw.rect(surface=self.screen, rect=(self.xpos, self.ypos, self.size, self.size), color="green", width=1)

        if self.punch_dict['thrown'] == True:
            pygame.draw.rect(surface=self.screen, rect=(self.punch_dict['xpos'], self.ypos + self.size / 4, self.punch_dict['range'], 32), color="blue")

        self.draw_healthbar()