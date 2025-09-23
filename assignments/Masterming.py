import random 

#Name = Krzysztof Marcinkiewicz
#ITU_MAIL = krzm@itu.dk

colors = ["B", "Y", "G", "R", "P", "T", "O", "C"]
length = 4
max_attempts = 10

random_color = random.choices(colors, k=length)
attempts = 0 

print("Welcome to the Mastermind Game!")
print(f"You have to pick 4 colors:", colors)


while attempts < max_attempts:
    guess = input(f"Attempts: {attempts}/{max_attempts} Enter Your guess:")
    if len(guess) != 4:
        print("Invalid guess! You have to guess 4 :DDD")
        continue
    
    if any(i not in colors for i in guess):
        print("Please choose from the list :<")


    correct_position = sum(g == c for g, c in zip(guess, random_color))
    correct_color = sum(min(guess.count(c), random_color.count(c)) for c in set(random_color))
    correct_color -= correct_position

    print(f"{correct_position} colors placed correctly")
    print(f"{correct_color} colors placed in wrong positions")

    if correct_position == length:
        print("Congratulations!!! YOU WON 🥳🥳🥳")
        exit()

    attempts += 1


print("You lost 💀💀💀")


