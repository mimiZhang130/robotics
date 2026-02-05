# General Notes: I think this works (if i did the math in my head right). Maybe add more validation for the inputs and stuff 
# so that like numbers outside of the accpetable range can't be inputed? Otherwise hopefully this works 

from asn2_tripod import tripodCycle
from asn2_turn_left import turnLeft90
from asn2_turn_right import turnRight90
from asn2_turn_180 import turn180

# Importing set directions (k) and map
from asn2_grpA import DIRECTION, CSME301Map

# Move forward one cell block (center-to-center)
cycles_per_cell = 6
def forwardCell(hipAdjust = [0, 0, 0, 0, 0, 0]):
    for i in range(cycles_per_cell):
        tripodCycle(hipAdjusts=hipAdjust)

# Updating heading when turning
def kRight(k):
    # North(1)->East(2), East(2)->South(3), etc
    if k == DIRECTION.North:
        return DIRECTION.East
    elif k == DIRECTION.East:
        return DIRECTION.South
    elif k == DIRECTION.South:
        return DIRECTION.West
    elif k == DIRECTION.West:
        return DIRECTION.North

def kLeft(k):
    # North(1)->West(4), West(4)->South(3), etc
    if k == DIRECTION.North:
        return DIRECTION.West
    elif k == DIRECTION.West:
        return DIRECTION.South
    elif k == DIRECTION.South:
        return DIRECTION.East
    elif k == DIRECTION.East:
        return DIRECTION.North
    
def deltaPos(k):
    # i+ when going down, j+ going right. Top left is (0,0)
    if k == DIRECTION.North:
        return (-1, 0)
    elif k == DIRECTION.East:
        return (0, 1)
    elif k == DIRECTION.South:
        return (1, 0)
    elif k == DIRECTION.West:
        return (0, -1)
    
def execMotion(frame, action):
    # Dict input for frame = {'i': int, 'j':int, k: one of the four directions}
    # String input for action = 'F', 'L', 'R', 'B' (Fowards, Left, Right, Backwards)

    action = action.upper() # in case someone types lowercase

    # Performs the movements and updates internal tracker (I think this works?)
    if action == 'F':
        forwardCell()
        di, dj = deltaPos(frame['k'])
        frame['i'] += di
        frame['j'] += dj
    elif action == 'R':
        # When turning we dont actually move anywhere so the i and j doesn't change
        # Heading is the only thing that changes
        turnRight90()
        frame['k'] = kRight(frame['k'])

    elif action == 'L':
        turnLeft90()
        frame['k'] = kLeft(frame['k'])

    elif action == "B":
        turn180()
        frame['k'] = kRight(kRight(frame['k']))

    return frame

def userInput(prompt):
    # Inputs the string as 0 0 1 for example
    raw_str = input(prompt)
    parts = raw_str.split()

    i = int(parts[0])
    j = int(parts[1])
    k = int(parts[2])

    return {'i': i, 'j': j, 'k':k}

def directionNames(k):
    if k == DIRECTION.North:
        return 'North'
    elif k == DIRECTION.East:
        return 'East'
    elif k == DIRECTION.South:
        return 'South'
    elif k == DIRECTION.West:
        return 'West'

# Prints the current frame in the format x(i,j,k) [DIRECTION]
def printFrame(p):
    return "x(" + str(p['i']) + "," + str(p['j']) + "," + str(p['k']) + ") [" + directionNames(p['k']) + "]"

def localize():
    # Asks for the user to put in start and end positions
    x_s = userInput("x_s/Starting Position (i j k): ")
    x_g = userInput("\n x_g/Ending Position (i j k): ")

    print("\n Start: ", printFrame(x_s))
    print("\n End: ", printFrame(x_g))

    actions = input("\n Enter a string of actions (ex:FBRLR): ").upper()

    # Updates the frame in exec_motion
    frame = x_s

    # Runs through all the actions
    for step in range(len(actions)):
        a = actions[step]
        execMotion(frame, a)
        # Prints out current position
        print("Step " + str(step) + ": " + a + " -> " + printFrame(frame))
    
if __name__ == "__main__":
    localize()