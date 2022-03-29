# 모든 정수에 대한 bubble sort
def bubble_sort(l:list): # 오름차순
    n = len(l)
    for i in range(n-1,0,-1): # 첫 루프 : 비교가 끝나는 부분 인덱스 선정(n-2까지 비교함) : 정렬 구간의 끝
        # 두 번째 루프 : j와 j+1 번째 index를 비교할 것임
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l