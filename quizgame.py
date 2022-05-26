print("Welcome to the game")

playing = input("Do you want to start the game? ")
if playing.lower() != "yes":
    quit()

print("lets start the game !  ")
score = 0
    
    
answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("correct!")
    score +=1
else:
    print("Incorrect")
    
answer = input("What is the full form of GUI? ")
if answer.lower() == "graphical user interface":
    print("correct!")
    score +=1
else:
    print("Incorrect")
     
    print("you got " + str(score) + " questions correct!")
    print("you got " + str((score * 4) / 100) + " % !")
    
    