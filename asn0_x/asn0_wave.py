# Wave: This gait is characterized by moving only one leg forward (or backward) at a
# time and cycling through all of the legs, creating a “wave” effect.
import sonar
from asn0_movement import waveRight, waveLeft, stopCheck
import time
import signal
import argparse # https://docs.python.org/3.6/library/argparse.html#module-argparse


start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    s = sonar.Sonar()
    parser = argparse.ArgumentParser()        
    parser.add_argument('step_size', type=int, help='step size of robot', default=225)
    args = parser.parse_args()
 
    while True:
        step_size = args.step_size
        waveRight(3, step_size)
        time.sleep(.25)
        waveRight(2, step_size)
        time.sleep(.25)
        waveRight(1, step_size)
        time.sleep(.25)
        waveLeft(4, step_size)
        time.sleep(.25)
        waveLeft(5, step_size)
        time.sleep(.25)
        waveLeft(6, step_size)
        time.sleep(.25)
