# sorting

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







# 문자열

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







# *브루트 포스* 다시 풀기

| 번호                                           | 설명   | 해결방법             | 제출번호                                                     |
| ---------------------------------------------- | ------ | -------------------- | ------------------------------------------------------------ |
| [2798번](https://www.acmicpc.net/problem/2798) | 블랙잭 | bit 로 부분집합 생성 | [39507291](https://www.acmicpc.net/submit/2798/39507291) 시간초과 |
|                                                |        |                      |                                                              |
|                                                |        |                      |                                                              |







# *Stack* 마저 풀기

| 번호                                             | 설명                                  | 해결방법                      | 제출번호                                                  |
| ------------------------------------------------ | ------------------------------------- | ----------------------------- | --------------------------------------------------------- |
| [10828번](https://www.acmicpc.net/problem/10828) | stack 구현(top,push, pop, empty,size) | stack class 생성              | [39718701](https://www.acmicpc.net/submit/10828/39718701) |
| [10773번](https://www.acmicpc.net/problem/10773) | stack 이용해서 숫자합 세기            |                               | [39721292](https://www.acmicpc.net/submit/10773/39721292) |
| [9012번](https://www.acmicpc.net/problem/9012)   | () 괄호짝맞추기                       | stack 생성( 오류 case 2 가지) | [39723612](https://www.acmicpc.net/submit/9012/39723612)  |
| 4949번                                           |                                       |                               |                                                           |
| 1874번                                           |                                       |                               |                                                           |
| 17298번                                          |                                       |                               |                                                           |





#  큐 & 덱

| 번호                                             | 설명                                                         | 해결방법                                                     | 제출번호                                                  |
| ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------- |
| [18258번](https://www.acmicpc.net/problem/18258) | 큐 구현(push, pop, front, back, size, empty)                 | collections.deque & sys.stdin.readline()이용                 | [40317941](https://www.acmicpc.net/submit/18258/40317941) |
| [2164번](https://www.acmicpc.net/problem/2164)   | 맨 위 카드 1장 버리고, 다음 맨 위 카드 맨 밑으로 넣는 것 반복 시, 마지막에 남는 카드 | collections.deque 이용                                       | [40298328](https://www.acmicpc.net/submit/2164/40298328)  |
| [11866번](https://www.acmicpc.net/problem/11866) | (N,K)-요세푸스 순열                                          | collections.deque에 모든 수 넣고, 맨 앞에거 빼서 맨 뒤로 집어넣는 거 반복하는 도중, 매 K 번째 것을 출력 | [40317091](https://www.acmicpc.net/submit/11866/40317091) |
| [1966번](https://www.acmicpc.net/problem/1966)   | 프린터 큐 (중요도 순서에 따라 문서 인쇄)                     | deque 이용 / 문서 중요도를 dict로 만들어 활용                | [40298915](https://www.acmicpc.net/submit/1966/40298915)  |
|                                                  |                                                              |                                                              |                                                           |

4, 8



# BFS&DFS

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
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px" />***[2206번](https://www.acmicpc.net/problem/2206)*** | 벽부수고 최단거리 이동                                       | BFS 이용. 모르겠음                                           | [40886487](https://www.acmicpc.net/submit/2206/40886487) 틀림 |
| [7562번](https://www.acmicpc.net/problem/7562)               | 나이트를 목표지점에 움직이는 최단거리                        | BFS 이용                                                     | [40823688](https://www.acmicpc.net/submit/7562/40823688)     |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px;" />***[1707번](https://www.acmicpc.net/problem/1707)*** | 이분 그래프 판별                                             | DFS + Dictionary 이용<br />노드이동 풀이                     | [40885796 ](https://www.acmicpc.net/submit/1707/40885796)시간초과<br />[40880220](https://www.acmicpc.net/submit/1707/40880220) 메모리초과 |

+ 7576번 : 주현님 풀이 보기





# 트리

| 번호                                                         | 설명                                        | 해결방법                                                     | 제출번호                                                     |
| ------------------------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [11725번](https://www.acmicpc.net/problem/11725)             | 트리의 부모노드 찾기                        | index를 자식, value를 부모로하는 tree 생성                   | [40883123](https://www.acmicpc.net/submit/11725/40883123) 시간초과 |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" alt="img" style="width:20px;" />[1991번 ](https://www.acmicpc.net/problem/1991) | 트리의 pre,in,post order 순회               |                                                              | [40884311](https://www.acmicpc.net/submit/1991/40884311)     |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/13.svg" alt="img" style="width:20px;" /> [1167번](https://www.acmicpc.net/problem/1167) | 트리지름구하기                              | dfs 재귀구현                                                 | [40954377](https://www.acmicpc.net/submit/1167/40954377) 메모리초과 |
| <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" alt="img" style="width:20px;" /> [1967번](https://www.acmicpc.net/problem/1967) | 트리 지름 구하기                            | dfs 재귀구현<br />후위탐색 재귀구현<br />후위탐색 재귀구현<br />sys.setrecursionlimit(10**9) | [41039735](https://www.acmicpc.net/submit/1967/41039735) 시간초과<br />[41041676](https://www.acmicpc.net/submit/1967/41041676) 재귀초과<br />[41042182](https://www.acmicpc.net/submit/1967/41042182) 재귀초과(위의 것 post인자 1개로 한 것)<br />[41043495](https://www.acmicpc.net/submit/1967/41043495) value error |
| ***<img src="https://d2gd6pc034wcta.cloudfront.net/tier/14.svg" alt="img" style="width:20px;" />[2263번](https://www.acmicpc.net/problem/2263)*** | 이진트리 중,후위순회로 전위순회 찾기        | sys.setrecursionlimit(10**9)<br />in_order에서 특정 값의 index 가져오기 위해, list 하나 만들고 시작하기(left,right만들어서 함)<br />left, right  안만들고, 바로 index로 계산 | [41045481][https://www.acmicpc.net/submit/2263/41045481] 시간초과<br />**[41101636](https://www.acmicpc.net/submit/2263/41101636)**<br />[41101739](https://www.acmicpc.net/submit/2263/41101739) |
| *** <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" alt="img" style="width:20px;" />[5639번](https://www.acmicpc.net/problem/5639)*** | 이진검색트리에서 전위순회를 후위순회로 변환 | 이진검색트리는 좌측노드의 값이 우측노드의 값보다 작으므로,  전위순회의 첫 원소가 root, root 보다 작은 첫 값이 왼쪽 노드, root보다 큰 첫 값이 오른쪽 노드 | [41122756](https://www.acmicpc.net/submit/5639/41122756)     |



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

  
