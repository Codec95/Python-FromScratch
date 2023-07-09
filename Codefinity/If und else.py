
# Assign some variable
test = "small string"

# Conditional statement
if(len(test) > 20):
    print("This string is wide!")
else:
    print("Nothing special")
    
# Check on different string
test = "This string is very-very and very large"

# Conditional statement
if(len(test) > 20):
    print("This string is wide!")
else:
    print("Nothing special")



revenue = 2000

# Check if revenue is less than 2000
if revenue < 2000:
  # Output We suffer losses!
  print('We suffer losses!')
else:
  # Output Everything is ok!
  print('Everything is ok!')



num = 8941 % 931

print(type(num) is float)


revenue = 2000

# Modify your conditional statement
if revenue < 2000:
  print("We suffer losses!")
# Add comparison of revenue with 2000
elif revenue == 2000:
  # Output 'We are breaking even!'
  print("We are breaking even!")
else:
  print("Everything is ok!")



# Defining the number
num = -460807 % 19

# Check if the number num is negative
if num < 0:
  print("The number num is", "negative")
elif num > 0:
  print("The number num is", "positive")
# Otherwise number num equals zero
else: 
  print("The number num", "equals zero")
