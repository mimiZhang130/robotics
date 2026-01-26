
import ros_robot_controller_sdk as rrc
import time

board = rrc.Board()

if __name__ == '__main__':
    board.bus_servo_set_position(2, [[1, 800], [4, 800], [7, 800]])
    time.sleep(1)
    board.bus_servo_set_position(2, [[2, 800], [5, 800], [8, 800]])
    time.sleep(1)
    board.bus_servo_set_position(2, [[3, 200], [6, 200], [9, 200]])
    time.sleep(1)
    board.bus_servo_set_position(2, [[10, 800], [13, 800], [16, 800]])
    time.sleep(1)
    board.bus_servo_set_position(2, [[11, 200], [14, 200], [17, 200]])
    time.sleep(1)
    board.bus_servo_set_position(2, [[10, 800], [13, 800], [16, 800]])
