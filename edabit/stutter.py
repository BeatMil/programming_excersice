def stutter(word):
    first_two_letters = word[:2]
    full_text = "%s... %s... %s?"%(first_two_letters, first_two_letters, word)
    return full_text

print(stutter("bob"))
