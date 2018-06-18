import random



randomNo = random.randint(1,10)
while True:
    guessNo = input("Please Guess the number (\"q\" to exit): ")
    if str(guessNo) == "q":
        break
    elif int(guessNo) == int(randomNo):
        print("Correct!")
        break
    elif (int(guessNo) != int(randomNo) and int(guessNo) != "n"):
        print("Wrong, try again! ")








