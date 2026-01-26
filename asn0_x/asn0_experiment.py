import ros_robot_controller_sdk as rrc
import time
import signal

board = rrc.Board()
start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    
    ######## Experimentation to see 0 and 500 extremes ########
    for i in range(1, 19):
        print(f'Moving Servo {i} (500)...: \n')
        board.bus_servo_set_position(1, [[i, 500]])
        time.sleep(2.5)
        print(f'Moving Servo {i} (0)...: \n')
        board.bus_servo_set_position(1, [[i, 0]])
        time.sleep(2.5)