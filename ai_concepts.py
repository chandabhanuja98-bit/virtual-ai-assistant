from datetime import datetime


def recommend_activity():
    now = datetime.now()
    time = now.hour
    print("time : ",time)

    if time <= 10 :
        print("Assistant : It's breakfast time. Have it and have a good day! ")
    elif time > 10 and time < 12 :
        print("Assistant : Please do your works ")
    elif time > 12 and time < 14 :
        print("Assistant : It's Lunch time. Have it !")
    elif time > 15 and time < 19 :
        print("Assistant : It's Snack time. Have it !")
    else :
        print("Assistant : It's Dinner time. Have it !")


def  perceptron_demo():
     
    input1 = int(input("Enter the input1 : "))
    input2 = int(input("Enter the input2 : "))

    weight1 = 0.5
    weight2 = 0.4

    bias = -0.5

    weighted_sum = (input1*weight1 + input2*weight2) + bias

    if weighted_sum > 1:
        print("Assistant : The output is 1")
    else : 
        print("Assistant : The output is 0")



     

    




    







