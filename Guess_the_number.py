#Hi, welcome to my game of guessing numbers
import random
guess=0
print("Welcome to my game of guessing numbers")
print("Choose:\n1)User guessing \n2)Computer Guessing ")
choice=int(input())# taking choice from user
if (choice==1 ):
    print("User guessing\n")

    print("You will have to guess my number\n")


    # print()
    def user_guess(x):
        random_num = random.randint(1, x)
        # print("Random number:", random_num)
        guess = 0
        while guess != random_num:
            guess = int(input(f"Guess a number between 1 and {x}\n"))
            if guess < random_num & random_num - guess >= 10:
                print("Too low")
            elif guess < random_num:
                print("Low")
            elif guess > random_num & guess - random_num >= 10:
                print("Too high")
            else:
                print("High")

        print(f"Congo, you have guessed the number {guess}  correctly ")


    user_guess(20)
else:
    def computer_guess(x):
        low = 1
        high = x
        feedback = ' '
        print("Hello,now I will guess values for you in range 1 to ", x)
        print("\nEnter the integer value you want me to guess")
        rand_num=int(input())
        while(rand_num >high or rand_num<low):
            print("\nPlease enter a valid value within range")
            rand_num=int(input())

        print(f"Number to be guessed by computer :{rand_num}")
        # print("Feedback required:\n1)th- too high if guess- high>5\n2)tl- too low if guess- low- guess>5\n3)h- high4)l-low")
        # feedback = input()

        while feedback != 'c':
            guess = random.randint(low, high)
            print(f"Is the number {guess} high(h) or low(l) or toolow (tl) or too high (th) or correct(c) ?\n")
            feedback = input()


            while feedback != 'h' and feedback != 'l' and feedback != 'th' and feedback != 'tl' and feedback != 'c':
                    print("Enter a valid feedback to help the computer")
                    feedback = input()

            if low != high:
                    if feedback == 'h':
                        high = guess - 1  # changing the range according to user
                    elif feedback == 'l':
                        low = guess + 1
                    elif feedback == 'th':
                        high = guess - 5
                    elif feedback == 'tl':
                        low = guess + 5
                    else:
                        print("\nYah, I guessed your number correctly")





    computer_guess(25)


















