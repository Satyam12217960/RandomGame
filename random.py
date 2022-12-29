import random
print("Hey,i am a magician.Let me show you some.")
print("Just guess the number in my mind")

r = random.randint(1,5)

t=3
while t>0:
    n=int(input("Enter a number between 1 to 5:"))
    if n==r:
        print("You have guessed the number correctly")
        for i in range(1, 6):
            for j in range(1,i):
                print("*",end='')
            print()
        break
    else:
        t=t-1
        print("Wrong")
        print("You have only",t,"more tries left")

if t==0:
    print("You lost")

print("Thank you for playing")