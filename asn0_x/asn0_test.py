import ros_robot_controller_sdk as rrc
import time
import signal

board = rrc.Board()
start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

## STEP 2 ##
if __name__ == '__main__':
    while True:
        # Lift each servo leg to the right of the LED display
        # 500 is default spider, < 500 is lower, > 500 is higher
        for i in range(2, 9, 3):
            print(f'Using servo {i}')
            board.bus_servo_set_position(1, [[i, 250]])
            time.sleep(2.5)
            board.bus_servo_set_position(1, [[i, 500]])
            time.sleep(2.5)
            board.bus_servo_stop([i, i + 1])

        # Lift each servo leg to the left of the LED display 
        # 500 is default spider, > 500 is higher, < 500 is lower
        for i in range(11, 18, 3):
            print(f'Using servo {i}')
            board.bus_servo_set_position(1, [[i, 750]])
            time.sleep(2.5)
            board.bus_servo_set_position(1, [[i, 500]])
            time.sleep(2.5)
            board.bus_servo_stop([i, i + 1])
        
        # Done lifting 
        print(f'Lifted all legs!')
        break