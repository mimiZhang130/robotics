# General Notes: I think this works (if i did the math in my head right). Maybe add more validation for the inputs and stuff 
# so that like numbers outside of the accpetable range can't be inputed? Otherwise hopefully this works 

from asn2_tripod import tripodCycle
from asn2_turn_left import turnLeft90
from asn2_turn_right import turnRight90
from asn2_turn_180 import turn180
from asn2_initialization import initialization

# Importing set directions (k) and map
from asn2_grpA import DIRECTION, CSME301Map

# robot info stores current direction & location
# robot_info = [DIRECTION.South, [0, 0]]

# Move forward one cell block (center-to-center)
cycles_per_cell = 6
def forwardCell(hipAdjust = [0, 0, 0, 0, 0, 0]):
    for i in range(cycles_per_cell):
        tripodCycle(hipAdjusts=hipAdjust)

# Updating heading when turning
def kRight(robot_info):
    k = robot_info[0]
    # North(1)->East(2), East(2)->South(3), etc
    if k == DIRECTION.North:
        robot_info[0] = DIRECTION.East
    elif k == DIRECTION.East:
        robot_info[0] = DIRECTION.South
    elif k == DIRECTION.South:
        robot_info[0] = DIRECTION.West
    elif k == DIRECTION.West:
        robot_info[0] = DIRECTION.North
    return robot_info

def kLeft(robot_info):
    k = robot_info[0]
    # North(1)->West(4), West(4)->South(3), etc
    if k == DIRECTION.North:
        robot_info[0] = DIRECTION.West
    elif k == DIRECTION.West:
        robot_info[0] = DIRECTION.South
    elif k == DIRECTION.South:
        robot_info[0] = DIRECTION.East
    elif k == DIRECTION.East:
        robot_info[0] = DIRECTION.North
    return robot_info

def deltaPos(robot_info):
    k = robot_info[0]
    # i+ when going down, j+ going right. Top left is (0,0)
    if k == DIRECTION.North:
        robot_info[1][0] -= 1
    elif k == DIRECTION.East:
        robot_info[1][1] += 1
    elif k == DIRECTION.South:
        robot_info[1][0] += 1
    elif k == DIRECTION.West:
        robot_info[1][1] -= 1
    return robot_info

def execMotion(action, robot_info):
    # Dict input for frame = {'i': int, 'j':int, k: one of the four directions}
    # String input for action = 'F', 'L', 'R', 'B' (Fowards, Left, Right, Backwards)
    # Performs the movements and updates internal tracker (I think this works?)
    if action == 'F':
        forwardCell()
        robot_info = deltaPos(robot_info)

    elif action == 'R':
        # When turning we dont actually move anywhere so the i and j doesn't change
        # Heading is the only thing that changes
        turnRight90()
        robot_info = kRight(robot_info)

    elif action == 'L':
        turnLeft90()
        robot_info = kLeft(robot_info)

    elif action == "B":
        turn180()
        robot_info = kRight(robot_info)
        robot_info = kRight(robot_info)

    return robot_info

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
def printFrame(robot_info):
    return "x(" + str(robot_info[1][0]) + "," + str(robot_info[1][1]) + "," + str(robot_info[0]) + ") [" + directionNames(robot_info[0]) + "]"

def runActions(actions, robot_info):
    # Runs through all the actions
    for step in range(len(actions)):
        a = actions[step]
        execMotion(a, robot_info)
        # Prints out current position
        print("Step " + str(step) + ": " + a + " -> " + printFrame(robot_info))

def calc_heading_change(goal_dir, curr_dir):
    heading_change = (goal_dir + 4 - curr_dir) % 4
    
    match heading_change:
        case 1: 
            return "R"
        case 2:
            return "B"
        case 3:
            return "L"
        case _: 
            return ""

def localize():
    # Asks for the user to put in start and end positions
    x_s = userInput("x_s/Starting Position (i j k): ")
    x_g = userInput("\n x_g/Ending Position (i j k): ")

    # actions = input("\n Enter a string of actions (ex:FBRLR): ").upper()
    
    actions = ''

    # set heading
    robot_info = [x_s['k'], [x_s['i'], x_s['j']]]
    print("\n Start: ", printFrame(robot_info))

    actions = ''
    i_dst = x_g['i'] - robot_info[1][0]
    
    # move i_dst amount
    if i_dst > 0: # move i_dst south
        actions += calc_heading_change(DIRECTION.South, robot_info[0])
    elif i_dst < 0:
        actions += calc_heading_change(DIRECTION.North, robot_info[0])

    for i in range(abs(i_dst)):
        actions += "F"

    runActions(actions, robot_info) 

    actions = ''
    j_dst = x_g['j'] - robot_info[1][1]
    # move j_dst amount
    if j_dst > 0: # move east
        actions += calc_heading_change(DIRECTION.East, robot_info[0])
    elif j_dst < 0: # move west
        actions += calc_heading_change(DIRECTION.West, robot_info[0])

    for i in range(abs(j_dst)):
        actions += "F"
    print("actions: " + actions)
    runActions(actions, robot_info)

    actions = ''
    
    # change heading at end
    actions += calc_heading_change(x_g['k'], robot_info[0])

    runActions(actions, robot_info)

    print("\n End: ", printFrame(robot_info))
    
if __name__ == "__main__":
    initialization()
    localize()