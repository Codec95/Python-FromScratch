
string = "puppy and nestling are babies"

# Assign excluded word puppy to the variable puppy
puppy = string[0:5]
# Assign excluded word nestling to the variables nestling
nestling = string[10:18]

# Print the variable puppy
print(puppy)
# Print the variable nestling
print(nestling)

string = "courage"

# Get these letters using negative indexation
a = string[-3]
g = string[-2]
e = string[-1]

print(a,g,e)

string1 = "Get a foot in the door in programming!"
string2 = "Plug away"
# Extract phrase Get a foot
phrase1 = string1[0:10]
# Extract phrase away
phrase2 = string2[5:9]

# Print the strings and relevant phrases
print("The first string is:", string1)
print("The phrase that was seized is:", phrase1)
print("The second string is:", string2)
print("The phrase that was seized is:", phrase2)

string = "That which does not kill us makes us stronger."
# Extracted symbols from 1 to 12 with the step of 3
sliced_string = string[1:13:2]

# Print the string
print(sliced_string)