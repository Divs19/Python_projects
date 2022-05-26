import random 

guess_number = input("Enter the number! ")

if guess_number.isdigit():
    guess_number = int(guess_number)

    if guess_number <= 0:
        print("Please type a number larger than 0 next time!")
        quit()
else:
        print("Please type a number next time")
        quit()
random_number = random.randint(0, guess_number)
print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess! ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue

    if user_guess == random_number:
        print('you got it!')
        break
    else:
        print("you got it wrong!")

print("you got it in", guesses, "guesses")

    
      
