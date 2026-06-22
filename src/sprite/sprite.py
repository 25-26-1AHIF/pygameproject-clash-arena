import pygame

class Sprite:
    def __init__(self, filepath: str, image_count: int, image_rect: pygame.Rect, animation_speed):

        self.filepath = filepath
        self.image_count = image_count
        self.image_rect = image_rect
        self.images: list[pygame.Surface] = []
        self.animation_speed = animation_speed

    def load_spritesheet(self, factor: float, flip_on_x: bool):
        sprite_sheet = pygame.image.load(self.filepath).convert_alpha()

        # KI-Anfang
        # KI: ChatGPT
        # prompt: kann man in pygame eine sprite flippen, um z.B. für animation nach rechts oder nach links kein extra spritesheet zu brauchen?
        if flip_on_x == True:
            sprite_sheet = pygame.transform.flip(sprite_sheet, True, False)
        # KI-Ende

        for image_index in range(self.image_count):
            image_surface = pygame.Surface(self.image_rect.size, pygame.SRCALPHA).convert_alpha()
            image_surface.blit(sprite_sheet, (0, 0), area=pygame.Rect(image_index * self.image_rect.width,
                                                                      self.image_rect.y,
                                                                      self.image_rect.width,
                                                                      self.image_rect.height))

            width, height = image_surface.get_size()

            scaled_image = pygame.transform.scale(image_surface, (width*factor, height*factor))

            self.images.append(scaled_image)

    def draw(self, screen: pygame.Surface, xpos: float, ypos: float,
             frame_counter: int):
        screen.blit(self.images[(frame_counter // self.animation_speed) % self.image_count],
                    dest=(xpos, ypos))