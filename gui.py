import pygame
import sys
import pickle
import numpy as np

import config

from environment import Lawn, Mower
from qagent import QLearningAgent

pygame.init()

epsilon = config.EPSILON
alpha = config.ALPHA
gamma = config.GAMMA
agent = QLearningAgent(alpha, gamma, epsilon)

lawn_size = config.LAWN_SIZE

run_pickle = sys.argv[1] if len(sys.argv) > 1 else None

if run_pickle:
    print('Loading pickle...')
    with open(f'pickle/{run_pickle}.pickle', 'rb') as f:
        agent.q_table = pickle.load(f)
else:
    print('No pickle file specified')
    exit()

# Screen setup
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Lawn Mower')

# Colors
dark_green = (34, 139, 34)
light_green = (0, 255, 0)
red = (255, 0, 0)

# Setup game
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30)
running = True

block_size = int(screen_width / lawn_size[0])

lawn = Lawn(lawn_size)
mower = Mower(lawn)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    # draw lawn
    for i in range(lawn_size[0]):
        for j in range(lawn_size[1]):
            color = dark_green if lawn.lawn[i][j] else light_green
            pygame.draw.rect(screen, color, (i * block_size, j * block_size, block_size, block_size))
        
    # draw mower
    pygame.draw.rect(screen, red, (mower.x * block_size, mower.y * block_size, block_size, block_size))

    state = agent.calculate_state(mower, lawn)
    action = np.argmax(agent.q_table[state])
    new_location = mower.action(action)
    mower.update_location(new_location)

    if lawn.lanw_cuted():
        running = False

    pygame.display.flip()
    clock.tick(60)

# wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()