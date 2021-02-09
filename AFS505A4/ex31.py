print (""" You walk into a room with two doors. Do you go through #1 or #2""")

door = input ("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear == input ("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
   elif bear == "2":
       print("The bear eats your legs off. Good job!")
   else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare at an endless abyss at the retina.")
    print("1. blueberries.")
    print("2. yellow jacket clothes pins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity == input ("> ")
    if insanity == "1" or insanity == "2":
        print(" Your body survives powered by a mind full of jello")
        print("Good Job!")
    else:
        print("The insanity rots your eyes in a pool of muck.")
        print("Good Job!")

else:
    print("You stumble around and fall on a pile of knives. Good Job!")
