import random

lowest_int=1
highest_int=100
guesses=0
answer=random.randint(lowest_int,highest_int)
is_running=True
print("Number Guessing Game")
while is_running:
    print(f"enter a number less than {highest_int} and more than {lowest_int}")
    guess=input("enter a number: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess < lowest_int or guess > highest_int:
            print("that number is out of range")
            print(f"please enter the number between {lowest_int}-{highest_int}")
        elif guess>answer:
            print("Your guess is too high!")
        elif guess<answer:
            print("your answer is too low")
        else:
            print(f"your answer {answer} is Correct!")
            print(f"number of guesses: {guesses}")
            is_running=False
    else:
        print("invalid guess")
        print(f"please enter the number between {lowest_int}-{highest_int}")
