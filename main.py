import time
import lib.virtGPIO as GPIO

######################## Write example

# led = 9

# GPIO.setup(led, GPIO.OUT)
# GPIO.pinMode(led, GPIO.OUT)
# GPIO.setup(led, GPIO.OUT)
	
# # GPIO.output(led, GPIO.LOW)    
# # GPIO.digitalWrite(led, GPIO.LOW) 

# nextState = True
# while True:
#     if nextState:
#         GPIO.output(led, GPIO.HIGH)    
#         GPIO.digitalWrite(led, GPIO.HIGH)
#         nextState = False
#         print("ON")
#     else:
#         GPIO.output(led, GPIO.LOW)    
#         GPIO.digitalWrite(led, GPIO.LOW)
#         nextState = True
#         print("OFF")

#     time.sleep(1)

######################## Write example end




######################## Read example


button = 0
PRESSED_STATE = 1023
led = 9

GPIO.setup(button, GPIO.IN)
GPIO.pinMode(button, GPIO.IN)
GPIO.setup(button, GPIO.IN)

while True:
    state = 'zamknięte'

    if GPIO.analogRead(button) == PRESSED_STATE:
        state = 'zamknięte'
        GPIO.output(led, GPIO.HIGH)    
        GPIO.digitalWrite(led, GPIO.HIGH)
    else:
        state = 'otwarte' 
        GPIO.output(led, GPIO.LOW)    
        GPIO.digitalWrite(led, GPIO.LOW)
   
    print(f'Drzwi są {state}')
    time.sleep(0.2)
