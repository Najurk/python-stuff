import random #this will import a random number

num = random.randint(1, 100)

while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('Exactly right!')
        break
    elif i < num:
               print('Too low')
    elif i > num:
               print('Too high')
