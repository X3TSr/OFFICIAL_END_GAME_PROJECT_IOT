import gpiod
import time

CHIP = gpiod.Chip('gpiochip4')
line = CHIP.get_line(21)
line.request(consumer="button_script", type=gpiod.LINE_REQ_DIR_IN)

def checkStation(destinationStation):
    last_value = 0
    debounce_ime = 0.5
    last_pressed_time = 0
    counter = 0
    checking = True

    while checking:
        value = line.get_value()
        current_time = time.time()

        if value == 1 and last_value == 0 and (current_time - last_pressed_time > debounce_ime):
            last_pressed_time = current_time
            counter += 1
            # print('COUNTER', counter)
            if counter == destinationStation:
                checking = False
                # print('STOP')
        last_value = value

def findStation(response, TYPES):
    res = response.lower()
    for type in TYPES:
        if res == type:
            station = TYPES.index(type) +1
    return station