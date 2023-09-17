import random
repeat = "yes"
money = 1000
while repeat == "yes":
    

    print("Your current available amount is: ")
    print(money)

    num = random.randint(1, 37)
    if num == 37:
        color = "green"

    else:
        if num % 2 == 1:
            color = "red"

        elif num % 2 == 0:
            color = "black"


    print(color)
    selected_clr = (input("Choose color you want to bet on (red or black): "))
    selected_amm = int(input("Choose ammount you want to bet: "))

    if selected_amm > money:
        print("You are too poor for this!")
        break

    print("The color is " + color)

    if selected_clr == color:
        money = money + selected_amm
        print("You have won! Your current ammount is: ")
        print(money)
    else:
        money = money - selected_amm
        print("You have lost! Your current ammount is: ")
        print(money)

    repeat = (input("Do you want to play again?  (yes/no) "))