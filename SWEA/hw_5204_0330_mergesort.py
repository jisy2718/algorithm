# 1. 배열이용

def merge_sort1(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort1(L[:mid])  # 리스트 복사해서 넘기므로 메모리 O(n)만큼 필요
    right = merge_sort1(L[mid:])  # 이렇게 슬라이싱 하면, 여기서도 n 만큼 시간 듦

    return merge(left, right)


def merge(left, right):
    global cnt
    l, r = 0, 0  # k는 삽입되는 index 위치
    result = []  # 결과 내보내는 것도 메모리 필요

    if left[-1] > right[-1]:
        cnt += 1

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
def merge_sort2(L, start, end):
    if start == end:
        return [L[start]]
    mid = start + (end - start) // 2 # 짝수일 때, 좌측 mid 선택

    left = merge_sort2(L, start, mid)
    right = merge_sort2(L, mid + 1, end)
    return merge(left, right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    L = list(map(int,input().split()))
    cnt = 0
    sorted_L = merge_sort1(L)
    print(f"#{tc} {sorted_L[N//2]} {cnt}")