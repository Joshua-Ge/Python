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
pygame.display.set_caption("AI Learns to Collect Fruits (Speed & Score Reward)")

# --- 2. Define Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)  # For the fruit

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
        self.time_to_fruit = None
        self.start_time = None

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
        self.time_to_fruit = None
        self.start_time = None


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

def discretize_time(time_value, num_bins, max_val):
    if time_value is None:
        return num_bins - 1
    if time_value > max_val or time_value < 0:
        return num_bins - 1
    bin_size = max_val / num_bins
    return min(num_bins - 1, int(time_value / bin_size))

# --- 6. Initialize Game Objects ---
player = Player(WIDTH // 2, HEIGHT // 2, 30)
fruit = Fruit(random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30), 20)

# --- 7. Set up AI and Learning Parameters ---
LEARNING_RATE = 0.5
DISCOUNT_FACTOR = 0.9
Q_TABLE = {}  # Store Q-values. Key is the state, value is a list of Q-values for each action
VISION_RADIUS = 350  # Increased vision radius
DISTANCE_BINS = 10  # Number of bins to discretize distances
MAX_MOVES_PER_GAME = 1000
moves_left = MAX_MOVES_PER_GAME
SPEED_REWARD_MULTIPLIER = 1000000000000  # High multiplier for faster collection
SCORE_REWARD_FACTOR = 1000000000000  # Reward per collected fruit
MAX_EXPECTED_TIME = 1.0
SPEED_BINS = 5

# Possible actions (defined as changes in x, y)
ACTIONS = [(0, 0), (0, -5), (0, 5), (-5, 0), (5, 0), (-3, -3), (-3, 3), (3, -3), (3, 3)]  # Stay, Up, Down, Left, Right, Diagonals
NUM_ACTIONS = len(ACTIONS)

def get_state(player, fruit):
    """Gets the current state of the game using discretised distance."""
    fruit_distance = calculate_distance(player, fruit)
    fruit_distance_bin = discretize_value(fruit_distance, DISTANCE_BINS, 0, VISION_RADIUS)

    # Consider relative positions within the vision radius
    relative_fruit_x = int((fruit.x - player.x + VISION_RADIUS) / (2 * VISION_RADIUS / 5)) if fruit_distance <= VISION_RADIUS else 5
    relative_fruit_y = int((fruit.y - player.y + VISION_RADIUS) / (2 * VISION_RADIUS / 5)) if fruit_distance <= VISION_RADIUS else 5

    return (fruit_distance_bin, relative_fruit_x, relative_fruit_y)

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
        fruit.respawn()
        num_games += 1
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        print(f"Out of Moves - Resetting. Epsilon: {epsilon:.3f}, Game: {num_games}, Score: {player.score}")
        player.score = 0
        moves_left = MAX_MOVES_PER_GAME

    # Get current state
    state = get_state(player, fruit)

    # Choose action
    action_index = choose_action(state, epsilon)
    action = ACTIONS[action_index]

    # Take action (move the player)
    player.move(action[0], action[1])
    moves_left -= 1

    # Calculate reward
    reward = 0
    current_fruit_distance = calculate_distance(player, fruit)

    reward -= 0.001 # Small negative reward per step

    if player.rect.colliderect(fruit.rect):
        reward += 1000000 + player.score * SCORE_REWARD_FACTOR  # Additive reward based on score
        player.score += 1
        fruit.respawn()
        player.last_fruit_distance = float('inf')  # Reset last fruit distance
        moves_left = MAX_MOVES_PER_GAME  # Reset moves on fruit collection
        if player.start_time is not None:
            time_taken = time.time() - player.start_time
            # Give much more reward for collecting faster (less time) - Normalized reward
            if time_taken > 0:
                time_bin = discretize_time(time_taken, SPEED_BINS, MAX_EXPECTED_TIME)
                reward += (SPEED_BINS - 1 - time_bin) * SPEED_REWARD_MULTIPLIER  # Higher reward for lower time bin
            player.time_to_fruit = time_taken
        player.start_time = None  # Reset start time after collecting
   # else:
        # Reward based on distance to fruit
       # if current_fruit_distance < player.last_fruit_distance:
            #reward += 0.5
            #if player.start_time is None:
             #   player.start_time = time.time()
            #else:
                #reward -= 0.05  # Slightly more negative reward per step
        #elif current_fruit_distance > player.last_fruit_distance:
           # reward -= 0.25

    player.last_fruit_distance = current_fruit_distance

    # Get new state
    next_state = get_state(player, fruit)

    # Update Q-value
    update_q_value(state, action_index, reward, next_state)

    # Draw everything
    screen.fill(BLACK)
    screen.blit(player.image, player.rect)
    screen.blit(fruit.image, fruit.rect)
    display_score(screen, font, "Score: ", player.score, 10, 10)
    display_message(screen, font, f"Game: {num_games}", WIDTH // 2, 30, WHITE)
    display_message(screen, font, f"Epsilon: {epsilon:.2f}", 70, 50, WHITE)
    display_message(screen, font, f"Moves: {moves_left}", 70, 80, WHITE)
    if player.time_to_fruit is not None:
        display_message(screen, font, f"Time: {player.time_to_fruit:.2f}s", WIDTH - 150, 30, WHITE)
    pygame.display.flip()
    clock.tick(frame_rate)

# --- 9. Game Over ---
pygame.quit()

