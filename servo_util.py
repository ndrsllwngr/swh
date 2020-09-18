from time import sleep

DUTY_MIN = 20
DUTY_MAX = 123
SLEEP = 0.1

# position needs to be between 0.0 and 1.0
def rotate(servo, position):
    print("desired position: "+ str(position))
    current_duty = servo.duty()
    if(current_duty>DUTY_MAX):
        current_duty = DUTY_MAX
    print("curr duty: " + str(current_duty))
    new_duty = int(DUTY_MIN + position * (DUTY_MAX - DUTY_MIN))
    print("new duty: " + str(new_duty))

    step = 1 if current_duty < new_duty else -1

    for i in range(current_duty, new_duty+1, step):
        servo.duty(i)
        sleep(SLEEP)