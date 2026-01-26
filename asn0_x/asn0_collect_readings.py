## STEP 4 ## 
# collect readings of sensor for 10cm, 20cm, and 30cm
import sonar
import time
import signal

start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    s = sonar.Sonar()

    while True:
        print("-- Readings at 10 cm -- ")
        for i in range(10):
            print(f'Trial {i + 1}')
            print(s.getDistance())
        print("Done with 10cm")

        time.sleep(10)
        print("-- Readings at 20 cm -- ")
        for i in range(10):
            print(f'Trial {i + 1}')
            print(s.getDistance())
        print("Done with 20cm")

        time.sleep(10)
        print("-- Readings at 30 cm -- ")
        for i in range(10):
            print(f'Trial {i + 1}')
            print(s.getDistance())
        print("Done with 30cm")
        break