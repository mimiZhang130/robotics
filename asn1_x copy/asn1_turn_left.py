from asn1_movement import rotateLeft
import argparse
import time

if __name__ == '__main__':  
    # allow us to read in step size from terminal argument
    while True:
        for i in range(3):
            rotateLeft(200)
            time.sleep(1)
        break
