import random

rock= '''    _______\n---'    ____)\n      (______)\n      (_____)\n      (____)\n---.__(___)\n'''
paper='''     _______\n---'     ____)____\n            ______)\n           ________)\n        _________)\n---.__________)\n'''
scissors='''     ______\n---'    ____)____\n           ______)\n        __________)\n      (____)\n---.__(___)\n'''

choice_image=[rock,paper,scissors]
user_choice=int(input("Choose from the folowing \n0.rock\n1.paper\n2.scisssors\nwhat is  your choice ? ( 0, 1 or 2) :"))
print("Your choice:\n", choice_image[user_choice])
computer_choice=random.randint(0,2)
print("computer choose:", computer_choice)
print(choice_image[computer_choice])
if user_choice!=0 and user_choice!=1 and user_choice!=2:
    print("Invalid choice")
else:
   
    if computer_choice==user_choice:
        print("It's a draw")
    elif computer_choice==0 and user_choice==2:
        print("user loose")
    elif computer_choice==2 and user_choice==0:
        print("user win")
    elif computer_choice < user_choice:
        print("user win")
    elif computer_choice > user_choice:
        print("user loose")