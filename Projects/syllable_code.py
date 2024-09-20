def syllable_count(word):
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            if word.endswith("e"):
                count -= 1
    if count == 0:
        count += 1
    return count



while True:
    word = input("WHat do you think grandma likes?")

    if syllable_count(word) > 2:
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma likes {word}")

    print("")
