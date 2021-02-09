i = 0
numbers = []

while i < 6:
    print(f"at the top i is {i}")
    numbers.append(i)

    i = i + 4
    print(f"Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")
for num in numbers:
    print(num)

def print_numbers(min, max):
    while min < max:
        print(f"At the top min is '{min}'")
        numbers.append(min)

        min = min + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom min is {min}")
numbers = []
print_numbers(0, 6)
print("The numbers: ")
for num in numbers:
    print(num)
