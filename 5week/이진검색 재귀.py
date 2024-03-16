import sys
sys.stdin = open('input.txt', 'r')

def binarySearchR(start, end, key):
    if start > end: return False
    middle = (start+end)//2     #(start+end)>>1
    if key == Data[middle]:     #검색성공
        return True
    elif key < Data[middle]:
        return binarySearchR(start, middle-1, key)   #재귀
    elif key > Data[middle]:
        return binarySearchR(middle+1, end, key)     #재귀

Data = list(map(int,input().split()))
Data.sort()

key = 55
x=binarySearchR(0,6, key)
print(x)