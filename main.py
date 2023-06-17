import os
import pickle
import time
import sys
import numpy as np

import config

from qagent import QLearningAgent
from episode import run_episode

from environment import Lawn, Mower
from draw import draw_stdout

if __name__ == '__main__':
    lawn_size = config.LAWN_SIZE 
    epsilon = config.EPSILON
    alpha = config.ALPHA
    gamma = config.GAMMA
    agent = QLearningAgent(alpha, gamma, epsilon)

    run_pickle = sys.argv[1] if len(sys.argv) > 1 else None

    if run_pickle:
        print('Loading pickle...')
        with open(f'pickle/{run_pickle}.pickle', 'rb') as f:
            agent.q_table = pickle.load(f)

    if not run_pickle:
        episodes = config.EPISODES

        runs = []
        for i in range(episodes):
            runs.append(run_episode(agent, lawn_size, False))
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Episode: ' + str(i) + '/' + str(episodes))
            print('Average steps: ' + str(sum(runs)/len(runs)))
            print('Max steps: ' + str(max(runs)))
            print('Min steps: ' + str(min(runs)))
            print('Last steps: ' + str(runs[-1]))
            if i % config.PICKLE_STEP == 0:
                with open(f'pickle/{i}.pickle', 'wb') as f:
                    pickle.dump(agent.q_table, f)

        # Save the final q_table
        with open(f'pickle/{episodes}.pickle', 'wb') as f:
            pickle.dump(agent.q_table, f)

        # Get the results from the asynchronous function calls
        results = [run for run in runs]


        print('Done!')

    # # Run best solution
    lawn = Lawn(lawn_size)
    mower = Mower(lawn)

    done = False
    print('Running solution...')

    while not done:
        state = agent.calculate_state(mower, lawn)
        action = np.argmax(agent.q_table[state])
        print('Action: ' + str(action))
        new_location = mower.action(action)
        mower.update_location(new_location)
        if lawn.progress() == lawn.get_lawn_size()-1:
            done = True
        draw_stdout(lawn, mower, clear=False)

        time.sleep(0.1)

        os.system('cls' if os.name == 'nt' else 'clear')
    
    print('Done!')