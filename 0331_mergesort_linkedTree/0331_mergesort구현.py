# 1. 배열이용

def merge_sort1(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort1(L[:mid])  # 리스트 복사해서 넘기므로 메모리 O(n)만큼 필요
    right = merge_sort1(L[mid:])  # 이렇게 슬라이싱 하면, 여기서도 n 만큼 시간 듦

    return merge(left, right)


def merge(left, right):
    l, r = 0, 0  # k는 삽입되는 index 위치
    result = []  # 결과 내보내는 것도 메모리 필요


    while l < len(left)  and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1


    result += left[l:] + right[r:]
    return result


# 2. index 이용
def merge_sort2(L,start, end):
    if start == end:
        return [L[start]]
    mid = start + (end - start) // 2 # 짝수일 때, 좌측 mid 선택

    left = merge_sort2(L, start, mid)
    right = merge_sort2(L, mid+1 , end)
    return merge(left, right)


# 3. index 이용
def merge_sort3(L, start, end):
    if start == end:
        return
    mid = start + (end-start) // 2  # 2개 남았을 때, 좌측 mid 선택되도록
    mid = (start+end)//2
    # print(L,start,mid,end)
    merge_sort3(L, start, mid)
    merge_sort3(L, mid+1 , end)      # mid 부터 우측
    merge3(L, start,mid,end)

# merge 해야하는 길이와 같은 리스트 만들어서, merge 후, L에 다시 복사
def merge3(L, start, mid, end):
    result = []
    i = start # left의 시작점
    j = mid+1   # right의 시작점

    while i <= mid and j <= end:
        if L[i] <= L[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(L[j])
            j += 1

    if i == (mid+1):
        result += L[j:end+1]

    if j == end+1:
        result += L[i:mid+1]

    # 결과를 L에 복사
    for i in range(start,end+1):
        L[i] = result[i-start]
    # L[start:end+1] = result

import time
L = [10,9,4,1,5,2,8,1,3,2,1,3,2,1,3,5,5,5,5,66,6,76,3,4532,4,14,21,421,4,214,214,12,321,3235,1,325,43,5,346,34643,234]*100
n = len(L)

s1 = time.time()
for _ in range(100):
    L = [10, 9, 4, 1, 5, 2, 8, 1, 3, 2, 1, 3, 2, 1, 3, 5, 5, 5, 5, 66, 6, 76, 3, 4532, 4, 14, 21, 421, 4, 214, 214, 12,
         321, 3235, 1, 325, 43, 5, 346, 34643, 234] * 100
    merge_sort1(L)
# print(r)
e1 = time.time()


L = [10,9,4,1,5,2,8,1,3,2,1,3,2,1,3,5,5,5,5,66,6,76,3,4532,4,14,21,421,4,214,214,12,321,3235,1,325,43,5,346,34643,234]*1000
s2 = time.time()
for _ in range(100):
    L = [10, 9, 4, 1, 5, 2, 8, 1, 3, 2, 1, 3, 2, 1, 3, 5, 5, 5, 5, 66, 6, 76, 3, 4532, 4, 14, 21, 421, 4, 214, 214, 12,
         321, 3235, 1, 325, 43, 5, 346, 34643, 234] * 100
    merge_sort2(L,0,n-1)

e2 = time.time()


s3 = time.time()
for _ in range(100):
    L = [10, 9, 4, 1, 5, 2, 8, 1, 3, 2, 1, 3, 2, 1, 3, 5, 5, 5, 5, 66, 6, 76, 3, 4532, 4, 14, 21, 421, 4, 214, 214, 12,
         321, 3235, 1, 325, 43, 5, 346, 34643, 234] * 100
    merge_sort3(L,0,n-1)
e3 = time.time()

print(f"{e1-s1:.10f} {e2-s2:.10f}  { e3-s3:.10f}")

