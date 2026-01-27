from asn1_tripod import tripodCycle
import sonar 
from asn1_turn_right import turnRight90
from asn1_turn_left import turnLeft90
from asn1_movement import sensor_left, sensor_right, sensor_reset
import time
from asn1_initialization import initialization

s = sonar.Sonar()

def blocked(dist):
    bound = 390 # 35 cm away from robot chassis + 4cm from sensor to chassis
    if dist < bound:
        return True
    else:
        return False

def checkBlockedandRotate():
    print("checking")
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

if __name__ == '__main__':  
    initialization()
    while True:
        tripodCycle()
        checkBlockedandRotate()