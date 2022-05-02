def quick_sort(L,left,right):
    # 피벗을 선정하고
    # 피벗을 기준으로 큰값과 작은값으로 구분 후
    # 작은 부분 정렬
    # 큰 부분 정렬
    if left < right:
        # print(L)
        pivot_loc = partition(L,left,right)
        quick_sort(L, left, pivot_loc-1)
        quick_sort(L, pivot_loc+1, right)

def partition(L,left,right):
    pivot = L[left]
    i = left
    j = right
    while i <= j:
        while i <= j and L[i] <= pivot:
            i += 1
        while i <= j and pivot < L[j]:
            j -= 1
        if i < j:
            L[i],L[j] = L[j],L[i]

    L[left], L[j] = L[j], L[left]
    return j

L = [1,3,2]
quick_sort(L,0,len(L)-1)
print(L)