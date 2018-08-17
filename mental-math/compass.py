import random
import time

import thread
import threading

compass_heading = random.randint(0,360)

prompt = "What is the reciprocal of this compass heading?\n"+str(compass_heading)+"\n"

def raw_input_with_timeout(prompt, timeout=10.0):
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    if astring is None:
	return -1
    else:
    	return astring

user_reciprocal = raw_input_with_timeout(prompt)

answer = None

if compass_heading < 180:
    answer = compass_heading + 180
else:
    answer = compass_heading - 180

if user_reciprocal == -1:
    print("Time exceeded")

if answer == int(user_reciprocal):
    print("Correct")
else:
    print("Incorrect")
    print("The answer is: "+str(answer))
