# Operators (Arithmetic, Assignment, Comparison, Logical, usw..)


#1 Arithmetic (+, -, /, *, //, %, **)

#1 Assignment (=, +=, -=, /=, *=, %=, //=, **=)

#2 Comparison (==, !=, >, >=, <, <=)

#2 Logical (not, or, and)

# usw.. (if else, is, is not, in, not in, ...)


#1
health = 50
health += 20
new_health = health + 20
print(new_health)
Modx = 5
print(Modx ** 5)

first_name = 'Sylvanas '
last_name = 'windrunner'
print(first_name + last_name)

testnum_1 = '42'
testnum_2 = '8'
print(testnum_1 + testnum_2)

#2

print(4 == 5)
print(5.0 == 5)
print(1 == True)

a = 'c'
b = 'bb'
print(a == b)
print(5 > False)

is_game_over = False
is_game_over = not is_game_over
print(is_game_over)

health = 0
lives = 1
print(health <= 0 and lives <= 0)
print(health <= 0 or lives <= 0)

