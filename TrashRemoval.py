from gpiozero import Servo, AngularServo
import time

servo = AngularServo(17)

def open():
    servo.angle = -90

def close():
    servo.angle = 90

def disposeTrash():
    time.sleep(1)
    open()
    time.sleep(3)
    close()
    time.sleep(1)