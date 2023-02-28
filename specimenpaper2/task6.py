a = []
for _ in range(5):
    name = input()
    a.append(name)
    
placing = a.index('Ellie')
placing = placing + 1
placing = str(placing)

if int(str(placing)[-1]) == 1:
    print(placing + 'st')
elif int(str(placing)[-1]) ==2:
    print(placing + 'nd')
elif int(str(placing)[-1]) == 3:
    print(placing + 'rd')
else:
    print(placing + 'th')
