import time 

from environment import Lawn, Mower
from draw import draw_stdout

def run_episode(agent, lawn_size, draw=False, delay=0.01):
    done = False
    lawn = Lawn(lawn_size)
    mower = Mower(lawn)

    while not done:
        current_state = agent.calculate_state(mower, lawn)
        action = agent.get_action(current_state)
        new_location = mower.action(action)

        reward = 0
        # check if done
        if new_location[0] < 0 or new_location[1] < 0:
            done = True
            reward = -1000
        
        if new_location[0] >= lawn.size[0] or new_location[1] >= lawn.size[1]:
            done = True
            reward = -1000

        if lawn.lanw_cuted():
            done = True
            reward = 1000
        
        if mower.steps > lawn.get_lawn_size() * 10:
            done = True
            reward = -10000
        
        if not done:
            # check lawn state at new location
            if lawn.lawn[new_location[0]][new_location[1]] == 1:
                reward = 10
            # elif lawn.lawn[new_location[0]][new_location[1]] == 0:
                # reward = -2
            else:
                reward = 0

            if mower.steps > lawn.get_lawn_size() * 4:
                reward -= 100

        # update location
        mower.update_location(new_location)
        next_state = agent.calculate_state(mower, lawn)

        # update q table
        agent.update_q_table(current_state, next_state, reward, action)
        
        # draw
        if draw:
            draw_stdout(lawn, mower)
            time.sleep(delay)
        
    return mower.steps
