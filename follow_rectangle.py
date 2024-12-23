#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()

color_sensor_in1 = ColorSensor(INPUT_1)
ultrasonic_sensor_in2 = UltrasonicSensor(INPUT_2)
gyro_sensor_in3 = GyroSensor(INPUT_3)
gps_sensor_in4 = GPSSensor(INPUT_4)
pen_in5 = Pen(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

def reached_turn() -> bool:
    return color_sensor_in1.red == 0
    
def keep_straight():
    if gyro_sensor_in3.angle > 0:
        print("correcting to the left")
        left_motor.on(5)
        right_motor.on(6)
    elif gyro_sensor_in3.angle < 0:
        print("correcting to the right")
        left_motor.on(6)
        right_motor.on(5)
    else:
        print("keep straight")
        left_motor.on(15)
        right_motor.on(15)
        
# Here is where your code starts
left_motor.on(15)
right_motor.on(15)
# gyro_sensor_in3.reset()
print("gyro reset")
while True:
    if not reached_turn():
        print(f"drive straight")
        print(f"gyro angle = {gyro_sensor_in3.angle}")
        keep_straight()
        time.sleep(1)
    else:
        print("reached turn")
        left_motor.off()
        right_motor.off()
