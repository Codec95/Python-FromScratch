launcher_cluster = ('Steam', 'Epic', 'Origin', 'PSN', 1024)
print(launcher_cluster)

buffer_size = launcher_cluster[4]
print(buffer_size)

steam = launcher_cluster[0]
print(steam)

#not able to add or change in tuples (immutable)

#launcher_cluster.append('Test')
#print(launcher_cluster)

####################

files = {'engine.ini': 2, 'default_game.ini': 3, 'game.ini': 4, 2: 'test'}
print(files)

print(len(files))
#print(max(files))
#(min(files))

files['visual.ini'] = 20
print(files)
#files.pop('visual.ini')
#print(files)

print(files.get('visual.ini'))
print(files.keys())
print(files.values())

list = [['test'],['realm']]

#list.append('2')
print(list)
#list.clear()
#list.insert(1, '3')
print(list)
#list.remove('test')
print(list)
#list.pop()
print(list)

list[1].append('test')
print(list)

health = 0
life = 0

print(health <= 0 and life <= 0)

