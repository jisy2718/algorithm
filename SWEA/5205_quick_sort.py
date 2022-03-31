def quick_sort(A,left,right):
    if left >= right:
        return

    pivot_index = partition(A,left,right)
    quick_sort(A,left, pivot_index-1)
    quick_sort(A,pivot_index+1, right)

def partition(A,left,right):
    # print(f"before {A}, pivot index{left}, value{A[left]}")
    pivot = A[left]
    i = left
    j = right
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i < j :
            A[i], A[j] = A[j],A[i]

    A[left], A[j] = A[j],A[left]
    # print(f"after : pivot is {pivot}", A)
    #print(A)
    return j


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    quick_sort(A,0,N-1)
    print(f"#{tc} {A[N//2]}")

