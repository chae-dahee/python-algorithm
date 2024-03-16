Data = [2,4,7,9,11,19,23]

def FinThis(key):
    start = 0   #시작점 가리킴 2
    end = len(Data)-1   #6 마지막점 가리킴 23
    while start <= end:
        mid = (start + end) // 2  # >>2 같음 mid = 3
        if Data[mid] == key:
            return True
        elif Data[mid] < key:
            start = mid+1   #mid오른쪽을 탐색하겠다. start가 mid 후로 이동
        else: end = mid-1   #mid왼쪽을 탐색하겠다. end가 mid 전으로 이동
    return False

key = 2
if FinThis(key):
    print('찾았다')
else:
    print('못찾았다')