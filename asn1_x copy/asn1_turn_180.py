
from asn1_movement import rotateRight
import argparse
import time

if __name__ == '__main__':  
    # allow us to read in step size from terminal argument

    while True:
        for i in range(6):
            rotateRight(225)
            time.sleep(1)
        break
