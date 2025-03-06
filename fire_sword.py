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

    class FireSword:
    def __init__(self):
        self.fire_column_cooldown = 5  # 5 seconds
        self.fire_rain_cooldown = 30  # 30 seconds
        self.lava_rise_cooldown = 90  # 1 1/2 minutes
        self.last_fire_column_time = 0
        self.last_fire_rain_time = 0
        self.last_lava_rise_time = 0
        self.fire_bar = 100  # Fire bar percentage (100%)
    
    def hit_player(self, target_player):
        if self.fire_bar > 0:  # Sword can only ignite if fire bar has energy
            target_player.ignite(3)  # Ignite for 3 seconds
            self.fire_bar -= 10  # Drain fire bar
            print(f"Hit {target_player.name}, they are on fire for 3 seconds!")
        else:
            print("Not enough fire energy to ignite the target.")
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.is_on_fire = False

    def ignite(self, duration):
        self.is_on_fire = True
        print(f"{self.name} is on fire!")
        pygame.time.set_timer(pygame.USEREVENT, duration * 1000)  # Fire duration timer
def craft_fire_sword(inventory):
    recipe = {
        'lava_bucket': 1,
        'iron_sword': 2,
        'flint_and_steel': 2,
        'water_potion': 2
    }

    # Check if inventory matches recipe
    for item, quantity in recipe.items():
        if inventory.get(item, 0) < quantity:
            print(f"Missing {item} to craft the Fire Sword.")
            return False

    print("Fire Sword crafted successfully!")
    return True
    class FireSword:
    def __init__(self):
        # Other attributes...
        self.fire_bar = 100  # Fire bar starts at 100%

    def recharge_in_fire(self):
        if self.fire_bar < 100:
            self.fire_bar = 100
            print("Fire Sword fully recharged in fire!")
            # Example inventory
player_inventory = {
    'lava_bucket': 1,
    'iron_sword': 2,
    'flint_and_steel': 2,
    'water_potion': 2
}

# Check crafting
if craft_fire_sword(player_inventory):
    fire_sword = FireSword()
    player = Player("Hero", (100, 100))
    target = Player("Villain", (200, 200))

    # Simulate hitting target
    fire_sword.hit_player(target)

    # Simulate recharging in fire
    fire_sword.recharge_in_fire()

    # Update display
    pygame.display.flip()

# Quit Pygame
