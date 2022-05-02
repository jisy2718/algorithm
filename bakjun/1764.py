N, M = map(int,input().split())

first = set()
second = set()
for _ in range(N):
    name = input()
    first.add(name)

for _ in range(M):
    name = input()
    second.add(name)

cap = first.intersection(second)
cap = list(cap)
cap.sort()
print(len(cap))
for name in cap:
    print(name)
