class Lawn:
    def __init__(self, size):
        self.size = size
        self.lawn = [[1 for i in range(size[0])] for j in range(size[1])]
    
    def get_lawn_size(self):
        return self.size[0] * self.size[1]
    
    def progress(self):
        # sum the number of 0s in the lawn
        return sum([sum([1 for i in range(len(self.lawn[j])) if self.lawn[j][i] == 0]) for j in range(len(self.lawn))])

class Mower:
    def __init__(self, lawn):
        self.location = (0, 0)
        self.steps = 0
        self.lawn = lawn
    
    def update_location(self, location):
        # if current location not is charger location and is value 1 (grass) update to 0 (cut grass)
        self.lawn.lawn[self.location[0]][self.location[1]] = 0

        # check bounds
        if location[0] < 0 or location[0] >= self.lawn.size[0]:
            return
        if location[1] < 0 or location[1] >= self.lawn.size[1]:
            return
        
        self.location = location
    
    def get_location(self):
        return self.location

    def action(self, action):
        self.steps += 1
        # move up
        if action == 0:
            new_location = (self.location[0] - 1, self.location[1])
        # move down
        elif action == 1:
            new_location = (self.location[0] + 1, self.location[1])
        # move left
        elif action == 2:
            new_location = (self.location[0], self.location[1] - 1)
        # move right
        elif action == 3:
            new_location = (self.location[0], self.location[1] + 1)
        else:
            new_location = self.location

        return new_location