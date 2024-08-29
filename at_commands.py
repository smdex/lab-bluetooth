import pyb

led2 = pyb.LED(2)
led3 = pyb.LED(3)

uart = pyb.UART(1, 38400)

arg = "NAME?"
command = "AT+" + arg + "\r\n"

while True:
    uart.write(command)
    answer = uart.read()
    if answer:
        print(answer)
        break


'''
pyboard - BT adapter
Y9        RXD
Y10       TXD
GND       GND
3V3       KEY
V+        VCC

'''
