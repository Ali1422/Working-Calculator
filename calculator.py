import time
print("Welcome to Kala's calculator")
while True:
    print("\nHere are the options")
    options = input("please enter 1 for addition, 2 for subtraction, 3 for division and 4 for multiplacation")
    if options == "1" :
        time.sleep(2)
        print("\n you have chosen addition")
        num1 = int(input("please enter a number"))
        num2 = int(input("please enter another number"))
        addition = num1 + num2
        print ("The answer to your sum is", addition)
        time.sleep(2)
        print("Thank you for feeding me summs daddy uwu, please run me again to give me your cummie wummies")
    elif options == "2":
         time.sleep(2)
         print("\n you have chosen subtraction")
         num1 = int(input("please enter a number to subtract from"))
         num2 = int(input("please enter a number to take away"))
         subtraction = num1 - num2
         print("The answer to your sum is",subtraction)
         time.sleep(2)
         print("Thank you for feeding me summs daddy uwu, pleased run me again to give me your cummie wummies")
    elif options == "3":
        time.sleep(2)
        print("\n you have chosen division")
        num1 = int(input("please enter a number to divide by"))
        num2 = int(input("please enter the number you would like it divided by"))
        division = num1/num2
        print("the answer to your sum is",division)
        time.sleep(2)
        print("Thank you for feeding me summs daddy uwuw, please run me again to give me your cummie wummies")
    elif options == "4":
        time.sleep(2)
        print("\n you have chosen multiplacation")
        num1 = int(input("please enter a number"))
        num2 = int(input("please enter another number"))
        multiplacation = num1 * num2
        print("the answer to your sum is",multiplacation)
        time.sleep(2)
        print("Thank you for feeding me summs daddy uwuw, please run me again to give me your cummie wummies")
    else:
        print("YOU DARE OPPOSE ME MORTAL! YOU BUFFON, YOU FOOL, YOU ABSOLUTE PEASENT! DO YOU NOT KNOW OF YOUR GODS")
        time.sleep(5)
        print("there are some things that are scarier then God")
               
               
