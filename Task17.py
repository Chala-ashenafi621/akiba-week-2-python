#TASK 17 — NUMBER GUESSING GAME
secret = 21
count = 0
while count < 5:
    guess = int(input("Guess the number: "))
    count += 1
    if guess == secret:
        print("Congratulations!")
        print("You guessed the number in", count, "attempts.")
        break
if guess != secret:
    print("Game Over!")