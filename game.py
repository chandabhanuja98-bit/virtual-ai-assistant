import random

def play_guessing_game():

    secret_number = random.randint(1,20)
    

    Attempts = 5

    print("Assistant : Guess a number between 1 and 20")
    print(f"Assistant : You have {Attempts} trails ")

    for attempt in range(Attempts):
        guess = int(input("you : "))

        if guess == secret_number:
            print("Assistant : congratulation ! you gussed correct number")
            return 

        elif guess < secret_number:
            print("Assistant : secret number is higher")

        else :
            print("Assistant : secret number is lower")
    
    print("Assistant : You have reached maximum attempts")

    print(f"Assistant : The secret number is {secret_number}")
    


    





