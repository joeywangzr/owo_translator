print("hewoo uwu owo")

def owo(phrase):
    translation = ""
    for letter in phrase:
        if letter in "rl":
            translation = translation + "w"
        elif letter in "RL":
            translation = translation + "W"
        else:
            translation = translation + letter
    return translation 

print(owo(input("Input a phwase: ")))