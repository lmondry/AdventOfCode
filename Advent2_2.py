f = open('data/data.txt','rb+')

datas = []
numOfDiff = 0

for i in f:
    datas.append(i)

for data1 in datas:
    for data2 in datas:
        numOfDiff = 0
        for index,letter in enumerate(data1):
            if letter != data2[index]:
                numOfDiff = numOfDiff+1

        if numOfDiff == 1:
            print data1,data2
            break
