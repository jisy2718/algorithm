def strlen(s): # \0을 만나면 \0을 제외한 글자수를 리턴하는 함수를 while을 이용해 구현
    i = 0
    while s[i]!='\0':
        i += 1
    return i

a = ['a','b','c','\0']
print(strlen(a))