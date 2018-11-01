from time import sleep
import serial


with serial.Serial(port='COM3', baudrate=9600, timeout=1) as serial_port:
    while True:
        # rotation = int.from_bytes(serial_port.readline(), byteorder='little')
        try:
            rotation = int(serial_port.readline().decode("ascii"))
        except ValueError:
            continue
            
        print(rotation)
        # sleep(.1)
