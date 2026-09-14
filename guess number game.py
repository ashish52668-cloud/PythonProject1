while True:
    import random
    n = random.randint(1,100)
    x = -1
    guesses = 1
    while (x != n):
        x = int(input("Guess the number:"))
        if(x>n):
            print("Lower number please")
            guesses+=1
        elif(x<n):
            print("Higher number please")
            guesses+=1

    print(f"You have guessed the number {n} correctly in {guesses} attempts")