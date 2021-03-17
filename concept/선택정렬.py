import sys

sys.stdin = open('선택정렬.txt')
arr = [*map(int,input().split())]
print(arr)

for idx in range(len(arr)):
    min_idx = idx
    for jdx in range(idx+1, len(arr)):
        if arr[min_idx]>arr[jdx]:
            min_idx = jdx
    # idx+1~len(arr)까지 다 돈 다음 스왑
    arr[min_idx], arr[idx] = arr[idx], arr[min_idx]

print(arr)