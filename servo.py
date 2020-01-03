import RPi.GPIO as GPIO
import time
from random import seed
from random import randint
import time

servoPIN = 14 # This is next to the GND pin after the two 5v pins. Type PinOut in terminal to see this.
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) 
p.start(7.5) # Initialization
print("Servo PWM Duty Cycle: ")
servo_pos = [2,6.5,11,6.5]
for loopcount in servo_pos:
    print(loopcount)
    p.ChangeDutyCycle(loopcount)
    time.sleep(0.2)
    p.ChangeDutyCycle(0)
    time.sleep(3)

