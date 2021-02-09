from sys import exit

def blue_box():
    print(f"This room is full of cupcakes, how much do you take?")
    choice = input ("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("oopsie")

    if how_much < 7:
        print(f"Wow that is half a bakers dozen or less")
        exit(0)
        # i do not understand the exit commands
    else:
        dead("Thats a lot of cupcakes!")

def blue_box():
    print("There are a lot of cupcakes here")
    print("The cupcakes have a bunch of sprinkles")
    print("The sprinkles are very crunchy")
    print("How are you going to avoid the crunch?")
    cupcakes_eaten = False

    while True:
        choice = input("> ")
        if choice == "eat sprinkles":
            dead("You broke a tooth on a sprinkle")
        elif choice == "remove sprinkles" and not cupcakes_eaten:
            print("The sprinkles are now gone")
            print("But now the frosting is gone too")
            cupcakes_eaten = True
        elif choice == "eat sprinkles" and cupcakes_eaten:
            dead("Sprinkles eaten and no teeth are broken.")
        elif choice == "remove sprinkles" and cupcakes_eaten:
             gold_room()
        else:
             print("Cupcakes are yummy!")
