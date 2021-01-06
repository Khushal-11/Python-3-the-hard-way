# defining a variable named formatter and assigning it a string of four {}
formatter = "{} {} {} {}"

# printing the variable formatter and replacing its four {} with 1, 2, 3, 4 using format function
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# python recognizes true and false as standard keywords for true and false, so no quates for them
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
