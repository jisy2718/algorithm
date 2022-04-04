| 문제번호                             | 내용                                                         | 참고사항                                                     |      |
| ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 1859 백만 장자 프로젝트              | 맥스 값을 찾고, 그 앞에 값들을 맥스에서 다 빼줘야 하는 문제.<br /> | 뒷 방향부터 오기 시작하면, O(n)으로 가능<br /> 앞에서부터 가면 O(n^2) |      |
| 2001 파리퇴치                        | 2차원 배열 내부에서, 2x2 만큼 값 더해서 최대값 찾기          | 2차원 배열의 가장 기본! 꼭 알기                              |      |
| 5356 의석이의 세로로 말해요          | 서로 다른 길이의 행들을 가지는 2차원 배열 arr이 주어졌을 때, 세로로 순서대로 indexing 하는 내용 | try-except 는 지원 안되는 언어도 많음<br />이중 for 문 내부에 if 문으로 처리가능 (열 -> 행 순 for 문으로 가능) |      |
| 1979 어디에 단어가 들어갈 수 있을까? | NxN 행렬의 행, 열에 정확히 K 개 1이 있는 것 개수 찾기        | 보통 1을 K 개 다찾고, 다음으로 넘어가서 점검을 해주는 것을 권장함 => 더미 행,열을 마지막에 1개추가하면 용이 |      |
| 1974 스도쿠검증                      | 9x9 스도쿠 퍼즐이 올바른지 파악                              | 숫자세기 배열을 count sort 할 때처럼 count 배열을 이용하면 편함 |      |

+ 알고리즘은 탑 다운으로 짜야 함 (main 완전 후, 내부 함수들은 나중에 짜기)
+ 2차원 배열에서 경계지역 조건 판단할 때, 더미로 행, 열 추가해서 하면 편하다
+ 연속된 숫자들이 몇 번 나왔는지 셀 때는 count 배열 이용하면 편함
  +  1974, **4408**, 6485 번

+ 반복문 내부에서 case 1개만 찾으면 작업 끝내는 경우, 함수로 짜서 함수의 return 이용하면 편하다.
+ 연속된 홀수, 짝수 정수를 같은 수로 만들기 `int( (n+1)/2 -1 )`  : 7 ->3 / 8->3







# stack1

| 문제번호                | 내용                                                         | 참고사항                                |      |
| ----------------------- | ------------------------------------------------------------ | --------------------------------------- | ---- |
| **4873** 반복문자지우기 |                                                              | stack 을 이용하면 한번만 loop를 돌면 됨 |      |
| **4869** 종이붙이기     | 2가지 종류의 종이가 주어질 때, 주어진 길이만큼 만들 수 있는 경우의 수 | 피보나치 스럽게 하면 됨                 |      |
|                         |                                                              |                                         |      |



# stack2

| 문제번호               | 내용                                                         | 참고사항            |      |
| ---------------------- | ------------------------------------------------------------ | ------------------- | ---- |
| 4874 Forth             | 후위 표기로 바꾸기                                           |                     |      |
| 4875 미로              | 미로 탈출구 찾기                                             |                     |      |
| 4880 토너먼트 카드게임 | 분할 정복 + 가위바위보 비기면 우선순위 존재                  | 영택님꺼참고        |      |
| 4881 배열최소합        | NxN 배열에서 한 행에서 1개씩 열이 겹치지 않게 뽑았을 때 최소합?<br /> | n-queen / 순열 이용 |      |
| 1224 계산기 3          |                                                              |                     |      |



# Problem Solving 3(220325)

+ 아래는 모두 BFS 이용
+ BFS에서 Queue에 넣을 때는, 바로 다음 행동만 생각해서 Queue에 넣으면 됨.
  + 주의할 점은 바로 다음 행동에 모든 경우의 수를 다 생각해야 함.

| 문제번호                                                     | 내용                                                         | 참고사항                                                     |      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| **[1952 수영장](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq&categoryType=CODE&problemTitle=1952&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)** | BFS로 4가지 화폐조합의 최저비용 계산하기                     |                                                              |      |
| **[2105 디저트 카페](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE&problemTitle=2105&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)** | BFS로 마름모 순환 + 각 자리별 숫자 있는데, <br />중복되는 숫자 없는 마름모만 순환하기 |                                                              |      |
| **[2819 격자판의 숫자 이어 붙이기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=2819&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)** | 4X4 숫자데이터(0~9, 중복숫자있음)에서, <br />상하좌우 중복방문 가능하게 움직일 때,<br /> 임의의 위치에서 시작해서, <br />7자리 수를 방문할 때,<br /> 중복되지 않는 방문 경로들의 개수는? | 좀 더 시간 줄여서 하는 방법 생각해보기                       |      |
| ***[2117_홈방법서비스](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV5V61LqAf8DFAWu&probBoxId=AX-rcCTK0_MDFARi&type=PROBLEM&problemBoxTitle=220325_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=8)*** |                                                              | 방문을 좀 더 효율적으로 코드 짜는 방법 생각해보기 **꼭다시** |      |
| ***[2382_미생물 격리](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV597vbqAH0DFAVl&probBoxId=AX-rcCTK0_MDFARi&type=PROBLEM&problemBoxTitle=220325_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=8)*** |                                                              |                                                              |      |
| **[4366_정식이의 은행업무](https://swexpertacademy.com/main/talk/solvingClub/problemSubmitDetail.do)** | 똑같은 숫자를, 3진수, 2진수 표현에서 각각 1자리씩만 잘못 적었을 때, 원래 숫자 맞추기 | 좀 더 간단하게 푸는 방법 생각해보기                          |      |
| [4615_오셀로게임](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AWQmA4uK8ygDFAXj&probBoxId=AX-rcCTK0_MDFARi&type=PROBLEM&problemBoxTitle=220325_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=8) | 오셀로 게임 결과 흑, 백 돌 개수 맞추기                       | 이 테이블 문제들 중 후순위로 다시 풀기                       |      |
| [10726_이진수표현](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXRSXf_a9qsDFAXS&probBoxId=AX-rcCTK0_MDFARi&type=PROBLEM&problemBoxTitle=220325_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=8) |                                                              | 이 테이블 문제들 중 최후순위로 다시 풀기                     |      |







# 완전탐색

| 문제번호                                                     | 내용                                                         | 참고사항                                                     |      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| **[5188](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXxOQHk6RM4DFASZ&probBoxId=AX_TwYkqORYDFARi+&type=USER&problemBoxTitle=220329_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)** 최소합 | NxN 배열의 (0,0) 에서 (N-1,N-1)까지  arr[r]\[c] 합을 최소로하도록 이동 |                                                              |      |
| **[5189](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXxOQwSKRPkDFASZ&solveclubId=AX7cgLH6Z7QDFAS2&problemBoxTitle=220329_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5&probBoxId=AX_TwYkqORYDFARi+)** 전자카트 | 순열 만들기                                                  | 순열 만드는 것 다시 보기<br />백트래킹 쓸 수 있도록, 이동 순간마다 이동 비용 계산하는 것이 훨씬 좋음 |      |
|                                                              |                                                              |                                                              |      |



# 그리디

| 문제번호                                                     | 내용                                                         | 참고사항                                    |      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------- | ---- |
| [5201](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXxORDsaRRMDFASZ&probBoxId=AX_TwYkqORYDFARi+&type=USER&problemBoxTitle=220329_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5) 컨테이너 운반 | 트럭들의 적재용량과, 물건들의 무게가 주어짐. 트럭이 1개만 적재할 수 있고, 1번만 이동 가능할 때, 최대한 많은 무게 운반한 경우의 무게 구하기 | 정렬 함수 안쓰고 할 수 있는 방법 생각해보기 |      |
| **[5202](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXxOSi3aRZ8DFASZ&solveclubId=AX7cgLH6Z7QDFAS2&problemBoxTitle=220329_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5&probBoxId=AX_TwYkqORYDFARi)** 화물 도크 | 시작과 끝 시간이 정해져있는 작업들이 input()으로 들어올 때, 하루 동안 가장 많은 작업을 처리한 횟수는? | 정렬함수 안 쓰고 했음                       |      |
| [5203](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXxOS4QKRbcDFASZ&probBoxId=AX_TwYkqORYDFARi&type=USER&problemBoxTitle=220329_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)  베이비진 게임 | 2명이서 베이비진 게임 플레이해서, 이긴 플레이어 찾기<br /> 연속된 3장이 있거나, 똑같은 3장 있으면 이기는 것 |                                             |      |





# 분할정복(03/31)

| 문제번호                                                     | 내용                                                         | 참고사항                             |      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ | ---- |
| **[5205](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXxY9RJqZasDFASZ&probBoxId=AX_eEqMax0wDFARi+&type=USER&problemBoxTitle=220331_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)** 퀵정렬 | 퀵정렬                                                       | 다시 해보기                          |      |
| **[5207](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXxY9pjaZeUDFASZ&probBoxId=AX_eEqMax0wDFARi+&type=USER&problemBoxTitle=220331_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)** 이진탐색 |                                                              | 다시 해보기                          |      |
| **[5208](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXxY99SaZhoDFASZ&probBoxId=AX_eEqMax0wDFARi+&type=USER&problemBoxTitle=220331_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)** 전기버스2 | 충전소를 최소한으로 지나면서, 목적지에 도착하기              | 백트래킹 잘해주기                    |      |
| [5209](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXxY-RpqZkoDFASZ&probBoxId=AX_eEqMax0wDFARi+&type=USER&problemBoxTitle=220331_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5) 최소생산비용 | 2차원 배열의 한 행에 한 개씩 선택해서, 합 최소되도록 하는 것 | 백트래킹 잘하면 됨                   |      |
| [1865](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV5LuHfqDz8DFAXc&probBoxId=AX_eEqMax0wDFARi+&type=PROBLEM&problemBoxTitle=220331_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5) 최대확률값 | 2차원 배열의 한 행에 한 개씩 선택해서, 곱이 최대가 되도록 하는 것 | 백트래킹 잘하면 됨. 5209와 같은 문제 |      |





# Problem Solving 4(220404)

| 문제번호                                                     | 내용                                     | 참고사항                                                     |      |
| ------------------------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------ | ---- |
| **[1249 ](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV15QRX6APsCFAYD&probBoxId=AX_ULMNaTCYDFARi&type=PROBLEM&problemBoxTitle=220404_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)보급로** | 중복방문 BFS<br />다익스트라로 풀어도 됨 | 중복 방문이 가능할 조건을 이전 결과보다 더 나은 결과일 때로<br />2차원 visited 배열에, 현재까지 비용을 입력 |      |
| **[5251](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AXx9IM3aaF0DFARs&probBoxId=AX_ULMNaTCYDFARi&type=USER&problemBoxTitle=220404_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5) 최소이동거리** | 다익스트라                               | 좀 더 깔끔하게 해보기                                        |      |
| [2806](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV7GKs06AU0DFAXB&probBoxId=AX_ULMNaTCYDFARi&type=PROBLEM&problemBoxTitle=220404_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5) Nqueen |                                          | 대각선의 합 규칙 알기 / used이용해서 순열만드는 것과 같은 테크닉 이용 |      |
| **[2115](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV5V4A46AdIDFAWu&probBoxId=AX_ULMNaTCYDFARi&type=PROBLEM&problemBoxTitle=220404_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)**벌꿀 채취 |                                          | **주의** : 연속된 M개의 벌꿀 통들 중에서, 조건에 맞게 몇 개의 벌꿀 통들을 선택하면 되는 문제 / dfs |      |
| **[5648](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AWXRFInKex8DFAUo&probBoxId=AX_ULMNaTCYDFARi&type=PROBLEM&problemBoxTitle=220404_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=5)** 원자소멸 시뮬레이션 |                                          | x,y 좌표축에서 움직이는 것과, 행렬좌표에서 움직이는 것의 차이 꼭!!! 알기<br />x,y좌표계는 위로가면 + 이지만, 행렬은 - |      |







# 일반사항

+ **대각선 표시** 
  
  + 정사각 배열에서 대각선은 2N-1개 존재
  
  + 한쪽 대각선 (////방향) 의 인덱스 합은 0,1,2,3,...,2N-2
  
  + 다른 한쪽의 경우 (\\\\\\\\ 방향) 의 경우 인덱스의 차는 -(N-1) , - (N-2) , ... , 0 , ... , (N-2), (N-1)
    + i - j + (N-1) 하면 0, 1, 2, ... , 2N-1
    
      
  
+ 진수표현

  + list에 숫자로 넣어서 하면 편함



+ 최소값 찾을 때, 찾는 도중에 찾은 값이 최소보다 크면, **백트래킹** 활용!
+ 소수점 아래자리 표현
  + `print(f'{number: .8f}')`  : number의 소수점 8자리까지 표현
+ for loop 뒤에서부터 순회하면, 삭제해도 index에 영향을 안미침
