def bubble_sort(target, N):
    # 1. 인접한 요소 2개씩 비교해서 큰 것 뒤로 보내기
    # 2. 1번 모든 요소에 대해서 다 실행하면, 가장 큰 수가 제일 뒤로 감
    # 1~2 번을 N-1 번 반복하면 전체 요소에 대해서 정렬 완료
    for i in range(N-1):
        for j in range(N-1-i): # 반복될때마다 숫자가 1개씩 자리를 찾음
            if GNS_dict[target[j]] > GNS_dict[target[j+1]]:
                target[j], target[j+1] = target[j+1], target[j]  #위치교환
    return target


    # 가장 작은 것 찾아서, 앞에서부터 채워 넣기
def select_sort(target, N):
    # 0번부터 N-1 번까지 자리에 들어갈 요소를 순서대로 찾아서 넣어주기
    for i in range(N-1): # 맨 마지막자리는 N-1번째 루프에서 같이 채워짐
        min_index = i # i번째 들어갈 요소 찾아서 i번째 넣어주기
        for j in range(i+1,N):
            if GNS_dict[target[min_index]] > GNS_dict[target[j]]:
                min_index = j
        target[i] , target[min_index] = target[min_index], target[i]

    return target



def counting_sort(target, N):
    # 각 요소가 몇개씩 나왔는지 개수를 세고
    # 각 요소가 들어갈 자리를 계산하기 위해서 누적합을 구함
    # 각 요소가 들어갈 자리에 넣어줌.
    count = [0]*10           # 요소중 최대값- 최소값 +1 만큼의 길이 필요
    result = [None]*N   # target 요소 정렬해서 반환할 배열
    for i in range(len(target)):
        count[GNS_dict[target[i]]] += 1
    print(f"count : {count}")
    # 요소가 들어갈 자리를 계산하기 위해 누적합 계산
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # 각 자리에 넣어줌
    for i in range(N):
        print(f"result : {result}")
        result[count[GNS_dict[target[i]]] -1] = target[i]
        count[GNS_dict[target[i]]] -= 1
        print(i)

    return result

GNS_dict = { alien : human for human, alien in enumerate(["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"])}



# T = int(input())
# for _ in range(T):
#     tc, N = input().split()
#     N = int(N)
#     target = input().split()
#
#     target = counting_sort(target, len(target))
#     print(tc,*target)








# print(GNS_dict)




target = ["TWO", "NIN", "TWO", "TWO", "FIV", "FOR" ]
N = len(target)


print(counting_sort(target,N))1
#print(target)
#bubble_sort(target,N)
#print(target)


