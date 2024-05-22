import gpiod
import time

CHIP = gpiod.Chip('gpiochip4')
line = CHIP.get_line(27)
line.request(consumer="blink_led", type=gpiod.LINE_REQ_DIR_OUT)

def ledBlink():
    line.set_value(1)
    time.sleep(.5)
    line.set_value(0)
    time.sleep(.5)
    line.set_value(1)
    time.sleep(.5)
    line.set_value(0)
    time.sleep(.5)
    line.set_value(1)
    time.sleep(.5)
    line.set_value(0)
