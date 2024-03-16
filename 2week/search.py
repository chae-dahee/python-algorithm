Data=[4,9,11,23,2,19,7]

key = 2

for i in range(len(Data)):
    if Data[i] == key:
        print(i+1)  #배열이어서 +1
        break