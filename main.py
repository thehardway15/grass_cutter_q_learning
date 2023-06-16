import os
import time
import numpy as np

from qagent import QLearningAgent
from episode import run_episode

from environment import Lawn, Mower
from draw import draw_stdout

if __name__ == '__main__':
    lawn_size = (10, 10)
    epsilon = 0.005
    alpha = 0.08
    gamma = 0.97
    agent = QLearningAgent(alpha, gamma, epsilon)

    episodes = 1200

    runs = []
    for i in range(episodes):
        runs.append(run_episode(agent, lawn_size, False))
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Episode: ' + str(i) + '/' + str(episodes))
        print('Average steps: ' + str(sum(runs)/len(runs)))
        print('Max steps: ' + str(max(runs)))
        print('Min steps: ' + str(min(runs)))
        print('Last steps: ' + str(runs[-1]))

    # Get the results from the asynchronous function calls
    results = [run for run in runs]


    print('Done!')

    # # Run best solution
    lawn = Lawn(lawn_size)
    mower = Mower(lawn)

    done = False
    print('Running best solution...')

    while not done:
        state = agent.calculate_state(mower, lawn)
        action = np.argmax(agent.q_table[state])
        print('Action: ' + str(action))
        new_location = mower.action(action)
        mower.update_location(new_location)
        if lawn.progress() == lawn.get_lawn_size()-1:
            done = True
        draw_stdout(lawn, mower, clear=False)

        print('Average steps: ' + str(sum(results)/len(results)))
        print('Max steps: ' + str(max(results)))
        print('Min steps: ' + str(min(results)))

        time.sleep(0.1)

        os.system('cls' if os.name == 'nt' else 'clear')
    
    print('Done!')