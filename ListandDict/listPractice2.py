heroes = ['iron man', 'hulk', 'black widow', 'thor', 'captain america', 'hawk eye']
heroes[1] = 'doctor strange'
print(heroes)

heroes.append('spider man')
heroes.insert(1, 'black panther')
print(heroes)

if 'black widow' in heroes:
    heroes.remove('black widow')
print(heroes)
