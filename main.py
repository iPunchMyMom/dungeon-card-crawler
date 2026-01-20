import pygame
from game_helpers import deal_hand

WIDTH = 900
HEIGHT = 600
SPRITE_DELAY = 500


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.font = pygame.font.SysFont("Arial", 20, True)
        pygame.display.set_caption("Dungeon Card Game")
        self.clock = pygame.Clock()
        self.cards_in_hand = deal_hand(self.screen)
        self.bg_image = pygame.image.load("./HR_Dark Gothic Castle.png").convert_alpha()
        self.bg = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT)).convert_alpha()
        self.hand_rect = pygame.Rect(0, 0, 0, 0)
        self.paused = False

    def pause_menu(self):
        dim_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dim_surface.fill((0, 0, 0, 150))
        pause_menu = pygame.Surface((600, 400), pygame.SRCALPHA)
        pause_rect = pause_menu.get_rect(center=(self.screen.width // 2, self.screen.height // 2))
        menu_text = self.font.render("Pause Menu", True, "white")
        self.screen.set_alpha(150)
        self.paused = True

        while self.paused:
            # text_surface = self.font.render("Pause Menu", True, "white")
            self.clock.tick(60)
            self.screen.blit(self.bg)
            self.cards_in_hand.draw(self.screen)
            self.screen.blit(dim_surface, (0, 0))
            pygame.draw.rect(
                dim_surface,
                (50, 50, 50, 230),
                pause_rect,
                border_radius=10,
            )
            dim_surface.blit(menu_text, (pause_rect.topleft[0] + 5, pause_rect.topleft[1] + 5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.screen.set_alpha(255)
                        self.paused = False

            pygame.display.flip()

    def run(self):
        while True:
            self.clock.tick(60)
            self.screen.fill("black")
            self.screen.blit(self.bg)

            self.cards_in_hand.update()
            self.cards_in_hand.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause_menu()

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
