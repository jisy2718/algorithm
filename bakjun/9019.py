# bfs로 해결

# 0 <= num <10000 인 정수연산
def D(num):
    return (num*2)%10000

def S(num):
    if num == 0:
        return 9999
    else:
        return num -1
def L(num):
    d4 = num % 10
    d3 = (num % 100)//10
    d2 = (num% 1000)//100
    d1 = num //1000

    return (d2*1000 + d3*100 + d4*10 + d1)

def R(num):
    d4 = num % 10
    d3 = (num % 100) // 10
    d2 = (num % 1000) // 100
    d1 = num // 1000

    return (d4 * 1000 + d1 * 100 + d2 * 10 + d3)

from collections import deque
T = int(input())
for tc in range(T):
    A, B = map(int,input().split()) # A -> B

    visited = [0]*10000
    visited[A] = 1

    queue = deque()
    queue.append([A,''])
    while queue:
        cur, string = queue.popleft()

        if cur == B:
            print(string)
            break

        if visited[D(cur)] == 0:
            visited[D(cur)] = 1
            queue.append([D(cur), string+'D'])

        if visited[S(cur)] == 0:
            visited[S(cur)] = 1
            queue.append([S(cur), string+'S'])

        if visited[L(cur)] == 0:
            visited[L(cur)] = 1
            queue.append([L(cur), string + 'L'])

        if visited[R(cur)] == 0:
            visited[R(cur)] = 1
            queue.append([R(cur), string + 'R'])