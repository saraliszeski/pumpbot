import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ctrlPin = 16
GPIO.setup(ctrlPin, GPIO.OUT)
try:
	while(True):
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(1.5)
		GPIO.output(ledPin,GPIO.LOW)
		time.sleep(0.5)
		

# End program cleanly with keyboard
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()
