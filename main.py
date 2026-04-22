import random

print("🎮 Guess the Number Game 🎮")
print("1 se 10 ke beech number guess karo")

number = random.randint(1, 10)

while True:
    guess = int(input("Apna guess dalo: "))

    if guess == number:
        print("🎉 Sahi jawab! Tum jeet gaye!")
        break
    elif guess < number:
        print("Thoda bada number try karo")
    else:
        print("Thoda chhota number try karo")
