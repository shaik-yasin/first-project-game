#Now I am making a Snake_Water_Gun game project 

'''constant values in game
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1, 0, 1])             # it takes random values from constant values in game (1,-1,0).
My_choice = input("Enter your choice:  ")      # input character from user.
MY_Dict = {"s": 1, "w": -1, "g": 0}
reverse_Dict = {1: "Snake", -1: "Water", 0: "Gun"}

My_new = MY_Dict[My_choice]

# By now we have 2 numbers (Variables), you and computer.

print(f"you chose {reverse_Dict[My_new]}\nComputer chose {reverse_Dict[computer]}")

if(computer == My_new):                        # if computer and you are choosing same str it will draw.
    print("Its a draw ")

else:
    if(computer ==-1 and My_new ==1):
        print("You win!!")
    
    elif(computer ==-1 and My_new ==0):
        print("You lose!! ")

    elif(computer ==1 and My_new ==-1):
        print("You lose!! ")

    elif(computer ==1 and My_new ==0):
        print("You Win!! ")

    elif(computer ==0 and My_new ==-1):
        print("You Win!! ")

    elif(computer ==0 and My_new ==1):
        print("You lose!! ")

    else:
        print("Something went wrong!! ")         # if user input beyond the given conditions it will print this.
