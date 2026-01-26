
# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn1_movement import tripodTrioLeftHeavy, tripodTrioRightHeavy
import argparse
import time

if __name__ == '__main__':  
    # allow us to read in step size from terminal argument
    parser = argparse.ArgumentParser()        
    parser.add_argument('step_size', type=int, help='step size of robot', default=225)
    args = parser.parse_args()

    while True:
        step_size = args.step_size
        tripodTrioLeftHeavy(1, 3, 5, step_size)
        time.sleep(1)
        tripodTrioRightHeavy(4, 6, 2, step_size)
        time.sleep(1)
