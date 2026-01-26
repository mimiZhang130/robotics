# Ripple: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn0_movement import ripplePair
import time
import argparse

if __name__ == '__main__':   
    # allow us to read in step size from terminal argument
    parser = argparse.ArgumentParser()        
    parser.add_argument('step_size', type=int, help='step size of robot', default=225)
    args = parser.parse_args()
 
    while True:
        step_size = args.step_size
        ripplePair(3, 4, step_size)
        time.sleep(.5)
        ripplePair(1, 6, step_size)
        time.sleep(.5)
        ripplePair(2, 5, step_size)
        time.sleep(.5) 