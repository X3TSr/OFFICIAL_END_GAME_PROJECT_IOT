import gpiod
import time
import Controller
import LightIndicators
import TrashRemoval

LightIndicators.PicLight_off()
TrashRemoval.close()

CHIP = gpiod.Chip('gpiochip4')
startButton_line = CHIP.get_line(20)
startButton_line.request(consumer="button_script", type=gpiod.LINE_REQ_DIR_IN)

last_value = 0
debounce_time = 0.5
last_pressed_time = 0
counter = 0

while True:
    value = startButton_line.get_value()
    current_time = time.time()
    if value == 1 and last_value == 0 and (current_time - last_pressed_time > debounce_time):
        last_pressed_time = current_time
        Controller.start()

    last_value = value