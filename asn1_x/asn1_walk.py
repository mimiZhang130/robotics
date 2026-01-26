from asn1_tripod import tripodCycle
import sonar 
from asn1_turn_right import turnRight90
from asn1_turn_left import turnLeft90
s = sonar.Sonar()

def blocked(dist):
    bound = 25
    if dist < bound:
        return True
    else:
        return False

def checkBlockedandRotate():
    # Check if blocked forward
    if blocked(s.getDistance()):
        # Rotate sensor right
        # TODO: 
        # Check if blocked right
        if blocked(s.getDistance()):
            turnRight90()
            # Rotate sensor left
            # TODO: 
            # Check if blocked left
            if blocked(s.getDistance()):
                turnRight90()
                turnRight90()
        # Check if only blocked left
        else:
            # Rotate sensor left
            # TODO: 
            # Check if blocked left
            if blocked(s.getDistance()):
                turnLeft90()

if __name__ == '__main__':  
    tripodCycle()
    checkBlockedandRotate()