# collections (Lists, Tuples, Dictionaries, Ranges)

# Lists

inventory = ['sword', 'bow', 'armor']
print(inventory)
print(inventory[0])

bow = inventory[1]
print(bow)

print(max(inventory))
print(len(inventory))
inventory.append('coin')
print(inventory)

inventory.pop()
print(inventory)

inventory.remove('armor')
print(inventory)

# inventory.clear()
print(inventory)


# Lists extra!

bag = [inventory, bow]
print(bag)

overworld = [
    [1, 2, 3],      #0
    [1, 2],         #1
    [1, 2, 3, 4],   #2
    [1, 2]]         #3
print(overworld[2][2])
print(overworld)

overworld[1].pop()
overworld[1].append('Roaster')
print(overworld[1])
