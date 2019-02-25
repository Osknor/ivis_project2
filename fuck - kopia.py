



old_data = open("ble.txt").read().split('\n')
array = []
for i in old_data:
    bel = i.split("  ")
    array.append(bel)

print (array)

settet = {"Yellow","Banana"}
for sak in array:
    settet.update(sak)
annanarray = []
array2 = []
for setSak in settet:
    c2 = 0
    for year in array:
        if (setSak in year):
            c2 += 1
    array2.append([setSak,c2])
print (array2.sort())
c3 = 0
for inne in array2:
    if (inne[1]>= 3 ):
        annanarray.append(inne[0])
        print(inne[0])
        c3 += 1
print (annanarray)
print (c3)
'''
settet.update(old_data)
array = []
array2 = []
counter = 0
for i in settet:
    c2 = 0
    for j in old_data:
        if (i == j):
            c2 += 1
    array.append([i,c2])
    array2.append(i)
c3 = 0
for hej in array:
    if (hej[1] == 4):
        print (hej[0])
        c3 += 1



print (c3)
array2.sort()
#print(array2)
'''