import time
import common.ros_robot_controller_sdk as rrc
import math

'''
    程序功能：IMU例程(MPU6050)(Program function: IMU(MPU6050))

    运行效果：程序运行后，在屏幕不断输出获取到的IMU的数据(Program outcome: After running the program, the obtained IMU data will be continuously output on the screen)

    对应教程文档路径：  SpiderPi Pro智能六足机器人\第10章 树莓派主板及扩展板拓展课程\2.拓展课程之树莓派扩展板课程\第4课 加速度计的使用(The path of corresponding tutorial： SpiderPi Pro 5\10.Raspberry Pi Controller & Expansion Board\2.Raspberry Pi Expansion Board Lesson\Lesson 4 Use of Accelerometer)
'''
board = rrc.Board()
board.enable_reception()


while True:
    try:
        res = board.get_imu()          # 获取IMU数据(obtain IMU data)
        time.sleep(1)
        
        if res is not None:
            # print(res)           # 输出获取到的IMU数据(output the obtained IMU data)
            print(f"Acceleration: X:{res[0]:.2f}, Y:{res[1]:.2f}, Z:{res[2]} m/s^2")
            print(f"Gyro: X:{res[3]:.2f}, Y:{res[4]:.2f}, Z:{res[5]:.2f} deg/s")

            acc_mag = math.sqrt(res[0]^2 + res[1]^2 + res[2]^2)

            print(acc_mag)

            # start = time.time()
            # for i in range(1000):
            #     board.get_imu()
            # end = time.time()
            # print("Rate:", 1000/(end-start))

        # time.sleep(0.01)
        time.sleep(2)
    except KeyboardInterrupt:
        break
