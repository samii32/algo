import sys
sys.stdin = open('삽입정렬.txt')

arr = [*map(int, input().split())]

for i in range(1, len(arr)):
    for j in range(i,0,-1): # i부터 정렬된곳들을 살펴준다
        if arr[j]<arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else: # 더 작은 숫자를 만나면 멈춤
            break
print(arr)