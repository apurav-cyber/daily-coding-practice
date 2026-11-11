print("---------------guess a number-----------------------")

user_number = int(input("make a guess"))

import random 
guess_number = random.randint(1,10)
if guess_number==user_number:
    print("correct")
while guess_number !=user_number:
 user_number=int(input("make a guess"))
 if guess_number>user_number:
    print("high number,enter smaller number")
 else:
    print("smaller number,enter higher number")

print("guess number",guess_number)