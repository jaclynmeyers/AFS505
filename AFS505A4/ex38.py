ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("wait there are not 10 things in that list, lets fix it.")

stuff = ten_things.split(' ')
more_stuff = ['day', 'night', 'frisbee', 'song', 'corn', 'banana', 'girl', 'boy']
# splits more things into stuff + things and adds these items to the list
while len(stuff) != 10:
    # means stuff does not equal 10
    next_one = more_stuff.pop()
    # call pop on more stuff
    print("Adding: ", next_one)
    stuff.append(next_one)
    #calls append on stuff
    print(f"There are {len(stuff)} items now")

print("There we go: ", stuff
# prints stuff as a list

print("Lets do some things with stuff")

print(stuff[1])
print(stuff[-1])
# prints number 1 which is also -1

print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
