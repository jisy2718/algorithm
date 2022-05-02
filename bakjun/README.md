[toc]



# 01 회차 - sorting

| 번호      | 설명                                                | 해결방법                                                     | 제출번호                                                     | 참고                                                   |
| --------- | --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| 11650     | (x,y) 좌표 x, y 순 정렬                             | bubble sort <br />selection sort<br />merge sort<br />내장 sort()<br />bubble sort + sys.stdin<br />selection sort + sys.stdin<br />merge sort + sys.stdin | 38976089 [?% 시간초과]<br />38977056 [9% 시간초과]<br />38980215 [18 % 시간초과]<br />38980529 [통과]<br />38980747 [시간초과]<br />38980814 [시간초과]<br />[38980690](https://www.acmicpc.net/submit/11650/38980690) [통과] |                                                        |
| 11651     | (x,y) 좌표 y, x 순 정렬                             | merge sort + sys.stdin                                       | [38981530](https://www.acmicpc.net/submit/11651/38981530) [통과] |                                                        |
| 1181      | str length 짧은 순, 사전 순 정렬<br />              | selection sort + sys.stdin<br /> **length merge sort + 사전 순은 내장 sort**<br /> **length & 사전 순 merge sort 이용**해 구현 | 38982139 [?% 시간초과]<br />[39061635](https://www.acmicpc.net/submit/1181/39061635) [통과]<br />[39125583](https://www.acmicpc.net/submit/1181/39125583) [통과] | [lambda 이용](https://www.acmicpc.net/source/25348011) |
| 10814(me) | 나이+이름 주어질 때, 나이순 정렬                    | insertion sort<br />insertion sort  + sys.stdin<br />selection sort  + sys.din<br /> merge sort | 39046292 [시간초과]<br />39046886 [시간초과]<br />39049874 [시간초과]<br />[39065910](https://www.acmicpc.net/submit/10814/39065910)[통과] |                                                        |
| 18870     | 좌표 압축 : 자신보다 작은 숫자의 개수를 차례로 출력 | 완전탐색 + sys.din<br /> 완전탐색 + dict 활용 + sys.din<br /> merge_sort + dict + sys.din<br /> 내장 sort + dict<br /> merge_sort + sys.din + pypy<br /> 내장 sort + set + dict (권장)<br /> **merge_sort + set + dict (권장)** | 39051114 [시간초과]<br />39051647 [시간초과]<br />39057153[시간초과]<br />39057076 [통과]<br />39058464 [통과]<br />39059736 [통과]<br />[39059855](https://www.acmicpc.net/submit/18870/39059855)[통과] |                                                        |

```python
11651 : sorted_arr = arr.sort(key=lambda x:(x[1],x[0]))
```







# 02 회차 - 문자열

| 번호                                             | 설명                                           | 해결방법                                                     | 제출번호                                                     | 참고 |
| ------------------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| [11654번](https://www.acmicpc.net/problem/11654) | 아스키코드 출력                                |                                                              | [37673128](https://www.acmicpc.net/submit/11654/37673128) [통과] |      |
| [11720번](https://www.acmicpc.net/problem/11720) | 숫자 합치기                                    |                                                              | [37686128](https://www.acmicpc.net/submit/11720/37686128)[통과] |      |
| [10809번](https://www.acmicpc.net/problem/10809) | 알파벳이 처음 포함된 위치 출력                 |                                                              | [39215201](https://www.acmicpc.net/submit/10809/39215201)[통과] |      |
| [2675번](https://www.acmicpc.net/problem/2675)   | 입력받은 문자를 <br />특정 횟수 반복해서 출력  | \\ 가 있는 경우와 없는 경우 나눠서 처리                      | [39215519](https://www.acmicpc.net/submit/2675/39215519) [통과] |      |
| [1157번](https://www.acmicpc.net/problem/1157)   | 대소문자 알파벳 구분없이 많이 나온 알파벳 찾기 |                                                              | [39216643](https://www.acmicpc.net/submit/1157/39216643) [통과] |      |
| [1152번](https://www.acmicpc.net/problem/1152)   | 공백으로 구분되는 영어 문장의 단어 개수 세기   |                                                              | [39378247](https://www.acmicpc.net/submit/1152/39378247)     |      |
| [2908번](https://www.acmicpc.net/problem/2908)   | 숫자 거꾸로 읽고 대소비교                      | 숫자 거꾸로 만드는 함수 생성                                 | [39431770](https://www.acmicpc.net/submit/2908/39431770)     |      |
| [5622번](https://www.acmicpc.net/problem/5622)   | 다이얼 누르기                                  |                                                              | [39436388](https://www.acmicpc.net/submit/5622/39436388)     |      |
| [2941번](https://www.acmicpc.net/problem/2941)   | 문자열에서 크로아티아 문자의 개수 세기         | dictionary 이용<br />좀 더 쉽게 할 수 있는지 생각해보기      | [39382871](https://www.acmicpc.net/submit/2941/39382871)     |      |
| [1316번](https://www.acmicpc.net/problem/1316)   | 그룹 단어 체커                                 | set과 for-else 이용<br /> string의 앞 글자와 뒷 글자가 다르다면 set에 앞 글자 추가 (마지막글자는 따로 확인하면 됨) | [39431577](https://www.acmicpc.net/submit/1316/39431577)     |      |

```python
a = '문자열' or 순회가능열
mid = len(a) // 2  : len(a)가 짝수면, i < mid 로 하면 딱 절반 indexing // len(a) 가 홀수면, i < mid로 하면 맨 중앙 꺼 빼고 그 전까지 indexing
```







# 03 회차 - *브루트 포스* 다시 풀기

| 번호                                           | 설명   | 해결방법             | 제출번호                                                     |
| ---------------------------------------------- | ------ | -------------------- | ------------------------------------------------------------ |
| [2798번](https://www.acmicpc.net/problem/2798) | 블랙잭 | bit 로 부분집합 생성 | [39507291](https://www.acmicpc.net/submit/2798/39507291) 시간초과 |
|                                                |        |                      |                                                              |
|                                                |        |                      |                                                              |







# 04 회차 - *Stack* 마저 풀기

| 번호                                             | 설명                                  | 해결방법                      | 제출번호                                                  |
| ------------------------------------------------ | ------------------------------------- | ----------------------------- | --------------------------------------------------------- |
| [10828번](https://www.acmicpc.net/problem/10828) | stack 구현(top,push, pop, empty,size) | stack class 생성              | [39718701](https://www.acmicpc.net/submit/10828/39718701) |
| [10773번](https://www.acmicpc.net/problem/10773) | stack 이용해서 숫자합 세기            |                               | [39721292](https://www.acmicpc.net/submit/10773/39721292) |
| [9012번](https://www.acmicpc.net/problem/9012)   | () 괄호짝맞추기                       | stack 생성( 오류 case 2 가지) | [39723612](https://www.acmicpc.net/submit/9012/39723612)  |
| 4949번                                           |                                       |                               |                                                           |
| 1874번                                           |                                       |                               |                                                           |
| 17298번                                          |                                       |                               |                                                           |





#  05 회차 - 큐 & 덱

| 번호                                             | 설명                                                         | 해결방법                                                     | 제출번호                                                  |
| ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------- |
| [18258번](https://www.acmicpc.net/problem/18258) | 큐 구현(push, pop, front, back, size, empty)                 | collections.deque & sys.stdin.readline()이용                 | [40317941](https://www.acmicpc.net/submit/18258/40317941) |
| [2164번](https://www.acmicpc.net/problem/2164)   | 맨 위 카드 1장 버리고, 다음 맨 위 카드 맨 밑으로 넣는 것 반복 시, 마지막에 남는 카드 | collections.deque 이용                                       | [40298328](https://www.acmicpc.net/submit/2164/40298328)  |
| [11866번](https://www.acmicpc.net/problem/11866) | (N,K)-요세푸스 순열                                          | collections.deque에 모든 수 넣고, 맨 앞에거 빼서 맨 뒤로 집어넣는 거 반복하는 도중, 매 K 번째 것을 출력 | [40317091](https://www.acmicpc.net/submit/11866/40317091) |
| [1966번](https://www.acmicpc.net/problem/1966)   | 프린터 큐 (중요도 순서에 따라 문서 인쇄)                     | deque 이용 / 문서 중요도를 dict로 만들어 활용                | [40298915](https://www.acmicpc.net/submit/1966/40298915)  |
|                                                  |                                                              |                                                              |                                                           |

4, 8



# 08 회차 - 우선순위 큐

| 번호                                                         | 설명                         | 해결방법 | 제출번호                                                  |
| ------------------------------------------------------------ | ---------------------------- | -------- | --------------------------------------------------------- |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" alt="img" style="width:20px;" /> **[11279번](https://www.acmicpc.net/problem/11279)** | 최대힙의 insert, delete 구현 | 구현     | [41228627](https://www.acmicpc.net/submit/11279/41228627) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" alt="img" style="width:20px;" /> [1927번](https://www.acmicpc.net/problem/1927) | 최소힙의 insert, delete 구현 | 구현     | [41228910](https://www.acmicpc.net/submit/1927/41228910)  |
|                                                              |                              |          |                                                           |



# 06 회차 - BFS&DFS

+ 최단 경로 / 최저비용에는 BFS 구현

+ DFS pop 위에서 하는 것도 해보기

  

| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [1260번](https://www.acmicpc.net/problem/1260)               | BFS, DFS 구현                                                | deque, stack 이용                                            | [40345136](https://www.acmicpc.net/submit/1260/40345136)     |
| [2606번](https://www.acmicpc.net/problem/2606)               | 연결된 덩어리의 정점 개수 세기                               | stack 이용한 DFS                                             | [40345632](https://www.acmicpc.net/submit/2606/40345632)     |
| [2667번](https://www.acmicpc.net/problem/2667)               | 연결된 덩어리 개수와, 각 덩어리 크기 세기                    | for loop 2회 로 연결 덩어리 찾고, DFS로 각 덩어리 탐색(visit)하며, 덩어리 크기 파악 | [40507516](https://www.acmicpc.net/submit/2667/40507516)     |
| [1012번](https://www.acmicpc.net/problem/1012)               | 연결된 덩어리 개수 세기 / 가로 세로 순으로 input 받음        | for loop 2회로 연결덩어리 찾고, DFS로 각 덩어리 탐색(visit)  | [40510088](https://www.acmicpc.net/submit/1012/40510088)     |
| [2178번](https://www.acmicpc.net/problem/2178)               | 미로의 최단경로                                              | BFS로 구현 visited를 q에 append 할 때 해주기                 | [40908957](https://www.acmicpc.net/submit/2178/40908957)     |
| ***[7576번](https://www.acmicpc.net/problem/7576)***         | 2차원 배열에서 상하좌우로 전염되는 문제로, 언제 전염이 끝날지 | 복사 arr 만들어서,  arr 순회하며 복사 arr에 결과 반영 후, 다시 복사본을 arr에 deepcopy<br /><br />주현님 풀이를 참고하여, q에 새로운 전염된 지점들을 넣어주면서 진행 | [40534259](https://www.acmicpc.net/submit/7576/40534259)시간초과<br /><br />[40550240](https://www.acmicpc.net/submit/7576/40550240) |
| ***[7569번](https://www.acmicpc.net/problem/7569)***         | 2차원 배열에서 상하좌우,수직위아래 6방향으로 전염되는 문제로, 언제 전염이 끝날지 | queue 이용해서, 풀면 됨<br />BFS이므로 날짜를 다로 세어주지 않아도 됨 | [40817078](https://www.acmicpc.net/submit/7569/40817078)<br />[40909218](https://www.acmicpc.net/submit/7569/40909218)<br />날짜 따로 안세어주는 버전 |
| ***[1697번](https://www.acmicpc.net/problem/1697)***         | 1차원 공간에서 목적지를 갈 때, +1, -1, *2 로 움직일 수 있을 때, 최단 시간 구하기 | BFS & visited : visited 이용해야 빨리할 수 있음 /  index 에러나는 것 대비해서, 범위도 조건으로 넣어주기 | [[40820377](https://www.acmicpc.net/submit/1697/40820377)]   |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px" />***[2206번](https://www.acmicpc.net/problem/2206)*** | 벽부수고 최단거리 이동                                       | BFS 이용.<br />**3차원visited**이용해야/ q는 한 번에 다 같은 거리의 경로에 대해 탐색하므로, q에 벽부순 것을 넣어도 된다고 생각하지만, 이는 다음과 같은 문제를 발생시킴<br /><br /> 1. 다음과 같은 (0,0)에서 출발해서, (3,2)로 최단경로로 가는 것을 생각해보자. 0은 통로, 1은 벽, 벽은 1번 부술수 있다고 하자. <br />010<br />000<br />111<br />100<br />2. 이동경로는 오른쪽부터 시계방향으로 탐색한다고 해보자. 그렇다면, 이미 벽을 부순 (0,1)을 지난 경로가  (1,1)에 가장 먼저 도달하게 되어, visted 처리를 하게되고,  (1,0)에서 (1,1)로는 이동하지 못하게 된다.<br />3. 위에서 최단경로는 (0,0) -> (1,0) ->(1,1) 을 꼭 지나야 하므로 최단 경로를 못찾게 된다.<br /><br />**요약**하자면, 벽을 k번 부술수 있다면, NxMx(k+1) visited 배열을 생성해서, 각 k에 대해, 벽을 0 번, 1번, 2번, ..., k번  부순 것들의 최단 경로가 visited에서 방문처리가 되도록 해야 함 <br />**주의** visted 배열 만들 때, 이중 for문으로 해야함 | [40886487](https://www.acmicpc.net/submit/2206/40886487) 틀림<br />[41750424](https://www.acmicpc.net/submit/2206/41750424) 3차원 visited |
| [7562번](https://www.acmicpc.net/problem/7562)               | 나이트를 목표지점에 움직이는 최단거리                        | BFS 이용                                                     | [40823688](https://www.acmicpc.net/submit/7562/40823688)     |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px;" />***[1707번](https://www.acmicpc.net/problem/1707)*** | 이분 그래프 판별                                             | DFS + Dictionary 이용<br />노드이동 풀이                     | [40885796 ](https://www.acmicpc.net/submit/1707/40885796)시간초과<br />[40880220](https://www.acmicpc.net/submit/1707/40880220) 메모리초과 |

+ 7576번 : 주현님 풀이 보기





# 07 회차 - 트리

| 번호                                                         | 설명                                        | 해결방법                                                     | 제출번호                                                     |
| ------------------------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **[11725번](https://www.acmicpc.net/problem/11725)**         | 트리의 부모노드 찾기                        | index를 자식, value를 부모로하는 tree 생성                   | [40883123](https://www.acmicpc.net/submit/11725/40883123) 시간초과 |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" alt="img" style="width:20px;" />[1991번 ](https://www.acmicpc.net/problem/1991) | 트리의 pre,in,post order 순회               |                                                              | [40884311](https://www.acmicpc.net/submit/1991/4088431       |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/13.svg" alt="img" style="width:20px;" /> **[1167번](https://www.acmicpc.net/problem/1167)** | 트리지름구하기                              | dfs 재귀구현                                                 | [40954377](https://www.acmicpc.net/submit/1167/40954377) 메모리초과 |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px;" />**[1967번](https://www.acmicpc.net/problem/1967)** | 트리 지름 구하기                            | dfs 재귀구현<br />후위탐색 재귀구현<br />후위탐색 재귀구현<br />sys.setrecursionlimit(10**9) | [41039735](https://www.acmicpc.net/submit/1967/41039735) 시간초과<br />[41041676](https://www.acmicpc.net/submit/1967/41041676) 재귀초과<br />[41042182](https://www.acmicpc.net/submit/1967/41042182) 재귀초과(위의 것 post인자 1개로 한 것)<br />[41043495](https://www.acmicpc.net/submit/1967/41043495) value error |
| ***<img src="https://d2gd6pc034wcta.cloudfront.net/tier/14.svg" alt="img" style="width:20px;" />[2263번](https://www.acmicpc.net/problem/2263)*** | 이진트리 중,후위순회로 전위순회 찾기        | sys.setrecursionlimit(10**9)<br />in_order에서 특정 값의 index 가져오기 위해, list 하나 만들고 시작하기(left,right만들어서 함)<br />left, right  안만들고, 바로 index로 계산(41101739) | [41045481][https://www.acmicpc.net/submit/2263/41045481] 시간초과<br />[41101636](https://www.acmicpc.net/submit/2263/41101636)<br />[41101739](https://www.acmicpc.net/submit/2263/41101739)<br />[41233770](https://www.acmicpc.net/submit/2263/41233770) : 이거보기 |
| *** <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" alt="img" style="width:20px;" />[5639번](https://www.acmicpc.net/problem/5639)*** | 이진검색트리에서 전위순회를 후위순회로 변환 | 이진검색트리는 좌측노드의 값이 우측노드의 값보다 작으므로,  전위순회의 첫 원소가 root, root 보다 작은 첫 값이 왼쪽 노드, root보다 큰 첫 값이 오른쪽 노드 | [41122756](https://www.acmicpc.net/submit/5639/41122756)     |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px;" /> **[4803번](https://www.acmicpc.net/problem/4803)** | 그래프에서 트리 개수 찾기                   | visited를 잘 하는 것이 핵심(dfs 풀이시)<br />**서로소 집합**으로 해결! | [42363368](https://www.acmicpc.net/submit/4803/42363368)     |



# 09 회차 - 백트래킹

| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [<img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" /> 15649번](https://www.acmicpc.net/problem/15649) | nPm                                                          | idx만 인자로 받는 재귀함수, 결과 : p=[0]\*M, used=[0]*N      | [41580199](https://www.acmicpc.net/submit/15649/41580199)    |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" alt="img" style="width:20px;" /> [9663번](https://www.acmicpc.net/problem/9663) N-Queen | 퀸들의 이동 경로가 서로 겹치지 않게, 놓을 수 있는 경우의 수 구하기 | 대각선의 합과 차가 일정하다는 것을 이용<br />**전형적인 dfs(트리)문제**로 풀이 | [41746933](https://www.acmicpc.net/submit/9663/41746933)<br />[41747223](https://www.acmicpc.net/submit/9663/41747223) 시간초과 |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" alt="img" style="width:20px;" />**[14888번](https://www.acmicpc.net/problem/14888)** 연산자끼워넣기 | 숫자와 연산자 4가지가 주어지면, 값이 최대/최소가 되도록 숫자와 연산자를 배치하기 | 4가지 경우 DFS의 if 문으로 진행(빠른편인듯)                  | [41735161](https://www.acmicpc.net/submit/14888/41735161)    |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" alt="img" style="width:20px;" /> **[14889번](https://www.acmicpc.net/problem/14889)**  스타트와 링크 | 전체를 절반으로 두팀으로 나눠서, 두 팀의 시너지의 차이가 가장 적게하는 방법 | **전형적인 dfs (tree)문제**로 **외우기**<br />종료조건, (재귀)포함시키는경우, (재귀)포함안시키는경우 | [41745415](https://www.acmicpc.net/submit/14889/41745415)    |





# 10 회차 - 그리디

| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[11047번](https://www.acmicpc.net/problem/11047)  거스름돈 | 문제 조건이 그리디 가능함(다음 단위 돈이 이전 돈의 배수)     | 그리디<br />dfs(완전탐색)                                    | [41923375](https://www.acmicpc.net/submit/11047/41923375)<br />[41933621](https://www.acmicpc.net/submit/11047/41933621) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" alt="img" style="width:20px;" />**[1931번](https://www.acmicpc.net/problem/1931)  회의실배정** |                                                              | 안되는 것들 전체 일정에서 삭제하는 것보다, index 접근이 빠름<br />좀 더 깔끔한 loop로 해보기(주현님참고) | [41929360](https://www.acmicpc.net/submit/1931/41929360)     |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[11399번 ](https://www.acmicpc.net/problem/11399) ATM |                                                              |                                                              | [41930168](https://www.acmicpc.net/submit/11399/41930168)    |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" alt="img" style="width:20px;" />[1541번](https://www.acmicpc.net/problem/1541) 잃어버린 괄호 | 양수, +, - 연산이 str 한 문장으로 주어질 때, 괄호를 쳐서 가장 작게 값 나오도록 하기 (55-50+40 와 같음) | 앞에서부터 보면서, - 가 한번이라도 나오면, 그 뒤는 모두 음수로 만들 수 있음 | [41930999](https://www.acmicpc.net/submit/1541/41930999)     |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" alt="img" style="width:20px;" />**[13305번 ](https://www.acmicpc.net/problem/13305)주유소** | 직선도로에서, 각 위치에서의 기름값과 위치간의 거리가 주어질 때, 최소 비용으로 목적지까지 이용하기 | 현재위치보다 기름값이 싼 곳이 나올 때까지 움직이면 됨 / index 처리가 조금 헷갈림<br />좀 더 깔끔한 loop로 해보기 (주현님참고) | [41931913](https://www.acmicpc.net/submit/13305/41931913)    |





# 11회차 - 아기상어 + 최소신장트리

| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" alt="img" style="width:20px;" />[17086번](https://www.acmicpc.net/problem/17086) 아기상어 | 0,1로 이루어진 2차원 배열주어지면, 1인 곳에서 8방으로 뻗어나갈 때, 언제 0을 다 전염시키는지와 같은 문제 | ***[7576번](https://www.acmicpc.net/problem/7576)*** 문제참고 | [42068859](https://www.acmicpc.net/submit/17086/42068859)    |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[9372번](https://www.acmicpc.net/problem/9372) 상근이의 여행 | 가중치 없는 연결 그래프에서, 최소신장트리의 길이는, node 개수 -1 |                                                              | [42069304](https://www.acmicpc.net/submit/9372/42069304)     |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px;" />**[1197번](https://www.acmicpc.net/problem/1197)** | 최소신장트리찾기                                             | prim은 시간초과되고, kruscal은 ok                            | [42139683](https://www.acmicpc.net/submit/1197/42139683) prim(arr) 시간초과<br />[42139960](https://www.acmicpc.net/submit/1197/42139960) prim(arrL) 시간초과<br />[42140779](https://www.acmicpc.net/submit/1197/42140779) Kruscal |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px;" />**[4386번](https://www.acmicpc.net/problem/4386)** | 2차원 좌표주어질 때, 최소신장트리찾기                        | prim으로 해결                                                | [42141573](https://www.acmicpc.net/submit/4386/42141573)     |





# 12 회차 - 아기상어 & class3+



| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------- |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/13.svg" alt="img" style="width:20px;" />**[16236번 ](https://www.acmicpc.net/problem/16236)아기상어** | 자신 크기 이하의 물고기 통과 가능, 자신 크기 미만 물고기 먹기 가능, 자신의 크기 만큼 물고기 먹으면, 자신의 크기 +1일 때,<br />물고기를 최대한 먹을 때까지 걸리는 시간 | bfs 만들어서, 먹을 수 있는 후보군 만들어서, 이를 규칙에 맞게 정렬해서, 먹고, 다시 물고기 탐색 반복 | [42360091](https://www.acmicpc.net/submit/16236/42360091) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[1463번](https://www.acmicpc.net/problem/1463) 1로 만들기 | 자연수를 //3  or //2 or -1 해서 1로 만드는 최소 횟수<br />주현님 풀이 **BFS & DP** 로 해보기 | dfs & 백트래킹                                               | [42184824](https://www.acmicpc.net/submit/1463/42184824)  |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[1003번](https://www.acmicpc.net/problem/1003)  피보나치수 | 재귀호출시 fibo(0), fibo(1) 몇번 호출되는지                  | 재귀구현은 시간초과<br />DP구현은 통과                       | [42269962](https://www.acmicpc.net/submit/1003/42269962)  |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="WIDTH:20PX;" />[9095번](https://www.acmicpc.net/problem/9095) 1,2,3 더하기 | 정수 n을 1,2,3 을 이용한 합으로 나타내는 방법의 수           | dfs                                                          | [42270546](https://www.acmicpc.net/submit/9095/42270546)  |



# 13 회차 - class3+

| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------- |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[11726번](https://www.acmicpc.net/problem/11726)   2xn 타일링 | \|, = 모양 타일로 2xn 타일채우기                             | 피보나치 & DP                                                | [42319435](https://www.acmicpc.net/submit/11726/42319435) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />**[2579번](https://www.acmicpc.net/problem/2579)**계단 오르기 | 1 칸 또는 2칸씩 계단 오르는데, 연속한 3칸을 오를 수는 없음. <br />각 계단마다 점수 있는데, 목적지 도착시 최대 점수값구하기 | DP<br />dfs는 시간초과<br />**현아님풀이대로 dp더 간단히 해보기** | [42337724](https://www.acmicpc.net/submit/2579/42337724)  |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[9461번](https://www.acmicpc.net/problem/9461) 파도반 수열 | 나선형으로 삼각형 배열했을 때, 마지막에 놓는 삼각형의 한 변의 길이 찾기 | 규칙찾아서하기.<br />신기한 것은 점화식이 2개임.<br />N = N- 1 + N-5<br /> = N -2 + N -3 | [42338392](https://www.acmicpc.net/submit/9461/42338392)  |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" alt="img" style="width:20px;" />**[10026번](https://www.acmicpc.net/problem/10026)** 적록색약 | R,G,B로 이루어진 2차원배열에서 뭉쳐진 R,G,B 그룹개수 찾기    | **2차원 서로소 집합** 이용<br />**현아님 BFS, 소연님 R을 G로 바꾸기, 주현님 DFS** | [42341639](https://www.acmicpc.net/submit/10026/42341639) |



# 14회차 - class3+

| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------- |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" alt="img" style="width:20px;" />**[1992번 ](https://www.acmicpc.net/problem/1992)**쿼드트리 | 2차원 0,1 배열 압축하기                                      | dfs로 해결<br />**매 순간 압축해주는 방식 : 현아님 풀이** 보기<br />**소연님 dfs 보기** | [42583356](https://www.acmicpc.net/submit/1992/42583356)  |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" alt="img" style="width:20px;" />**[11403번 ](https://www.acmicpc.net/problem/11403)**경로찾기 | 2차원으로 연결관계가 표현되는 유향그래프에서, i에서 j로 갈 수 있는 경우 모두 찾기 | stack을 이용한 dfs 이용 / for-else 방식의 stack으로 dfs 구현하면, **stack에 있는 node들은 모두 순서대로 이어진 경로**이므로, 이를 이용 & **cycle 부분 처리를 따로** 해줘야 함 | [42581327](https://www.acmicpc.net/submit/11403/42581327) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" alt="img" style="width:20px;" />**[14500번](https://www.acmicpc.net/problem/14500)**테르트미노 | 테트리스 4가지 모양 중 1개 이용해서 2차원 배열 덮을 때, 덮인 부분 값의 합이 최대가 되도록 | 생각해보면, 이어진 4개의 블록의 모든 경우의 수와 동일함 그래서 모든 경우의 수 더해서 해결<br />**bfs, dfs로도 해보기** (dfs경우 ㅗ 모양따로 해줘야함)<br />**소연님 풀이 ㅗ 구하는 것 알기 hhhh함수** | [42577319](https://www.acmicpc.net/submit/14500/42577319) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" alt="img" style="width:20px;" />[1764번](https://www.acmicpc.net/problem/1764)  듣보잡 |                                                              | set1.intersection(set2) 이용                                 | [42537995](https://www.acmicpc.net/submit/1764/42537995)  |



# 15회차 - class 3+ /  분할정복

| 번호                                                         | 설명                                                         | 해결방법                                                     | 제출번호                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------------- |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" alt="img" style="width:20px;" />**[1074번](https://www.acmicpc.net/problem/1074)** Z | 이차원 배열을 4등분 하며 z자 형태로 순회할 때, (r,c)는 몇 번째로 순회하는가? | index를 이용해서 4곳 중 어느 위치인지 파악                   | [42757362](https://www.acmicpc.net/submit/1074/42757362) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" alt="img" style="width:20px;" />[1780번](https://www.acmicpc.net/problem/1780) 종이의 개수 | <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[2630번](https://www.acmicpc.net/problem/2630) 색종이 만들기의 확장버전 / 3x3으로 9등분함 | **index**로만 조작하는 함수 만들어서 다시 해보기<br />**현아님** 풀이처럼 루프로 한번에 처리 | [42755167](https://www.acmicpc.net/submit/1780/42755167) |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" alt="img" style="width:20px;" />[2630번](https://www.acmicpc.net/problem/2630) 색종이 만들기 | <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" alt="img" style="width:20px;" />**[1992번 ](https://www.acmicpc.net/problem/1992)**쿼드트리 의 쉬운 버전 문제로, 2차원 배열을 4등분 해가는 문제 | 2차원 배열이 모두 같은지 판단하는 same 함수와, 모두 같지 않다면 4등분하는 divide 함수를 생성<br />**소연님** 풀이 처럼 1992 활용하기 | [42749038](https://www.acmicpc.net/submit/2630/42749038) |
|                                                              |                                                              |                                                              |                                                          |
|                                                              |                                                              |                                                              |                                                          |
|                                                              |                                                              |                                                              |                                                          |





# 참고

+ input의 개수가 정해지지 않은 경우

  ```python
  # sol1
  
  import sys
  for line in sys.stdin:
      x, y = map(int,line.split())
  
  # sol2
  while True:
      try:
          x, y = map(int,input().spilt())
      except:
          break
  ```

  