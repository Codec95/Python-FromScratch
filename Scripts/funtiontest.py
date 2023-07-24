
# People dictionary
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Update the function
def people_information_mod(x, name):
  if name not in x.keys():
    # Check if name doesn't exist in the dictionary keys
    print("There is no information about", name)
  else:
    print("Name:", name)
    print("Age:", x[name][0], "y.o.")
    print("Height:", x[name][1], "cm")

# Test your function
people_information_mod(people_d, "Alex")
people_information_mod(people_d, "Richard")

