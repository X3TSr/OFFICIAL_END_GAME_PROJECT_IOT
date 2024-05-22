# git commit -a -m 'MESSAGE'
# git push

import MotorFunctions as motor
import TheAIPartOfThings as AI
import CheckStation as stationChecker
import TrashRemoval
import time

# response = AI.run()
response = 'pmd'

TYPES = ['rest', 'pmd', 'karton/papier', 'gft', 'kga']

def findStation():
    res = response.lower()
    if res == TYPES[0]:
        station = 1
    elif res == TYPES[1]:
        station = 2
    elif res == TYPES[2]:
        station = 3
    elif res == TYPES[3]:
        station = 4
    elif res == TYPES[4]:
        station = 5
    else:
        station = 1
    return station

def disposeTrash():
    time.sleep(1)
    TrashRemoval.open()
    time.sleep(3)
    TrashRemoval.close()
    time.sleep(1)

station = findStation()

TrashRemoval.close()
motor.forwards()
stationChecker.checkStation(station)
motor.stop()

disposeTrash()

motor.backwards()
stationChecker.checkStation(station)
time.sleep(1.5)
motor.stop()