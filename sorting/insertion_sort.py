def insertion_sort(arr:list):

    # 해당 인덱스 미만 정렬됨
    for i in range(1,N):
    # 해당 인덱스 미만과 해당 인덱스 비교
        for j in range(i-1,-1,-1):
            # 좌측 것이 더 크면, 해당 인덱스 i의 값을 좌측으로
            if arr[j] > arr[i]:
                # 현재 비교하는 대상이 j 인덱스로 옮겨짐
                arr[j], arr[i] = arr[i], arr[j]
                i = j
            # 왼쪽의 수가 오른쪽보다 크지 않을 경우, 해당 인덱스 i 에 대한 정렬 끝
            else:
                break
    return arr