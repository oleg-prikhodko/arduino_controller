from p5 import *
import serial

port = serial.Serial(port='COM3', baudrate=9600)
rotation = 0
prev_rotation = 0
max_color_value = 255
coefficient = 4

def setup():
    size(1280, 720)

def draw():
    global rotation, prev_rotation

    raw_data = port.readline()
    # print(raw_data)
    ascii_string = raw_data.decode('ascii').strip()
    # print(ascii_string)

    if ascii_string.isdecimal():
        rotation = int(int(ascii_string) /max_color_value * max_color_value / coefficient)
        # print(rotation)

    port.reset_input_buffer()
    background(rotation)
    prev_rotation = rotation

if __name__ == '__main__':
    run()
    