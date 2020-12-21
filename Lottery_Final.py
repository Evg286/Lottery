import random
from time import sleep

print("Welcome to the lottery \n")
sleep(1)
money = int(input("Enter how much money you would like to spend: \n"))
if money < 3:
    print("\nGo away!")
    exit()
turns = (money//3)
change = (money % 3)

print("You have " + str(turns) + " turns and " + str(change) + " ILS left in change")

lot_nums = []
for i in range(0, 6):
    num = random.randint(1, 37)
    while num in lot_nums:
        num = random.randint(1, 37)
    lot_nums.append(num)

prize = 0

for i in range(turns):
    user_nums = []

    print("\nRound " + str(i+1) + ":\n")

    for j in range(0, 6):
        num = int(input("\nEnter a number from 1 to 37: "))
        while num in user_nums:
            sleep(1)
            print("\nYou have already used this number. Please choose a new one!\n")
            num = int(input("Enter a number from 1 to 37: "))
        while num < 1 or num > 37:
            sleep(1)
            print("\nYou may only enter numbers from 1 to 37!\n")
            num = int(input("Enter a number from 1 to 37: "))
        user_nums.append(num)

    print("\nYour numbers are: \n")
    print(user_nums)

    counter = 0

    for num in user_nums:
        if num in lot_nums:
            counter += 1
            prize = 0

    if counter < 3:
        sleep(1)

    elif counter == 3:
        prize = (prize + 10)
        sleep(1)

    elif counter == 4:
        prize = (prize + 100)
        sleep(1)

    elif counter == 5:
        prize = (prize + 5000)
        sleep(1)

    elif counter == 6:
        prize = (prize + 1000000)

print("\nThe winning numbers are: \n")
print(lot_nums)

print("\nYour total prize: " + str(prize))
