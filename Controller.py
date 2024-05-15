# git commit -a -m 'MESSAGE'
# git push

import MotorFunctions as motor
import TheAIPartOfThings as AI
import ButtonFunctions as button
import time

response = AI.run()
# response = 'kga'

TYPES = ['rest', 'pmd', 'karton/papier', 'gft', 'kga']

for type in TYPES:
    if response.lower() == type:
        print(type)
        station = 0
        motor.forwards()

        if type == TYPES[0]:
            station = 1
            
        elif type == TYPES[1]:
            station = 2

        elif type == TYPES[2]:
            station = 3

        elif type == TYPES[3]:
            station = 4

        elif type == TYPES[4]:
            station = 5
            
        else:
            station = 1
        
        button.checkStation(station)
        motor.stop()

        time.sleep(3)
        motor.backwards()
        button.checkStation(station)

        time.sleep(1.5)
        motor.stop()
