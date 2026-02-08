from asn2_tripod import tripodCycle
import sonar 
from asn2_turn_right import turnRight90
from asn2_turn_left import turnLeft90
from asn2_movement import sensor_left, sensor_right, sensor_reset
from asn2_initialization import initialization
from time import time

s = sonar.Sonar()

def blocked(dist):
    bound = 390 # 35 cm away from robot chassis + 4cm from sensor to chassis
    if dist < bound:
        return True
    else:
        return False

def checkBlockedandRotate():
    print(s.getDistance())
    # Check if blocked forward
    if blocked(s.getDistance()):
        print("blocked front")

        # Rotate sensor right
        sensor_right()
        print("right distance: " + str(s.getDistance()))

        # Check if blocked right
        if blocked(s.getDistance()):
            print("blocked right")
            # Rotate sensor left
            sensor_left()
            print("left distance: " + str(s.getDistance()))

            # Check if blocked left
            if blocked(s.getDistance()):
                print("blocked left")
                turnRight90()
                turnRight90()
            else:
                turnLeft90()
        # Check if only blocked left
        else:
            # Rotate sensor left
            sensor_left()
            print("left distance: " + str(s.getDistance()))

            # Check if blocked left
            if blocked(s.getDistance()):
                print("blocked left")
                turnRight90()
    sensor_reset()

## UNTESTED CODE THAT IS BETTER
# def checkBlockedandRotate():
#     print("checking")
#     print(s.getDistance())
#     right_blocked = False
#     left_blocked = False

#     # Check if blocked forward
#     if blocked(s.getDistance()):
#         print("blocked front")

#         # Rotate sensor right & check right distance
#         sensor_right()
#         print("right distance: " + str(s.getDistance()))
#         if blocked(s.getDistance()):
#             right_blocked = True
        
#         # Rotate sensor left & check left distance
#         sensor_left()
#         print("left distance: " + str(s.getDistance()))
#         if blocked(s.getDistance()):
#             left_blocked = True

#         # turn based on left & right blocks
#         if right_blocked and left_blocked:
#             turnRight90()
#             turnRight90()
#         elif right_blocked:
#             turnLeft90()
#         else:
#             turnRight90()
        
#     sensor_reset()

if __name__ == '__main__':  
    # initialization()
    while True:
        tripodCycle()
        checkBlockedandRotate()
        time.sleep(1)