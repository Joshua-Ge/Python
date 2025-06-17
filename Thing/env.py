import pygame
import random
import time
import math

# Initialize Pygame
pygame.init()

# --- 1. Set up the Game Window ---
# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Learns to Collect Fruits")

# --- 2. Define Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)  # For the fruit
PURPLE = (128, 0, 128) # For the enemy

# --- 4. Game Object Classes ---
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.speed = 5
        self.score = 0
        self.image = pygame.Surface((size, size))  # Create a surface
        self.image.fill(BLUE)  # Fill with color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.last_fruit_distance = float('inf')
        self.last_enemy_distance = float('inf')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        # Keep player within bounds
        self.x = max(0, min(self.x, WIDTH - self.size))
        self.y = max(0, min(self.y, HEIGHT - self.size))
        self.rect.center = (self.x, self.y) # Update the rect

    def update(self):
        self.rect.center = (self.x, self.y)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.last_fruit_distance = float('inf')
        self.last_enemy_distance = float('inf')


class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.Surface((size, size))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def respawn(self):
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(0, HEIGHT - self.size)
        self.rect.center = (self.x, self.y)

    def update(self):
        self.rect.center = (self.x, self.y)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed=2):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed  # Allow setting different speeds
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]  # Initial random direction
        self.image = pygame.Surface((size, size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

        # Bounce off walls
        if self.x <= 0 or self.x >= WIDTH - self.size:
            self.direction[0] *= -1
        if self.y <= 0 or self.y >= HEIGHT - self.size:
            self.direction[1] *= -1
        self.rect.center = (self.x, self.y)

    def update(self):
        self.move()
        self.rect.center = (self.x, self.y)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (x, y)

# --- 5. Helper Functions ---
def calculate_distance(obj1, obj2):
    """Calculates the Euclidean distance between two objects."""
    return math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2)

def display_score(screen, font, text, score, x, y):
    """Displays the score on the screen."""
    score_text = font.render(text + str(score), True, WHITE)
    screen.blit(score_text, (x, y))

def display_message(screen, font, text, x, y, color):
    """Displays a message on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def discretize_value(value, num_bins, min_val, max_val):
    """Discretizes a continuous value into a finite number of bins."""
    if value < min_val:
        return 0
    if value > max_val:
        return num_bins - 1
    bin_size = (max_val - min_val) / num_bins
    return min(num_bins - 1, int((value - min_val) / bin_size))

# --- 6. Initialize Game Objects ---
player = Player(WIDTH // 2, HEIGHT // 2, 30)
fruit = Fruit(random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30), 20)
enemy = Enemy(random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 40), 25, speed=1.5) # Slightly slower enemy

# --- 7. Set up AI and Learning Parameters ---
LEARNING_RATE = 0.5
DISCOUNT_FACTOR = 0.9
Q_TABLE = {}  # Store Q-values. Key is the state, value is a list of Q-values for each action
VISION_RADIUS = 350  # Increased vision radius
DISTANCE_BINS = 7  # Number of bins to discretize distances
MAX_MOVES_PER_GAME = 1000
moves_left = MAX_MOVES_PER_GAME

# Possible actions (defined as changes in x, y)
ACTIONS = [(0, 0), (0, -5), (0, 5), (-5, 0), (5, 0), (-3, -3), (-3, 3), (3, -3), (3, 3)]  # Stay, Up, Down, Left, Right, Diagonals
NUM_ACTIONS = len(ACTIONS)

def get_state(player, fruit, enemy):
    """Gets the current state of the game using discretised distances."""
    fruit_distance = calculate_distance(player, fruit)
    enemy_distance = calculate_distance(player, enemy)

    fruit_distance_bin = discretize_value(fruit_distance, DISTANCE_BINS, 0, VISION_RADIUS)
    enemy_distance_bin = discretize_value(enemy_distance, DISTANCE_BINS, 0, VISION_RADIUS)

    # Consider relative positions within the vision radius
    relative_fruit_x = int((fruit.x - player.x + VISION_RADIUS) / (2 * VISION_RADIUS / 5)) if fruit_distance <= VISION_RADIUS else 5
    relative_fruit_y = int((fruit.y - player.y + VISION_RADIUS) / (2 * VISION_RADIUS / 5)) if fruit_distance <= VISION_RADIUS else 5
    relative_enemy_x = int((enemy.x - player.x + VISION_RADIUS) / (2 * VISION_RADIUS / 5)) if enemy_distance <= VISION_RADIUS else 5
    relative_enemy_y = int((enemy.y - player.y + VISION_RADIUS) / (2 * VISION_RADIUS / 5)) if enemy_distance <= VISION_RADIUS else 5

    return (fruit_distance_bin, enemy_distance_bin, relative_fruit_x, relative_fruit_y, relative_enemy_x, relative_enemy_y)

def get_q_value(state, action_index):
    """Gets the Q-value for a given state and action index."""
    if state not in Q_TABLE:
        Q_TABLE[state] = [0.0] * NUM_ACTIONS  # Initialize Q-values for all actions
    return Q_TABLE[state][action_index]

def update_q_value(state, action_index, reward, next_state):
    """Updates the Q-value based on the Bellman equation."""
    old_q_value = get_q_value(state, action_index)
    next_max_q = max(get_q_value(next_state, a) for a in range(NUM_ACTIONS))
    new_q_value = old_q_value + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_max_q - old_q_value)
    Q_TABLE[state][action_index] = new_q_value

def choose_action(state, epsilon):
    """Chooses an action based on an epsilon-greedy policy."""
    if random.random() < epsilon:  # Explore randomly
        return random.randint(0, NUM_ACTIONS - 1)
    else:  # Exploit the best action so far
        if state in Q_TABLE:
            return Q_TABLE[state].index(max(Q_TABLE[state]))
        else:
            return random.randint(0, NUM_ACTIONS - 1) # Choose randomly if state is new

# --- 8. Game Loop ---
font = pygame.font.Font(None, 30)  # For displaying text
game_over = False
epsilon = 1.0  # Exploration rate, starts high and decays
epsilon_decay = 0.95
min_epsilon = 0.05
num_games = 0
clock = pygame.time.Clock()
frame_rate = 240

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    if game_over:
        break

    if moves_left <= 0:
        player.reset(WIDTH // 2, HEIGHT // 2)
        enemy.reset(random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 40))
        num_games += 1
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        print(f"Out of Moves - Resetting. Epsilon: {epsilon:.3f}, Game: {num_games}, Score: {player.score}")
        player.score = 0
        moves_left = MAX_MOVES_PER_GAME

    # Get current state
    state = get_state(player, fruit, enemy)

    # Choose action
    action_index = choose_action(state, epsilon)
    action = ACTIONS[action_index]

    # Take action (move the player)
    player.move(action[0], action[1])
    moves_left -= 1

    # Move the enemy
    enemy.move()

    # Calculate reward
    reward = 0
    current_fruit_distance = calculate_distance(player, fruit)
    current_enemy_distance = calculate_distance(player, enemy)

    if player.rect.colliderect(fruit.rect):
        reward += 1000
        player.score += 1
        fruit.respawn()
        player.last_fruit_distance = float('inf') # Reset last fruit distance
        moves_left = MAX_MOVES_PER_GAME # Reset moves on fruit collection
    elif player.rect.colliderect(enemy.rect):
        reward -= 100
        player.reset(WIDTH // 2, HEIGHT // 2)
        enemy.reset(random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 40))
        num_games += 1
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        print(f"Collision - Resetting. Epsilon: {epsilon:.3f}, Game: {num_games}, Score: {player.score}")
        player.score = 0
        player.last_fruit_distance = float('inf')
        player.last_enemy_distance = float('inf')
        moves_left = MAX_MOVES_PER_GAME # Reset moves on collision
    else:
         #Reward based on distance to fruit
        if current_fruit_distance < player.last_fruit_distance:
            reward += 5
        elif current_fruit_distance > player.last_fruit_distance:
            reward -= 5

        # Reward based on distance to enemy (staying away is good)
        if current_enemy_distance > player.last_enemy_distance:
           reward += 0.5
        elif current_enemy_distance < player.last_enemy_distance:
            reward -= 0.5

    player.last_fruit_distance = current_fruit_distance
    player.last_enemy_distance = current_enemy_distance

    # Get new state
    next_state = get_state(player, fruit, enemy)

    # Update Q-value
    update_q_value(state, action_index, reward, next_state)

    # Draw everything
    screen.fill(BLACK)
    screen.blit(player.image, player.rect)
    screen.blit(fruit.image, fruit.rect)
    screen.blit(enemy.image, enemy.rect)
    display_score(screen, font, "Score: ", player.score, 10, 10)
    display_message(screen, font, f"Game: {num_games}", WIDTH // 2, 30, WHITE)
    display_message(screen, font, f"Epsilon: {epsilon:.2f}", 70, 50, WHITE)
    display_message(screen, font, f"Moves: {moves_left}", 70, 80, WHITE)
    pygame.display.flip()
    clock.tick(frame_rate)

# --- 9. Game Over ---
pygame.quit()