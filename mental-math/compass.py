import random
import time

compass_heading = random.randint(0,360)

user_reciprocal = input("What is the reciprocal of this compass heading?\n"+str(compass_heading)+"\n")

time.sleep(5)

answer = 0

if compass_heading < 180:
#   global answer
    answer = compass_heading + 180
else:
#   global answer
    answer = compass_heading - 180

if answer == user_reciprocal:
    print("Correct")
else:
    print("Incorrect")
