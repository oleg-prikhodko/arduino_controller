import serial


with serial.Serial(port='COM3', baudrate=9600, timeout=1) as serial_port:
    while True:
        try:
            rotation = int(serial_port.readline().decode("ascii"))
            print(rotation)
        except ValueError:
            continue
