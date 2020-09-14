# IMPORT LIBRARIES
import RPi.GPIO as GPIO
import time

# CONFIGURE PYTHON WITH PI
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# PIN ASSIGNMENTS
switchCW = 22 # CLOCKWISE SWITCH POSITION PIN (CONNECT TO SWITCH TERMINAL 1)
switchCCW = 27 # COUNTERCLOCKWISE SWITCH POSITION PIN (CONNECT TO SWITCH TERMINAL 3)

DIR = 23 # DIRECTION GPIO PIN
PUL = 25 # PULSE GPIO PIN
ENA = 17 # ENABLE GPIO PIN

# CONFIGURE INPUT PINS
# SWITCH TERMINAL 2 GETS CONNECTED TO 3.3V SOURCE
GPIO.setup(switchCW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchCCW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# CONFIGURE OUTPUT PINS
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# CONFIGURE PWM CONTROL CHARACTERISTICS


# CONFIGURE STEP PIN AS PWM WITH FREQUENCY
pulse = GPIO.PWM(PUL, 3200)

try:
    while True:
        if GPIO.input(switchCW): # SWITCH IN CLOCKWISE POSITION?
            #print("Clockwise!") # TERMINAL FEEDBACK
            GPIO.output(ENA, False) # ENABLE THE MOTOR DRIVE
            GPIO.output(DIR, True) # SET DIRECTION PIN TO HIGH
            pulse.start(50) # START PWM WITH 50% DUTY CYCLE
        elif GPIO.input(switchCCW): # SWITCH IN COUNTERCLOCKWISE POSITION?
            #print("Counterclockwise!") # TERMINAL FEEDBACK
            GPIO.output(ENA, False) # ENABLE THE MOTOT DRIVE
            GPIO.output(DIR, False) # SET DIRECTION PIN TO LOW
            pulse.start(50) # START PWM WITH 50% DUTY CYCLE
        else: # SWITCH IN CENTER POSITION
            #print("Idle!") # TERMINAL FEEDBACK
            GPIO.output(DIR, False) # SET DIRECTION PIN TO LOW
            GPIO.output(PUL, False) # TURN OFF PWM GPIO
            GPIO.output(ENA, True) # DISABLE THE MOTOR DRIVE
        time.sleep(0.1)
except KeyboardInterrupt: # PRESS CTRL-C TO TERMINATE THE SCRIPT
    print ("\nCtrl-C pressed. Stopping and exiting...")
finally:
    GPIO.output(PUL, False) # TURN OFF PWM GPIO
    GPIO.output(ENA, True) # DISABLE THE MOTOR DRIVE
    GPIO.cleanup()