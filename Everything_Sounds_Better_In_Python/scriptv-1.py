var1 = 100
# Try to redefine the value to 150
var1 = 150

# Print the var1 variable
print(var1)

#########################

string = "My goal is to achieve way beyond what I expected"
# Extract the very last symbol using negative indexation
symbol1 = string[-1]
# Extract the very last symbol using len() function
symbol2 = string[len(string) - 1]

# Print symbols
print("This symbol was get using negative indexation:", symbol1)
print("This symbol was get using len() function:", symbol2)

#########################

string = "Work your way up!"

# Print the index of the letter p
print(string.find('p'))
# Print the index of the letter y
print(string.find('y'))
# Print the index of the letter r
print(string.find('r'))

#########################

string = "It is cool to have a burning desire for studying"

# Find the index of the given words
burning = string.index('burning')
desire = string.index('desire')
studying = string.index('studying')

# Print the index
print("The index of the word burning is", burning)
print("The index of the word desire is", desire)
print("The index of the word studying is", studying)

#########################

string = "It can be painful to learn from mistakes"

# Extract necessary words
painful = string[string.index('painful'):string.index('painful') + 7]
mistakes = string[string.index('mistakes'):string.index('mistakes') + 8]
learn = string[string.index('learn'):string.index('learn') + 5]

# Print the word painful
print(painful)
# Print the word mistakes
print(mistakes)
# Print the word learn
print(learn)

#########################

string1 = "Rome is the capital of France"
string2 = "Brasilia located in Europe"
string3 = "Monkeys eat earphones"

# Make required replacements
new_string1 = string1.replace('Rome', 'Paris')
new_string2 = string2.replace('Europe', 'South America')
new_string3 = string3.replace('earphones', 'bananas')

# Print the first corrected string
print(new_string1)
# Print the second corrected string
print(new_string2)
# Print the third corrected string
print(new_string3)

#########################

string1 = "country"
string2 = "Italy"
string3 = "Ukraine"
string4 = "Egypt"

# Print country: Italy
print(string1 + ":" + " " + string2)
# Print country: Ukraine
print(string1 + ":" + " " + string3)
# Print country: Egypt
print(string1 + ":" + " " + string4)

#########################

variable1 = 0.6e1
variable2 = 28.073983298
variable3 = 4.96e2

# Convert variable1 to integer
integer1 = int(variable1)
# Convert variable2 to integer
integer2 = int(variable2)
# Convert variable3 to integer
integer3 = int(variable3)

# Print converted numbers
print(integer1)
print(integer2)
print(integer3)

#########################

price1 = "456"
price2 = "50"
price3 = "830"

# Increase price1 variable by 15
new_price1 = int(price1) + 15
# Increase price2 variable by 780
new_price2 = int(price2) + 780
# Decrease price3 variable by 90
new_price3 = int(price3) - 90

# Print the new_price1 variable
print(new_price1)
# Print the new_price2 variable
print(new_price2)
# Print the new_price3 variable
print(new_price3)

#########################

print("Number of vertices of a pyramid is " + str(5))

print("Number of Major Arcana cards in divinatory Tarot is " + str(22))

print("Largest number that is not the sum of distinct squares is " + str(128))

#########################

string1 = "Over"
string2 = "8 million"
string3 = "people use Python"

# Print the first string twice
print(string1 * 2)
# Print the second string three times
print(string2 * 3)
# Print the third string once
print(string3)

#########################

# Make this statement equals False
print('C' > 'D')

# Make this statement equals False
print("Codefinity" < "Art")

# Make this statement equals True
print("Programming" > "Data")