
# 1. Funktion

# Name u. Funktion (1)
def print_snake():
  print('My name is Codec95')

# Ausführen Funktion (1)
print_snake()


# 2. Funktion

# Name u. Funktion (2)
def calculate_triangle_perimeter(a, b, c):
    perimeter = a + b + c
    print(f'The perimeter is {perimeter}')

# Ausführen Funktion (2)
calculate_triangle_perimeter(2, 3, 5)


# 3. Funktion

# Name u. Funktion (3)
def calculate_list_sum(list):
    total = 0
    for num in list:
        total += num
    print(total)

# Ausführen Funktion (3)
my_list = [1, 2, 3, 4, 5]
calculate_list_sum(my_list)


# 4. Funktion

# Function to calculate velocity
def calculate_velocity(distance, time):

    velocity = distance / time
    return velocity

# Function to calculate acceleration which uses velocity as argument  
def calculate_acceleration(velocity, time):

    acceleration = velocity / time
    return acceleration


distance = 100
time = 10

# Calculate velocity
velocity = calculate_velocity(distance, time)
# Use valocity as the first argument to calculate acceleration
acceleration = calculate_acceleration(velocity, time)

print(f'Velocity: {velocity}')
print(f'Acceleration: {acceleration}')


# 5. Funktion

def calculate_velocity(distance, time):

    velocity = distance / time
    return velocity

def calculate_kinetic_energy(mass, velocity):

    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy


distance = 100  # meters
time = 10  # seconds
velocity = calculate_velocity(distance, time)

mass = 5  # kilograms
kinetic_energy = calculate_kinetic_energy(mass, velocity)

print(f'Velocity: {velocity} m/s')
print(f'Kinetic Energy: {kinetic_energy} Joules')


# 6. Funktion

num_x = 5  #Test
num_y = 2  #Test

def show_test_value(num_x, num_y=2):
	num_z = num_x * num_y
	return num_z

num_z = show_test_value(num_x, num_y)
print(num_z)

def calculate_test_value(num_z, num_y):
	value_2 = num_z + num_y
	value_output = value_2**2
	return value_output

value_output = calculate_test_value(num_z, num_y)
print(value_output)

if value_output == 144:
	print(value_output == 144) # return True

else: 
	print(value_output == 144) # return False


# 7. Funktion

def calculate_interest(principal, rate, years):
    # Check the types of inputs: check if the type of input belongs to values in tuple
    if type(principal) not in (int, float):
        print('Principal amount must be a number.')
        return 0
    
    if type(rate) not in (int, float):
        print('Interest rate must be a number.')
        return 0
    
    if type(years) is not int:
        print('Number of years must be an integer.')
        return 0
    
    # Calculate the compound interest using built-in functions
    amount = principal * (1 + rate/100) ** years
    interest = amount - principal
    
    # Round the interest to two decimal places using the built-in round() function
    interest = round(interest, 2)
    
    # Return the calculated interest
    return interest


  
print(calculate_interest(2000, '5', 3))
print(calculate_interest(2000, 5, 3))


# 8. Funktion

def function_simple(task, number=2): # default value of 2
	print(task, 'and', number)

function_simple('hello')


# 9. Funktion

def calculate_total_cost(price, quantity, discount=0, tax_rate=0.1):

    discounted_price = price - (price * discount)
    subtotal = discounted_price * quantity
    total_cost = subtotal + (subtotal * tax_rate)
    return total_cost
  
# Calculate the total cost without discount and with a tax rate of 0.15
cost1 = calculate_total_cost(10, 5, tax_rate=0.15)
print('The first cost is', cost1)

# Calculate the total cost with a 20% discount and the default tax rate
cost2 = calculate_total_cost(10, 5, discount=0.2)
print(f'The second cost is {cost2}') 
    
	
	



