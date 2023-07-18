
var1 = 91400000
var2 = 238855

# Print the corrected variables
print("The initial var1 was 91,400,000 and the corrected is:", var1)
print("The initial var2 was 238 855 and the corrected is:", var2)


first_number = 238855
# Present the first number in scientific notation
first_number_e = "{:.4e}".format(first_number)

second_number = 67000000
# Present the second number in scientific notation
second_number_e = "{:.2e}".format(second_number)

print(first_number_e, second_number_e)

# Calculate the number of task that will be completed
completed = 60 // 7
# Calculate the number of minutes that will left
minutes = 60 % 7

# Print the result
print("The number of completed tasks is", completed)
print("The number of remaining minutes is", minutes)


completed = 60 // 7
minutes = 60 % 7
# Calculate the number of remaining tasks
remaining_tasks = 10 - completed
# Calculate how many minutes you need to complete all tasks
required_time = 10 * 7

# Print the result
print("The number of remaining tasks is", remaining_tasks)
print("The number of minutes for completing the tasks is", required_time)