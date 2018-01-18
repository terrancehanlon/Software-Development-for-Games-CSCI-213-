import random
name = input("Enter name: ")
print("Hello", name)
print("Guess the number, enter -1 to exit game")
totalGuesses = 0;
for i in range(1,4):
    print("-----------------")
    print("Game: ", i)
    guesses = 0
    answer = random.randrange(1,11)
    guess = -1
    while guess != answer:
        guess = input("Enter a guess form 1-10: ")
        flag = guess.isnumeric()
        while flag == False:
            if guess =='-1':
                guess = int(guess)
                break
            guess = input("Wrong value, enter a NUMBER between 1-10: ")
            flag = guess.isnumeric()
        guess = int(guess)
        if guess == -1:
            break
        while guess < 1 or guess > 10:
            guess = input("Enter a value between 1-10: ")
        if guess == answer:
            print("You won! \nCorrect Answer: ", answer, "Your Guess: ", guess)
            guesses += 1
            totalGuesses += 1
            print("Guesses you took: ", guesses)
        elif guess < answer:
            print("Your guess was to small")
            guesses += 1
            totalGuesses += 1
        else:
            print("Your guess was too big")
            guesses += 1
            totalGuesses += 1
    if guess == -1:
        break
if guess == -1:
    print("You've exited the game, thanks for playing!")
else:
    print("You've finished! Heres you score: \nAverage guess per game: ", float(totalGuesses/3))

        
        
