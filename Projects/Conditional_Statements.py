while True: 
    word = input("Guess the right words to win! Once you get enough wins try to guess the connection!")

    if "y" in word or "o" in word:
         print(f"You win!")
    else:
        print(f"You lost!")
    print("")
        

    