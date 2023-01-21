
# Quiz Game

print("Welcome to Quiz")
score = 0
playing = input("Are you ready to play? ")
if playing.lower() != "yes":
    quit("You have exited the quiz successfully")
else:
    print("Okay let's play")
    answer = input("What is the full form of CPU? ")
    if answer.lower() == "central processing unit":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    answer = input("What is the full form of RAM? ")
    if answer.lower() == "random access memory":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    answer = int(input("What is the size of Integer character: "))
    if answer == 4:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
print()
print("Your Final Score is : " + str(score))
print("Your percentage is: " + str((score/3)*100) + "%")
