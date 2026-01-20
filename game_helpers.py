import pygame
from entities import Entity


def deal_hand(
    screen,
    number_of_cards: int = 5,
    x_offset: int = 50,
    ms_to_increment: int = 250,
) -> pygame.sprite.Group:
    """Deals hand to target location, delaying each cards
    animation start time by `ms_to_increment` milliseconds"""

    bg = pygame.transform.scale(pygame.image.load("./HR_Dark Gothic Castle.png"), (900, 600))
    hand_clock = pygame.Clock()
    entities = pygame.sprite.Group()
    # hand_rect = pygame.Rect(0, 0, x_offset * (number_of_cards - 1) + 150, 0)

    for i in range(5):
        card = Entity(screen, 50 * i, i * ms_to_increment)
        entities.add(card)

    while True:
        if all(sprite.finished_moving for sprite in entities):
            return entities

        hand_clock.tick(60)
        screen.blit(bg)

        for sprite in entities:
            sprite.deal()

        entities.update()
        entities.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
