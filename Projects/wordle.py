import random

# Pick a word at random
word_list = ["cloud", "jokey", "whack", "would", "small", "happy", "glaze", "sadly", "upset", "found", "cares", "loves", "grades", "grate", "joker", "kindle", "paper",]
hidden_word = random.choice(word_list)


    
# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter 
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    # Second letter 
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Third letter 
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
     # Fourth letter 
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
     # Fifth letter 
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

    
print(f"You used {i+1} guesses")

