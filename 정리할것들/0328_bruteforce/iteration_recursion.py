# 1. selection sort

def selectionsort_iter(A):

    for i in range(len(A)):
        minI = i
        for j in range(i,len(A)):
            if A[minI] > A[j]:
                minI = j
        A[i], A[minI] = A[minI], A[i]

    return

def selectionsort_recur(A,s,e):
    if e-s == 1:
        return

    print(A)

    minI = s
    for i in range(s,e):
        if A[i] < A[minI]:
            minI = i
        A[s], A[minI] = A[minI], A[s]

    selectionsort_recur(A,s+1,e)


A = [5,4,3,2,1]
selectionsort_recur(A,0,len(A))
# selectionsort_iter(A)
print(A)

