#number guessing game
import random

lucky_number=random.randint(1,100) 

user_number =int( input("enter any number between 1-100"))
if user_number == lucky_number:
    print("You are successful!🎰")

else: 
    print("sorry you lost try again!😭"+str(lucky_number))
    
