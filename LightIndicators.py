import gpiod
import time

CHIP = gpiod.Chip('gpiochip4')
errorLed_line = CHIP.get_line(27)
errorLed_line.request(consumer="blink_led", type=gpiod.LINE_REQ_DIR_OUT)

picLed_line = CHIP.get_line(22)
picLed_line.request(consumer="picture_led", type=gpiod.LINE_REQ_DIR_OUT)

picLed_line2 = CHIP.get_line(16)
picLed_line2.request(consumer="picture_led2", type=gpiod.LINE_REQ_DIR_OUT)


def ledBlink():
    errorLed_line.set_value(1)
    time.sleep(.5)
    errorLed_line.set_value(0)
    time.sleep(.5)
    errorLed_line.set_value(1)
    time.sleep(.5)
    errorLed_line.set_value(0)
    time.sleep(.5)
    errorLed_line.set_value(1)
    time.sleep(.5)
    errorLed_line.set_value(0)

def PicLight_off():
    picLed_line.set_value(0)
    picLed_line2.set_value(0)
def PicLight_on():
    picLed_line.set_value(1)
    picLed_line2.set_value(1)