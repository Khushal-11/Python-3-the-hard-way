# assigning value 10 to the variable name types_of_people
types_of_people = 10
# assigning a formated string that includes variable types_of_people, to variable x
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# assigning a formated string that has varibles binary and do_not, to variable y
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# assigning a boolean value to variable hilarious
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# another way to format a string: inserting the value of variable hilarious inside the string of variable joke_evaluation, and printing it
print(joke_evaluation.format(hilarious))

w = "This is a left siede of ..."
e =  "a string with a right side."

# here + is not addition instead it is concatenation of two strings w and e
print(w + e)
