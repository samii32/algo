array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, s, e):
    if s>=e: #원소가 1개인 경우 종료!
        return
    pivot = s # 첫번째 원소가 기준 피봇
    l = s+1
    r = e
    #l부터 오른쪽으로 가면서 pivot보다 큰값을 찾는다.
    #r부터 왼쪽으로 가면서 pivot보다 작은값을 찾는다.
    while l<=r:
        #오른쪽으로 가면서 pivot보다 큰걸 발견할때까지!
        while l <= e and array[l] <= array[pivot]:
            l += 1
        #왼쪽으로 가면서 pivot보다 작은걸 발견할때까지!
        while r > s and array[r] >= array[pivot]:
            r -= 1
        if l>r: #커서가 엇갈릴때 기준피봇값과 작은값(r) 서로 자리 교체
            array[r], array[pivot] = array[pivot], array[r]
        else: #엇갈리지 않았으면 r, l 값 자리 교체
            array[l], array[r] = array[r], array[l]
        # 분할 되고 나면 기준피봇값 왼쪽은 무조건 기준피봇값보다 작다.
        # 또한 오른쪽은 무조건 기준피봇값보다 크다.
        # 왼쪽과 오른쪽을 다시 재귀로 정렬을 수행해준다.
        quick_sort(array,s,r-1)
        quick_sort(array,r+1,e)

print(array)
quick_sort(array,0,len(array)-1)
print(array)

#머지솔트도 확인하기!





