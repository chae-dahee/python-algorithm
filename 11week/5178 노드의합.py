import sys
sys.stdin = open('5178_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    V, howmany, position = map(int, input().split())     #V=5, L=3, where=2

    Tree = [0 for _ in range(1000)]     #V+1로 두면 입력배열만큼 나올 수 있는데,, 문제에서 1000이하의 자연수라고 선언함

    for i in range(howmany):
        where, what = map(int, input().split())     #where=4, what=1
        Tree[where] = what

    for i in range(V-howmany,0,-1):
        Tree[i] = Tree[i*2] + Tree[i*2+1]   #LC(1) + RC(2) = 3

    print(f'#{tc} {Tree[position]}')