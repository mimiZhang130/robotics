from asn2_tripod import tripodCycle
import sonar 
from asn2_movement import sensor_left, sensor_right, sensor_reset
from asn2_turn_right import turnRight90
from asn2_turn_left import turnLeft90
from asn2_turn_180 import turn180

s = sonar.Sonar()

def check_right():
    sensor_right()
    rightDistance = s.getDistance()
    print("right distance: " + str(rightDistance))
    sensor_reset()
    if rightDistance < 350:
        return True
    else:
        return False

def check_left():
    sensor_left()
    leftDistance = s.getDistance()
    print("left distance: " + str(leftDistance))
    sensor_reset()
    if leftDistance < 350:
        return True
    else:
        return False
    
# returns whether we have a wall on the left, right, or in front of the robot
def check_directions(curr_direction, direction):
    heading_change = (direction + 4 - curr_direction) % 4
    if heading_change == 1:
        return check_right()
    elif heading_change == 3:
        return check_left()
    elif heading_change == 0:
        sensor_reset()
        return s.getDistance() < 350

    return "ERROR OUT"
    
# turn from curr_direction to direction
def turn_to_direction(curr_direction, direction):
    heading_change = (direction + 4 - curr_direction) % 4
    if heading_change == 1:
        turnRight90()
    elif heading_change == 2:
        turn180()
    elif heading_change == 3:
        turnLeft90()

# walk one tile forward
cycles_per_cell = 6
def forward_cell(hipAdjust = [0, 0, 0, 0, 0, 0]):
    for i in range(cycles_per_cell):
        tripodCycle(hipAdjusts=hipAdjust)

def get_opp_direction(curr_direction):
    return (curr_direction + 1) % 4 + 1

if __name__ == '__main__':  
    # initialization()
    # while True:
    #     tripodCycle()
    #     check_directions()
    pass