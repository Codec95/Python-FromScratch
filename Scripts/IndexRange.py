
# Initial list
values = [1, [2, 3], 4, "code"]

# Initialize a for loop over indexes
for i in range(len(values)):
  print("Index:", i)
  print("Value:", values[i])
  print("----") # Delimiter


# Countries data
countries = [['USA', 9629091, 331002651], ['Canada', 9984670, 37742154], 
['Germany', 357114, 83783942], ['Brazil', 8515767, 212559417], ['India', 3166391, 1380004385]]


# Iterate over list
for country in countries: 
  # Iterate over nested list
  for j in country:
    print(j, end = ' ')
  print('\n') # Print new line after nested loop finish

# Initial data
countries = [["USA", 9629091, 331002651], ["Canada", 9984670, 37742154],
            ["Germany", 357114, 83783942], ["Brazil", 8515767, 212559417],
            ["India", 3166391, 1380004385]]

# Iterating over external list
for i in range(len(countries)):
    if type(countries[i]) is list:
        # Computing population density for a country
        pop_dens = round(countries[i][2]/countries[i][1], 2)
        print(countries[i][0], pop_dens, 'people per km²')


# Data
people = [["Alex", 178], ["Noah", 189], ["Peter", 175], ["John", 185], ["Michelle", 165]]

# Iterating over external list
for i in range(len(people)):
    if type(people[i]) is list:
        # Calculate and round height in inches
        ht_in = round(people[i][1]/2.54, 2)
        print(people[i][0], 'has height of', ht_in, 'inches')