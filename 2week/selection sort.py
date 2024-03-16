Data = [3,2,5,4,1]

def getMin(start, end):
    min = Data[start]
    wheremin = start    #0이 아니라 start로 둬서 오류 해결..!!
    for i in range(start,end+1):
        if Data[i] < min:
            min = Data[i]
            wheremin = i
    return wheremin


for here in range(len(Data)-1):
    where = getMin(here,4)  #지금시점0부터
    Data[here], Data[where] = Data[where], Data[here]

print(Data)