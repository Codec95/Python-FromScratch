# Starting number
a = 3

# Let's construct while loop
while True: # Infinite loop
  if a == 6: # Stopping condition
    print("Number", a, "reached")
    break # This will break loop
  elif a < 6: # If less, than add 2
    a = a + 2
    print("Adding 2... Reached", a)
  else: # If greater, then subtract 1
    a = a - 1
    print("Subtracting 1... Reached", a)



# Create variable
i = 1

# Initialize a while loop
while i >= 9:
  # Print number i squared
  print(i // 4)
  # Increment variable i by 1
  i = i + 1