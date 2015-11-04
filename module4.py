##############################################
# File Name: module4.py
# Version: 1.0
# Team No.: 27
# Team Name:
# Date: 4 Nov 15
##############################################

import RPi.GPIO as GPIO
import time

print 'Press CTRL+C to exit the program'

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

RUNNING = True

try:
   while RUNNING:

    print 'Turn on red light\n'
    GPIO.output(11, True)
    time.sleep(2)
    GPIO.output(11, False)
    
    print 'Turn on orange light\n'    
    GPIO.output(13, True)
    time.sleep(2)
    GPIO.output(13, False)
    
    print 'Turn on green light\n'    
    GPIO.output(15, True)
    time.sleep(2)
    GPIO.output(15, False)

# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
   RUNNING = False
   print "\nQuitting program."

# Actions under 'finally' will always be called, regardless of
# what stopped the program (be it an error or an interrupt)
finally:
   # Stop and cleanup to finish cleanly so the pins
   # are available to be used again
   GPIO.cleanup()
   
print "\nProgram ended"
