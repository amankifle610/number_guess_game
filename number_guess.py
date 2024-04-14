import random

def getInput():
    top_of_range=input("Enter a number? ")
    while top_of_range.isdigit()==False:
        print("please enter a digit!")
        top_of_range=input("Enter a number? ")
    return int(top_of_range)

top_of_range=getInput()
while top_of_range<=0:
    print("please enter a digit greater than 0!")
    top_of_range=getInput()

x=random.randint(0,top_of_range)
i=3
while i>0:
    guess=input("Please guess the number between 1 and "+str(top_of_range)+": ")
    if(guess.isdigit()==True and x==int(guess)):
        print("congratulations! you guess the number correctly.")
        quit()
    elif(i>1):
        print("you have "+str(i-1)+" chances")
    i-=1

print("Sorry the number was "+str(x))
