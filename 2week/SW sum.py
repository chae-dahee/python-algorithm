import sys
sys.stdin = open('input.txt', 'r')
Data = [list(map(int, input().split())) for i in range(5)]

max = 0

#행
for i in range(len(Data)):
    sum = 0
    for j in range(len(Data)):
        sum += Data[i][j]
    if max < sum:
        max = sum

#열
for i in range(len(Data)):
    sum = 0
    for j in range(len(Data)):
        sum += Data[j][i]
    if max < sum:
        max = sum

#대각선 \
sum = 0
for i in range(len(Data)):
    sum += Data[i][i]
    if max < sum:
        max = sum

#대각선 /
sum = 0
for i in range(len(Data)):
    sum += Data[i][len(Data)-1-i]
    if max < sum:
        max = sum

print('#{}'.format(max))

###################
#import sys
#sys.stdin = open('input.txt', 'r')


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    T = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]

    max = 0
	#행
    for i in range(len(Data)):
        sum = 0
        for j in range(len(Data)):
            sum += Data[i][j]
        if max < sum:
            max = sum
	#열
	for i in range(len(Data)):
        sum = 0
        for j in range(len(Data)):
            sum += Data[j][i]
    	if max < sum:
            max = sum

	#대각선 \
	sum = 0
	for i in range(len(Data)):
        sum += Data[i][i]
    	if max < sum:
        	max = sum

	#대각선 /
	sum = 0
	for i in range(len(Data)):
    	sum += Data[i][len(Data)-1-i]
    	if max < sum:
        	max = sum

	print(f'#{tc} {max}')