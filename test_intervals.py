import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ctrlPin = 16
GPIO.setup(ctrlPin, GPIO.OUT)
if __name__ == "__main__":
	try:
		GPIO.output(ctrlPin, GPIO.HIGH)
		time.sleep(1.5)
		GPIO.output(ctrlPin,GPIO.LOW)
		time.sleep(0.5)
    		GPIO.cleanup()
# End program cleanly with keyboard
	except KeyboardInterrupt:
    		print("Quit")
		GPIO.cleanup()
		pass

    # Reset GPIO settings

