Data = [2,3,5,4,1]

for i in range(5-1):    #단계
    for j in range(5-i-1):  #거품 이동 횟수
        if Data[j]>Data[j+1]:   #값 비교
            Data[j], Data[j+1]=Data[j+1],Data[j]    #파이썬 swap 문법

print(Data)