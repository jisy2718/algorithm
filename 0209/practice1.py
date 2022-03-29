# 7 4 2 0 0 6 0 7 0
boxes = list(map(int,input().split()))
max_value = 0
# 입력이 제대로 되어 있는지 확인
print(boxes)

# 해야할 일 : 낙차가 가장 큰 상자의 낙차 구하기
# 모든 열에 대해서 가장 꼭대기에 있는 상자의 낙차 구하기
# 낙차 구하기 : 나보다 오른쪽 (인덱스가 뒤쪽) 인 요소의 값이 작으면 낙차 + 1

for i in range(len(boxes)):
    # box[i] : 현재 열의 박스 높이
    count = 0
    for j in range(i+1,len(boxes)):
        if boxes[i] > boxes[j]:
            count += 1
    if max_value < count:
        max_value = count


print(max_value)