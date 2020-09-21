from time import sleep

DUTY_MIN = 120
DUTY_MAX = 1023
SLEEP = 0.0005
MIN_POS = 0.55
MAX_POS = 1.0

def init(servo):
    print("INIT")
    servo.duty(DUTY_MAX)

# position needs to be between 0.0 and 1.0
def rotate(servo, pos, speed=SLEEP, step=1):
    position = MAX_POS - pos * (MAX_POS - MIN_POS)
    print("desired position: "+ str(position))
    current_duty = servo.duty()
    if(current_duty>DUTY_MAX):
        current_duty = DUTY_MAX
    print("curr duty: " + str(current_duty))
    new_duty = int(DUTY_MIN + position * (DUTY_MAX - DUTY_MIN))
    print("new duty: " + str(new_duty))
    servo.duty(i)
    step = step if current_duty < new_duty else -step

    for i in range(current_duty, new_duty+1, step):
        servo.duty(i)
        #print(str(i) + " - " + str(servo.duty()))
        sleep(speed)