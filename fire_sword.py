class FireSword:
    def __init__(self):
        self.fire_column_cooldown = 5  # 5 seconds
        self.fire_rain_cooldown = 30  # 30 seconds
        self.lava_rise_cooldown = 90  # 1 1/2 minute
        self.last_fire_column_time = 0
        self.last_fire_rain_time = 0
        self.last_lava_rise_time = 0

    def shoot_fire_column(self, player):
        current_time = time.time()
        if current_time - self.last_fire_column_time >= self.fire_column_cooldown:
            # Logic to shoot fire column
            print(f"Fire column shot at position {player.position}")
            self.last_fire_column_time = current_time

    def rain_fire(self):
        current_time = time.time()
        if current_time - self.last_fire_rain_time >= self.fire_rain_cooldown:
            # Logic to rain fire for 10 seconds
            print("Fire raining for 10 seconds")
            time.sleep(10)
            self.last_fire_rain_time = current_time

    def rise_lava(self, lava_source):
        current_time = time.time()
        if current_time - self.last_lava_rise_time >= self.lava_rise_cooldown:
            # Logic to make lava rise
            print(f"Lava rising at source {lava_source}")
            self.last_lava_rise_time = current_time

class Player:
    def __init__(self, position):
        self.position = position

# Example usage
sword = FireSword()
player = Player((100, 100))
lava_source = (200, 200)

# Shooting fire column
sword.shoot_fire_column(player)

# Raining fire
sword.rain_fire()

# Making lava rise
sword.rise_lava(lava_source)

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the texture
texture = pygame.image.load('texture.png')

class FireSword:
    def __init__(self):
        self.fire_column_cooldown = 5  # 5 seconds
        self.fire_rain_cooldown = 30  # 30 seconds
        self.lava_rise_cooldown = 90  # 1 1/2 minute
        self.last_fire_column_time = 0
        self.last_fire_rain_time = 0
        self.last_lava_rise_time = 0

    def shoot_fire_column(self, player):
        current_time = time.time()
        if current_time - self.last_fire_column_time >= self.fire_column_cooldown:
            # Logic to shoot fire column
            print(f"Fire column shot at position {player.position}")
            self.last_fire_column_time = current_time

    def rain_fire(self):
        current_time = time.time()
        if current_time - self.last_fire_rain_time >= self.fire_rain_cooldown:
            # Logic to rain fire for 10 seconds
            print("Fire raining for 10 seconds")
            time.sleep(10)
            self.last_fire_rain_time = current_time

    def rise_lava(self, lava_source):
        current_time = time.time()
        if current_time - self.last_lava_rise_time >= self.lava_rise_cooldown:
            # Logic to make lava rise
            print(f"Lava rising at source {lava_source}")
            self.last_lava_rise_time = current_time

class Player:
    def __init__(self, position):
        self.position = position

    def draw(self):
        # Draw the texture on the player's position
        screen.blit(texture, self.position)

# Example usage
sword = FireSword()
player = Player((100, 100))
lava_source = (200, 200)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw player with texture
    player.draw()

    # Update display
    pygame.display.flip()

# Quit Pygame
