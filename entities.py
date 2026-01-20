import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, screen, x_offset, delay):
        super().__init__()
        self.screen = screen
        self.sprite_image = pygame.image.load("./card.png").convert()

        self.image = pygame.transform.scale(self.sprite_image, (150, 210))
        self.rect = self.image.get_rect(topleft=(0, 0))

        self.pos = pygame.Vector2(self.rect.center)
        self.x_offset = x_offset
        self.target_pos = pygame.Vector2(self.screen.width / 2.5 + self.x_offset, 450)

        self.moving = False
        self.delay = delay
        self.creation_time = pygame.time.get_ticks()
        self.finished_moving = False
        self.anchor_point = self.target_pos

    def deal(self):
        if self.finished_moving:
            return
        if pygame.time.get_ticks() - self.creation_time >= self.delay:
            distance = self.target_pos - self.pos
            direction = distance * 0.1
            self.pos += direction
            self.rect.center = self.pos
            if distance.x <= 1:
                self.pos = self.target_pos
                self.rect.center = self.pos
                self.finished_moving = True
