import numpy as np

class QLearningAgent:
    def __init__(self, alpha, gamma, epsilon):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 4))
    
    def get_action(self, state):
        # epsilon greedy
        if np.random.random() < self.epsilon:
            return np.random.randint(0, 4)
        else:
            return np.argmax(self.q_table[state])
    
    def update_q_table(self, current_state, new_state, reward, action):
        # Q(s, a) = Q(s, a) + alpha * (reward + gamma * max(Q(s', a')) - Q(s, a))
        self.q_table[current_state][action] = self.q_table[current_state][action] + self.alpha * (reward + self.gamma * np.max(self.q_table[new_state]) - self.q_table[current_state][action])


    def calculate_state(self, mower, lawn):
        state = []
        state.append(self.check_lawn(mower, lawn, 'top'))
        state.append(self.check_lawn(mower, lawn, 'bottom'))
        state.append(self.check_lawn(mower, lawn, 'left'))
        state.append(self.check_lawn(mower, lawn, 'right'))
        state.append(self.check_bounds(mower, lawn, 'top'))
        state.append(self.check_bounds(mower, lawn, 'bottom'))
        state.append(self.check_bounds(mower, lawn, 'left'))
        state.append(self.check_bounds(mower, lawn, 'right'))
        state = np.array(state, dtype=int)
        return tuple(state)

    def check_bounds(self, mower, lawn, dir):
        if dir == 'top' and mower.get_location()[1] -1 < 0:
            return True
        if dir == 'bottom' and mower.get_location()[1] + 1 > lawn.size[1]:
            return True
        if dir == 'left' and mower.get_location()[0] - 1 < 0:
            return True
        if dir == 'right' and mower.get_location()[0] + 1 > lawn.size[0]:
            return True
        return False
    
    def check_lawn(self, mower, lawn, dir):
        # check if lawn has grass in the direction
        return self.calculate_grass(mower, lawn, dir) > 0

    def calculate_grass(self, mower, lawn, dir):
        # calculate value 1 on lawn 
        grass = 0
        if dir == 'top':
            y = mower.get_location()[1] - 1
            if y < 0:
                return 0
            while y >= 0:
                for x in range(lawn.size[0]):
                    if lawn.lawn[x][y] == 1:
                        grass += 1
                y -= 1
        if dir == 'bottom':
            y = mower.get_location()[1] + 1
            if y >= lawn.size[1]:
                return 0
            while y < lawn.size[1]:
                for x in range(lawn.size[0]):
                    if lawn.lawn[x][y] == 1:
                        grass += 1
                y += 1
        
        if dir == 'left':
            x = mower.get_location()[0] - 1
            if x < 0:
                return 0
            while x >= 0:
                for y in range(lawn.size[1]):
                    if lawn.lawn[x][y] == 1:
                        grass += 1
                x -= 1
        
        if dir == 'right':
            x = mower.get_location()[0] + 1
            if x > lawn.size[0]:
                return 0
            while x < lawn.size[0]:
                for y in range(lawn.size[1]):
                    if lawn.lawn[x][y] == 1:
                        grass += 1
                x += 1
        
        return grass