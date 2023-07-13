
# Define your own function
def my_first_function(a, b, c):
  return((a * 3 + b * 2 + c) ** 2)

# Testing the function
print(my_first_function(5,4,3))


# Define a function
def is_odd(n):
  if n % 2 == 0:
    return "even"
  else:
    return "odd"

# Testing function
print('2 is', is_odd(2))
print('3 is', is_odd(3))


# Define a function
def is_positive(n):
  if n > 0:
    return('positive')
  elif n < 0:
    return('negative')
  else:
    return('zero')

# Test your function on -5, 0 and 5
print('Number -5 is', is_positive(-5))
print('Number 0 is', is_positive(0))
print('Number 5 is', is_positive(5))


# Data
countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
                  'Germany': (357114, 83783942), 'Brazil': (8515767, 212559417), 
                  'India': (3166391, 1380004385)}

# Defining a function
def country_information(d, name):
  print('Country:', name)
  print('Area:', d[name][0], 'sq km')
  print('Population:', round(d[name][1]/1000000, 2), 'MM')

# Testing the function
country_information(countries_dict, 'Brazil')
country_information(countries_dict, 'Germany')



# People dictionary
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Define the function
def people_information(d, name):
  print("Name:", name)
  print("Age:", d[name][0], "y.o.")
  print("Height", d[name][1], "cm")

# Testing the function
people_information(people_d, "Alex")
people_information(people_d, "Michelle")