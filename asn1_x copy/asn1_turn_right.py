
# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn1_movement import rotateRight
import argparse
import time

if __name__ == '__main__':  
    # allow us to read in step size from terminal argument
    while True:
        for i in range(3):
            rotateRight(220)
            time.sleep(1)
        break
