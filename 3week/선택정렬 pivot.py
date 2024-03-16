Data = [3,2,5,4,1]

howmany = len(Data)

for pivot in range(howmany):
    min = pivot
    for where in range(pivot+1, howmany):
        if(Data[where]<Data[min]):
            min = where
    Data[pivot], Data[min] = Data[min], Data[pivot]

print(Data)