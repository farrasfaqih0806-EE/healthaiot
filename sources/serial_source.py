import serial

import config


def stream():

    ser = serial.Serial(

        config.SERIAL_PORT,

        config.SERIAL_BAUDRATE

    )

    print("Serial Connected")

    while True:

        try:

            line = ser.readline().decode().strip()

            yield float(line)

        except:

            continue