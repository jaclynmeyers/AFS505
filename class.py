tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


from sys import argv
script, age, height, weight
print("The script is called:", script)
print("How old are you?: ", first)
print("How much do you weigh?: ", second)
print("How tall are you?: ", third)

from sys import argv
script, first, second, third = argv
print("The script is called:", script)
print("How old are you?: ", first)
print("How much do you weigh?: ", second)
print("How tall are you?: ", third)
