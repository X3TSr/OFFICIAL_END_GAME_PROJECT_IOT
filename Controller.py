# git commit -a -m 'MESSAGE'
# git push

import MotorFunctions as motor
import TheAIPartOfThings as AI
import CheckStation as stationChecker
import TrashRemoval
import time

# response = AI.run()
response = 'gft'

TYPES = ['rest', 'pmd', 'karton/papier', 'gft', 'kga']
station = stationChecker.findStation(response, TYPES)

def goTo(destination, sleepTime = 0.0):
    if destination == 'station':
        motor.forwards()
    elif destination == 'garage':
        motor.backwards()
    stationChecker.checkStation(station)
    time.sleep(sleepTime)
    motor.stop()
 

TrashRemoval.close()
if station != -1:
    goTo('station')
    TrashRemoval.disposeTrash()
    goTo('garage', 1.5)