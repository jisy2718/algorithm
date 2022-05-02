import sys
sys.stdin = open('1232_input.txt')

def operation(left_num, result, right_num):
    if result == '-':
        return (left_num - right_num)
    elif result == '+':
        return (left_num + right_num)
    elif result == '/':
        return (left_num / right_num)
    elif result == '*':
        return (left_num * right_num)


def cal(v):
    if v <= N:
        result = tree[v] # v 노드의 값. 숫자면 return하고, 연산자면 자식탐색
        child1_idx = child1[v]
        child2_idx = child2[v]

        # Base case
        # 현재 노드가 숫자인 경우, return 하여 연산 준비(자식없음)
        if type(result) == int:
            return result

        else: # 현재 노드가 연산자인 경우 : 자식 무조건 2개 있음
            left_child = cal(child1_idx) # 왼쪽 아래 숫자
            right_child = cal(child2_idx) # 오른쪽 아래 숫자
            result = operation(left_child, result, right_child) # 연산

            # 자신의 값을 바꾸기
            tree[v] = result

    return result


T = 10
for tc in range(1,T+1):
    N = int(input())
    # 1. input 형식
    # 노드 idx , 양의정수(or 연산자) , 자식1 idx, 자식2 idx
    infos = [list(input().split()) for _ in range(N)] # 연산자 있으므로, 정수로 못바꿈

    # 2. 트리만들기
    tree = [0]*(N+1) # index가 노드이고,tree 내부의 값이 노드의 value
    child1 = [0]*(N+1)
    child2 = [0]*(N+1)
    # 트리 채우기
    for info in infos:
        # 연산자인 경우
        if info[1] in ['-','+','/','*']:  # 연산자는 무조건 자식 2개 가짐
            tree[int(info[0])] = info[1]
            child1[int(info[0])] = int(info[2])
            child2[int(info[0])] = int(info[3])

        else: # 숫자인경우 / 숫자는 무조건 자식 안 가짐
            tree[int(info[0])] = int(info[1])

    #### tree 완성

    # 3. post_order 로 진행
    # (1) 숫자가 나올 때까지 계속 내려가기 (연산자는 무조건 자식2개 있음)
    # (2) 자식1(숫자), 연산자(부모), 자식2(숫자) 가 되도록 한 후 연산 후 부모에 저장
    print(f'#{tc} {int(cal(1))}')






