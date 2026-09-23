from datetime_utils import get_current_time,get_current_date
from calculator import calculate
from content import get_random_joke
from game import play_guessing_game
from content import get_random_quote
from content import get_random_fact
from greetings import show_welcome_message
from greetings import get_user_name
from greetings import build_greeting
from calculator import parse_expression
from help_menu import print_help
from ai_concepts import recommend_activity
from ai_concepts import perceptron_demo

show_welcome_message()
name = get_user_name()
build_greeting(name)

while True : 
    command = input('you : ')
    if command == 'help':
        print_help()
    
    elif command == 'time':
        current_time = get_current_time()
        print(f"Assistant : Current time is {current_time}")

    elif command == 'date':
        current_date = get_current_date()
        print(f"Assistant : Current time is {current_date}")

    elif command == 'calculate':
        expression = input("Assistant : Enter an expression: ")

        result = parse_expression(expression)

        if result is None:
            print("Assistant : Invalid expression. Please use format: 20 + 30")
        else:
            num1, operator, num2 = result

            calculation = calculate(num1, operator, num2)

            if calculation is None:
                print("Assistant : Invalid calculation.")
            else:
                print(f"Assistant : Result is {calculation}")

    elif command == 'joke':
        joke = get_random_joke()
        print(f"Assistant : {joke}")

    elif command == 'quote':
        Quote = get_random_quote()
        print(f"Assistant : {Quote}")

    elif command == 'fact':
        facts = get_random_fact()
        print(f"Assistant : {facts}")
        
    elif command == 'game':
        play_guessing_game()
        
    elif command == 'exit':
        print(f"Assistant : Goodbye, {name}! Have a great day.")
        break

    elif command == 'recommend_activity':
        print("Assistant : I will recommend an activity for you based on current time")
        recommend_activity()

    elif command == 'perceptron':
        print("Assistant : calculation demonstrating inputs, weights, bias, and output")
        perceptron_demo()

    else :
        print("Assistant : You have choosen out of menu options, please type 'help' so I can provide what I can able to do for you  ")

