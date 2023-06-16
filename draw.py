import sys 
import os

def draw_stdout(lawn, mower, clear=True):
    # draw ascii the lawn with the mower's location
    lawn_draw = lawn.lawn
    lawn_draw[mower.get_location()[0]][mower.get_location()[1]] = 'M'

    output = ''
    for i in range(len(lawn_draw)):
        for j in range(len(lawn_draw[i])):
            # generate string
            output += str(lawn_draw[i][j]) + ' '
        output += '\n'
    # clear the screen
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write(output)
    # draw progress
    sys.stdout.write('Progress: ' + str(lawn.progress()) + '/' + str(lawn.get_lawn_size()-1) + '\n')
    sys.stdout.write('Steps: ' + str(mower.steps) + '\n')
    sys.stdout.flush()