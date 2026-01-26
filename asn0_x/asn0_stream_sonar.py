import time
import sonar
import signal

start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

## STEP 3 ##
if __name__ == '__main__':

    s = sonar.Sonar()

    while True:
        # stream sonar sensor to terminal for 1 second
        for i in range(10):
            start_time = time.time()
            while True:
                curr_time = time.time()
                if curr_time - start_time > 1:
                    break
                else:
                    print(s.getDistance())