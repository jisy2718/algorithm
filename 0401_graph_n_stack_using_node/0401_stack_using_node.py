# 구현 사항
# push, pop, is-empty
# 방법 : 노드가 자신의 뒤에 것만 알고 있으면 됨 / top 이 node를 가리키게 만들기

class MyStack:
    def __init__(self):
        self.top = None
        self.head = None

        pass


    def push(self, value):
        # top이 가리키는 node의 다음에 연결

        if self.top == None:
            self.top = Node(value)
            self.head = self.top

        else: # self.top != None:
           self.top.next = Node(value)
           self.top = self.top.next # top이 None 경우와 아닌 경우 둘 다 같은 코드


    # head를 설정해서 top까지 탐색
    def pop(self):

        # 요소가 존재하는 경우
        if not self.is_empty():
            # 요소가 1개인 경우
            if self.top is self.head:
                result = self.top
                self.top = None
                self.head = None
                return result.value
            # 요소가 2개 이상인 경우
            else:
                prev = self.find_top(self.head)
                self.top = prev
                return prev.next.value


        else:
            print("Stack is empty")
            return


    # 사실상 top의 이전 노드를 찾아 반환하는 것
    def find_top(self,node): # 요소가 2개 이상인 경우에만 호출되게 되어있음.
                             # 만약 요소 1개일 때도 호출해야 한다면, 바꿔줘야 함
        # 내 다음 요소가 마지막 요소라면, 반환
        if node.next is self.top:
            return node

        else:
            return self.find_top(node.next)


    def is_empty(self):
        if self.top is None:
            return True
        else: return False


class Node:
    def __init__(self,value): # value와 next 노드 지정
        self.value = value
        self.next = None # 최초 생성시 next없음




stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

#!-------------------------------------------------------dfs-
N = 7
E = list(map(int,'1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7'.split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(0,len(E),2):
    s = E[i]
    e = E[i+1]
    adj[s][e] = 1
    adj[e][s] = 1


visited = [0]*(N+1)
stack = MyStack()

# version1, version2는 이동 순서 똑같은데, version1 은 중복되지 않게 방문된 곳 print함
# version2는 모든 이동 경로를 print해서 중복되서 나옴
#---------------------------------------------------version 1
stack.push(1)
# visited[1] = 1

while not stack.is_empty():
    top = stack.top.value
    if visited[top] == 0:

        print(top, end=' ')
    visited[top] = 1
    # 경로 발견 즉시 이동
    for i in range(1,N+1):
        if adj[top][i] == 1 and visited[i] == 0 :
            stack.push(i)
            # visited[i] = 1
            break

    else:
        stack.pop()


#-----------------------------------version 2-------------------
stack = MyStack()
stack.push(1)
visited[1] = 1

while not stack.is_empty():
    top = stack.top.value
    # if visited[top] == 0:
    #
    #     print(top, end=' ')
    # visited[top] = 1
    # 경로 발견 즉시 이동
    for i in range(1,N+1):
        if adj[top][i] == 1 and visited[i] == 0 :
            stack.push(i)
            visited[i] = 1
            break

    else:
        stack.pop()