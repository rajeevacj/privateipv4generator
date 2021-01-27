# Copyright (c) Chi.C.J.Rajeeva Lochana


import random
import time

numberList = [10,0,192,127,172]

def randIPGenerator():
    print("\nThis tool is for informational purposes only.\nI am not responsible for any abuse of this tool.\n\n", end="")
    time.sleep(2.5)
    yesOrNo = str(input("Are you sure you want to generate a random private IPv4 address? (y/n): "));
    print("\n", end="");
    if yesOrNo.lower().strip() == "y" or yesOrNo.lower().strip() == "yes":
        global numberList
        r1 = str(random.choice(numberList))
        if r1 == "10" or r1 == "0" or r1 == "127":
            r2 = str(random.randint(0, 255))
            r3 = str(random.randint(0, 255))
            r4 = str(random.randint(0, 255))
        elif r1 == "192":
            r2 = str("168")
            r3 = str(random.randint(0, 255))
            r4 = str(random.randint(0, 255))
        elif r1 == "172":
            r2 = str(random.randint(16, 31))
            r3 = str(random.randint(0, 255))
            r4 = str(random.randint(0, 255))
        else:
            print("Some error occurred! Please run the script again!\nIf this error continues to happen. Please let us know!\n")
            exit()
        print("Your random private IPv4 address is: " + r1 + "." + r2 + "." + r3 + "." + r4 + "\n", end="")

randIPGenerator()
