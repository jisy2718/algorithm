import sys
input = sys.stdin.readline
N, M = map(int,input().split())

int_to_string = {}
string_to_int = {}

for i in range(1,N+1):
    string = input().strip()
    int_to_string[str(i)] = string
    string_to_int[string] = str(i)

for _ in range(M):
    problem = input().strip()
    if string_to_int.get(problem):
        print(string_to_int[problem])
    else:
        print(int_to_string[problem])