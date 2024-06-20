# git commit -a -m 'MESSAGE'
# git push

import MotorFunctions as motor
import TheAIPartOfThings as AI
import CheckStation as stationChecker
import TrashRemoval
import time

def goTo(station, destination, sleepTime = 0.0):
    if destination == 'station':
        motor.forwards()
    elif destination == 'garage':
        motor.backwards()
    stationChecker.checkStation(station)
    time.sleep(sleepTime)
    motor.stop()
 

def start():
    response = AI.run()
    # response = 'gft'

    print(response)

    TYPES = ['rest', 'pmd', 'karton/papier']
    station = stationChecker.findStation(response, TYPES)
    TrashRemoval.close()
    if station != -1:
        goTo(station, 'station')
        TrashRemoval.disposeTrash()
        goTo(station, 'garage', .5)

# start() # To use when testing with Controller.py NOT WITH Start.py