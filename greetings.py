def show_welcome_message():
    print ('===========================================')
    print ('        MINI ALEXA - VIRTUAL ASSISTANT     ')
    print ('===========================================')


def get_user_name():

    print ("Assistant: Hi! I'm Mini Alexa. What's your name?")
    name = input('you : ')
    return name


def build_greeting(name):
    
    print(f"Assistant: Nice to meet you, {name}! Type 'help' \n \t   to see what I can do.")




