import pyb

led2 = pyb.LED(2)
led3 = pyb.LED(3)

uart = pyb.UART(1, 38400)

command = "AT+VERSION?" + "\r\n"

while True:
    uart.write(command)
    answer = uart.read()
    if answer:
        print(answer)
        break


