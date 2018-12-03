f = open('data/data.txt','rb+')

datas = []

numOfTwo = 0
numOfThree = 0

found2 = False
found3 = False

for i in f:
    datas.append(i)

for data in datas:
    found2 = False
    found3 = False

    for letter in data:
        if data.count(letter) == 2 and not found2:
            numOfTwo = numOfTwo + 1
            found2 = True
        if data.count(letter) == 3 and not found3:
            numOfThree = numOfThree + 1
            found3 = True
        if found2 and found3:
            break

print numOfTwo * numOfThree
