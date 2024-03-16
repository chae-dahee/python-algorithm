import sys
sys.stdin = open('insert_input.txt', 'r')

Data = list(map(int,input().split()))

for here in range(1,len(Data)):
    key = Data[here]    #key = 2

    where = here-1
    while key < Data[where] and where >= 0:    #where이 0보다 작으면 종료
        Data[where+1] = Data[where]     #옆방으로 이동
        where -= 1
    Data[where+1] = key

print(Data)