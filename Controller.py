import MotorFunctions as motor
import TheAIPartOfThings as AI
import time

response = AI.run()

TYPES = ['rest', 'pmd', 'karton/papier', 'gft', 'kga']

for type in TYPES:
    if response.lower() == type:
        print(type)
        motor.forwards()
        time.sleep(3)
        motor.stop()
        # if type == TYPES[0]:
