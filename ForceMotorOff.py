import gpiod

CHIP = gpiod.Chip('gpiochip4')
ENABLE_A = 2
ENABLE_B = 14
FORWARDS_A = 4
FORWARDS_B = 15
BACKWARDS_A = 3
BACKWARDS_B = 18

motor_pins = [FORWARDS_A, FORWARDS_B, BACKWARDS_A, BACKWARDS_B, ENABLE_A, ENABLE_B]

for motor in motor_pins:
    motor_line = CHIP.get_line(motor)
    motor_line.request(consumer="MOTOR", type=gpiod.LINE_REQ_DIR_OUT)
    motor_line.set_value(0)