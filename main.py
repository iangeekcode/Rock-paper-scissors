choice = int(input("Choose between 1 sicssors, 2 paper, and 3 rock"))
choice = 3

# Rock Paper Sicssors

randomnumber = random.randint(1,3)
randomnumber = 2

1 = scissors
2 = paper
3 = rock

if choice == 1:
    print("You used sissors")
elif choice == 2:
    print("You used paper")
elif choice == 3:
    print("You used rock")

if randomnumber == 1:
    print("computer used scissors")
elif randomnumber == 2:
    print("computer used paper")
elif randomnumber == 3:
    print("computer used rock")




if choice == 3 and randomnumber == 3:
    print("You tied!")
if choice == 2 and randomnumber == 2:
    print("You tied!")
if choice == 1 and randomnumber == 1:
    print("You tied!")
if choice == 1 and randomnumber == 2:
    print("You won!")
if choice == 2 and randomnumber == 3:
    print("You won!")
if choice == 3 and randomnumber == 1:
    print("You Won!")
if choice == 2 and randomnumber == 1:
    print("You Lost!")
if choice == 3 and randomnumber == 2:
    print("You Lost!")
if choice == 1 and randomnumber == 3:
    print("You Lost!")