# git commit -a -m 'MESSAGE'
# git push

import MotorFunctions as motor
import TheAIPartOfThings as AI
import ButtonFunctions as button
import time

response = AI.run()

TYPES = ['rest', 'pmd', 'karton/papier', 'gft', 'kga']

for type in TYPES:
    if response.lower() == type:
        if type == TYPES[0]:
            print(type)
            motor.forwards()
            button.checkStation(True, 2)
            motor.stop()
            
        elif type == TYPES[1]:
            print(type)
            motor.forwards()
            time.sleep(3)
            motor.backwards()
            time.sleep(3)
            motor.stop()

        elif type == TYPES[2]:
            print(type)
            motor.forwards()
            button.checkStation(True, 2)
            motor.stop()

        elif type == TYPES[3]:
            print(type)
            motor.forwards()
            time.sleep(3)
            motor.backwards()
            time.sleep(3)
            motor.stop()

        elif type == TYPES[4]:
            print(type)
            motor.forwards()
            time.sleep(3)
            motor.backwards()
            time.sleep(3)
            motor.stop()
            
        else:
            print('ERROR')
