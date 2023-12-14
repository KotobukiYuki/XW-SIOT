import RPi.GPIO as GPIO

FAN = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(FAN, GPIO.OUT)

def fanOn():
    GPIO.output(FAN, GPIO.HIGH)
    print('Fan On')

def fanOff():
    GPIO.output(FAN, GPIO.LOW)
    print('Fan Off')