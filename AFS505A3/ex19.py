def cheese_and_crackers(cheese_count, boxes_of_crackers):
#this section does not actually print anything in the output
    print(f"You have {cheese_count} cheeses!")
    print("You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket. \n")
# this line prints the words plus the statements above with the numbers below
    print("We can just give the function numbers directly:")
    cheese_and_crackers(20, 30)
# this prints in the same format of the words above given the numbers below in the command
    print("OR, we can use variables from our script:")
    amount_of_cheese = 10
    amount_of_crackers = 50
# this gives new variables (objects)
    cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# this line uses the new variables of amounts
    print("WE can even do the math inside too:")
    cheese_and_crackers(10+ 20, 5+6)
# this line combines the variables with the math
    print("And we can combine the two, variables and math:")
    cheese_and_crackers(amount_of_cheese + 100, amount_of_crackerse + 1000)
