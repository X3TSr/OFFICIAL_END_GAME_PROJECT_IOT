import LightIndicators as LED
import gpiod
import time

CHIP = gpiod.Chip('gpiochip4')
stationButton_line = CHIP.get_line(21)
stationButton_line.request(consumer="button_script", type=gpiod.LINE_REQ_DIR_IN)

def checkStation(destinationStation):
    last_value = 0
    debounce_time = 0.5
    last_pressed_time = 0
    counter = 0
    checking = True

    while checking:
        value = stationButton_line.get_value()
        current_time = time.time()

        if value == 1 and last_value == 0 and (current_time - last_pressed_time > debounce_time):
            last_pressed_time = current_time
            counter += 1
            # print('COUNTER', counter)
            if counter == destinationStation:
                checking = False
                # print('STOP')
        last_value = value

def findStation(response, TYPES):
    station = -1
    res = response.lower()
    for type in TYPES:
        if res == type:
            station = TYPES.index(type) +1
    if station == -1:
        LED.ledBlink()
    return station