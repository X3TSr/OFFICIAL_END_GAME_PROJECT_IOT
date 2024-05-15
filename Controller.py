# git commit -a -m 'MESSAGE'
# git push

import MotorFunctions as motor
import TheAIPartOfThings as AI
import ButtonFunctions as button
import time

response = AI.run()
# response = 'karton/papier'

TYPES = ['rest', 'pmd', 'karton/papier', 'gft', 'kga']

for type in TYPES:
    if response.lower() == type:
        if type == TYPES[0]:
            print(type)
            motor.forwards()
            button.checkStation(1)
            motor.stop()
            
        elif type == TYPES[1]:
            print(type)
            motor.forwards()
            button.checkStation(2)
            motor.stop()

        elif type == TYPES[2]:
            print(type)
            motor.forwards()
            button.checkStation(3)
            motor.stop()

        elif type == TYPES[3]:
            print(type)
            motor.forwards()
            button.checkStation(4)
            motor.stop()

        elif type == TYPES[4]:
            print(type)
            motor.forwards()
            button.checkStation(5)
            motor.stop()
            
        else:
            print('ERROR')
