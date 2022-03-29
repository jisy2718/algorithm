K = int(input())
for _ in range(K):
    # 1. input &
    V, E = map(int, input().split())

    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        arr[v1][v2] = 1
        arr[v2][v1] = 1

    # 2. 전체 노드를 순환하면서 , group1과 group2로 나눠서 노드 넣어주기
    group1 = set()
    group2 = set()

    flag = "YES"
    for v in range(1, V + 1):
        if v in group1 and v in group2:  # 그룹에 교집합있으면 이분그래프 아님
            flag = "NO"
            break
        for neighbor_v in range(1, V + 1):
            if arr[v][neighbor_v] == 1:
                if v in group1:
                    group2.add(neighbor_v)
                elif v in group2:
                    group1.add(neighbor_v)

                else:
                    group1.add(v)
                    group2.add(neighbor_v)

        if group1.intersection(group2):  # 그룹에 교집합있으면 이분그래프 아님
            flag = "NO"
            break
    print(flag)