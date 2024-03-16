import sys
sys.stdin = open('input.txt', 'r')

howmany = int(input())  #int를 안해주면 문자열 형식

for now in range(1, howmany+1): #1~howmany까지 출력
    if now % 3 == 0:
        print('X', end='')  #console 12X45X7
    else:
        print(now, end='')  #console 1234567