import pygame

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Delay between each sprite animation start (in milliseconds)
SPRITE_DELAY = 500  # 0.5 seconds


# --- Sprite Class ---
class DelayedSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, position, start_delay_ms):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 100))
        self.start_delay_ms = start_delay_ms
        self.is_animating = False
        self.start_time = None  # To be set after game initializes
        self.target_pos = (500, 500)
        self.pos = (0, 0)

    def start_animation(self, current_time):
        """Sets the start time reference for the sprite's delay."""
        self.start_time = current_time

    def update(self, current_time):
        if not self.is_animating:
            # Check if enough time has passed since the start time reference
            if current_time - self.start_time >= self.start_delay_ms:
                self.is_animating = True
                # Optional: Start actual animation logic here (e.g., changing frames, movement)
                print(f"Sprite at {self.rect.center} starting animation!")

        if self.is_animating:
            # Add your actual animation logic here (e.g., self.rect.x += speed)
            direction = self.target_pos - self.pos
            self.pos += direction * 0.1
            self.rect.center = self.pos


# --- Main Game Loop ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Delayed Sprite Animations")
    clock = pygame.time.Clock()

    # Create 5 sprites with cumulative delays
    all_sprites = pygame.sprite.Group()
    for i in range(5):
        # Calculate cumulative delay: 0ms, 500ms, 1000ms, 1500ms, 2000ms
        delay = i * SPRITE_DELAY
        # Position them horizontally
        pos_x = 100 + i * 150
        sprite = DelayedSprite("./card.png", (pos_x, SCREEN_HEIGHT // 2), delay)
        all_sprites.add(sprite)

    running = True
    # Record the initial time *after* Pygame has initialized
    initial_start_time = pygame.time.get_ticks()

    # Tell each sprite what time to reference for its delay calculation
    for sprite in all_sprites:
        sprite.start_animation(initial_start_time)

    while running:
        # Get the current time for the update loop
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update sprites, passing the current time
        all_sprites.update(current_time)

        # Drawing
        screen.fill((30, 30, 30))  # Fill with dark gray
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    # You must replace 'my_sprite_image.png' with an actual valid image file path.
    # If you don't have one, the code will raise an error.
    main()
