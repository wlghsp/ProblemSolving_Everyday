# 리트코드 문제 풀이를 위한 기본기 학습 가이드

## 목차
1. [자료구조 직접 구현](#1-자료구조-직접-구현)
2. [비트 연산](#2-비트-연산)
3. [알고리즘 기본 패턴](#3-알고리즘-기본-패턴)
4. [Python 테스팅 및 디버깅](#4-python-테스팅-및-디버깅)
5. [학습 순서 권장사항](#5-학습-순서-권장사항)

---

## 1. 자료구조 직접 구현

### 1.1 배열/리스트 (Array/List)
**학습 내용:**
- 동적 배열의 동작 원리
- 시간 복잡도: 접근 O(1), 삽입/삭제 O(n)
- Python list의 내부 구조

**구현 필요:**
- [ ] 동적 배열 구현 (크기 자동 조절)
- [ ] 배열 회전, 역순 변환

---

### 1.2 연결 리스트 (Linked List)
**학습 내용:**
- 단일 연결 리스트 (Singly Linked List)
- 이중 연결 리스트 (Doubly Linked List)
- 순환 연결 리스트 (Circular Linked List)

**구현 필요:**
- [ ] ListNode 클래스 구현
- [ ] 삽입 (맨 앞, 맨 뒤, 중간)
- [ ] 삭제 (맨 앞, 맨 뒤, 중간, 특정 값)
- [ ] 순회 및 출력
- [ ] 역순 변환 (iterative, recursive)
- [ ] 중간 노드 찾기 (slow-fast pointer)
- [ ] 사이클 탐지

---

### 1.3 스택 (Stack)
**학습 내용:**
- LIFO (Last In First Out) 원리
- 배열 기반 vs 연결 리스트 기반

**구현 필요:**
- [ ] Stack 클래스 (push, pop, peek, isEmpty)
- [ ] 배열 기반 구현
- [ ] 연결 리스트 기반 구현

**응용 문제:**
- 괄호 검증
- 후위 표기식 계산
- 최소값 스택

---

### 1.4 큐 (Queue)
**학습 내용:**
- FIFO (First In First Out) 원리
- 일반 큐, 원형 큐, 덱(Deque)

**구현 필요:**
- [ ] Queue 클래스 (enqueue, dequeue, front, isEmpty)
- [ ] 원형 큐 (Circular Queue)
- [ ] 덱 (Deque - 양방향 삽입/삭제)

**Python 내장:**
- `collections.deque` 사용법

---

### 1.5 이진 트리 (Binary Tree)
**학습 내용:**
- 트리 기본 용어 (root, leaf, parent, child, height, depth)
- 이진 트리의 종류 (완전, 포화, 균형)
- 트리 순회 (Traversal)

**구현 필요:**
- [ ] TreeNode 클래스 구현
- [ ] 배열로부터 트리 생성 (레벨 순서)
- [ ] 전위 순회 (Preorder - Root, Left, Right)
- [ ] 중위 순회 (Inorder - Left, Root, Right)
- [ ] 후위 순회 (Postorder - Left, Right, Root)
- [ ] 레벨 순서 순회 (Level-order - BFS)
- [ ] 트리 높이 계산
- [ ] 트리 출력/시각화

**핵심 패턴:**
- 재귀적 사고 (대부분의 트리 문제)
- BFS (큐 사용) vs DFS (재귀 또는 스택)

---

### 1.6 이진 탐색 트리 (Binary Search Tree)
**학습 내용:**
- BST 속성: 왼쪽 < 부모 < 오른쪽
- 탐색, 삽입, 삭제 연산

**구현 필요:**
- [ ] BST 검증 (유효한 BST인지 확인)
- [ ] 삽입
- [ ] 삭제
- [ ] 탐색
- [ ] 최소/최대값 찾기
- [ ] 중위 순회 → 정렬된 배열

---

### 1.7 힙 (Heap)
**학습 내용:**
- 최소 힙 (Min Heap), 최대 힙 (Max Heap)
- 완전 이진 트리 구조
- 배열로 힙 표현 (인덱스 관계)

**구현 필요:**
- [ ] heapify (힙 속성 유지)
- [ ] insert
- [ ] extract_min / extract_max
- [ ] heap_sort

**Python 내장:**
- `heapq` 모듈 사용법 (최소 힙만 제공)
- 최대 힙 구현 방법 (음수 활용)

---

### 1.8 해시 테이블 (Hash Table)
**학습 내용:**
- 해시 함수의 원리
- 충돌 해결 (Chaining, Open Addressing)

**구현 필요:**
- [ ] 간단한 해시 테이블 (chaining 방식)
- [ ] get, put, remove

**Python 내장:**
- `dict` 사용법
- `collections.defaultdict`
- `collections.Counter`

---

### 1.9 그래프 (Graph)
**학습 내용:**
- 인접 리스트 vs 인접 행렬
- 유향 그래프 vs 무향 그래프
- 가중치 그래프

**구현 필요:**
- [ ] 그래프 표현 (인접 리스트)
- [ ] DFS (재귀, 스택)
- [ ] BFS (큐)
- [ ] 사이클 탐지
- [ ] 위상 정렬

---

### 1.10 트라이 (Trie)
**학습 내용:**
- 문자열 검색 트리
- Prefix 검색에 효율적

**구현 필요:**
- [ ] TrieNode 클래스
- [ ] insert
- [ ] search
- [ ] startsWith

---

## 2. 비트 연산

### 2.1 기본 비트 연산자
**학습 내용:**
- `&` (AND): 두 비트가 모두 1일 때 1
- `|` (OR): 둘 중 하나라도 1이면 1
- `^` (XOR): 두 비트가 다를 때 1
- `~` (NOT): 비트 반전
- `<<` (Left Shift): 왼쪽으로 이동 (2배)
- `>>` (Right Shift): 오른쪽으로 이동 (1/2배)

**연습 문제:**
- [ ] 특정 비트 확인하기
- [ ] 특정 비트 설정하기
- [ ] 특정 비트 클리어하기
- [ ] 특정 비트 토글하기

---

### 2.2 비트 연산 패턴
**학습 내용:**

1. **XOR의 특성**
   - `a ^ a = 0`
   - `a ^ 0 = a`
   - 교환법칙, 결합법칙 성립
   - 활용: 중복 제거, 두 수 교환

2. **비트 마스크 (Bit Mask)**
   - 특정 비트만 추출/조작
   - 부분 집합 생성

3. **2의 거듭제곱 판별**
   - `n & (n-1) == 0`

4. **최하위 비트 추출**
   - `n & -n`

5. **비트 카운팅**
   - 1의 개수 세기 (Hamming Weight)

**연습 문제:**
- [ ] Single Number (XOR 활용)
- [ ] Power of Two
- [ ] Counting Bits
- [ ] Bitwise AND of Numbers Range

---

### 2.3 비트 연산 시각화
**학습 방법:**
- 2진수로 변환해서 손으로 직접 계산
- Python: `bin()` 함수로 확인
```python
# 예시
a = 5    # 0101
b = 3    # 0011
print(bin(a & b))  # 0001 = 1
print(bin(a | b))  # 0111 = 7
print(bin(a ^ b))  # 0110 = 6
```

---

## 3. 알고리즘 기본 패턴

### 3.1 투 포인터 (Two Pointers)
**학습 내용:**
- 양쪽 끝에서 시작
- 같은 방향으로 이동
- 빠른/느린 포인터

**연습 문제:**
- [ ] Two Sum (정렬된 배열)
- [ ] 팰린드롬 검증
- [ ] 연결 리스트 사이클

---

### 3.2 슬라이딩 윈도우 (Sliding Window)
**학습 내용:**
- 고정 크기 윈도우
- 가변 크기 윈도우

**연습 문제:**
- [ ] Maximum Sum Subarray
- [ ] Longest Substring Without Repeating Characters

---

### 3.3 이진 탐색 (Binary Search)
**학습 내용:**
- 정렬된 배열에서 O(log n) 탐색
- 경계 조건 처리

**구현 필요:**
- [ ] 기본 이진 탐색
- [ ] Lower bound / Upper bound
- [ ] 회전된 배열에서 탐색

---

### 3.4 동적 프로그래밍 (Dynamic Programming)
**학습 내용:**
- Memoization (Top-down)
- Tabulation (Bottom-up)
- 상태 정의, 점화식

**연습 문제:**
- [ ] Fibonacci
- [ ] Climbing Stairs
- [ ] Longest Common Subsequence

---

### 3.5 백트래킹 (Backtracking)
**학습 내용:**
- 재귀적 탐색
- 가지치기 (Pruning)

**연습 문제:**
- [ ] Permutations
- [ ] Subsets
- [ ] N-Queens

---

### 3.6 그리디 (Greedy)
**학습 내용:**
- 매 순간 최선의 선택
- 증명의 중요성

**연습 문제:**
- [ ] Jump Game
- [ ] Gas Station

---

## 4. Python 테스팅 및 디버깅

### 4.1 테스트 케이스 작성
**학습 내용:**
- 리트코드 입력을 Python 객체로 변환
- 트리/연결 리스트를 배열로부터 생성

**유틸리티 함수 구현:**
- [ ] `build_tree(values)` - 배열 → 이진 트리
- [ ] `build_linked_list(values)` - 배열 → 연결 리스트
- [ ] `tree_to_list(root)` - 트리 → 배열 (레벨 순서)
- [ ] `linked_list_to_list(head)` - 연결 리스트 → 배열

---

### 4.2 디버깅 기법
**학습 내용:**
- `print()` 디버깅
- Python Debugger (pdb)
- 시각화 (트리 출력)

---

### 4.3 시간/공간 복잡도 분석
**학습 내용:**
- Big-O 표기법
- 각 자료구조/알고리즘의 복잡도

---

## 5. 학습 순서 권장사항

### Phase 1: 기초 자료구조 (1-2주)
1. 배열/리스트 조작
2. 연결 리스트 구현 및 문제
3. 스택/큐 구현 및 문제
4. 해시 테이블 활용

### Phase 2: 트리 마스터 (2-3주)
1. 이진 트리 구현 (TreeNode, 순회)
2. 트리 빌더 함수 작성
3. 이진 탐색 트리 이해
4. 트리 기본 문제 풀이 (20-30문제)

### Phase 3: 비트 연산 (1주)
1. 비트 연산자 기본
2. 비트 마스크 패턴
3. 비트 조작 문제 풀이 (10-15문제)

### Phase 4: 고급 자료구조 (2주)
1. 힙 구현 및 활용
2. 그래프 표현 및 탐색
3. 트라이 (필요시)

### Phase 5: 알고리즘 패턴 (지속적)
1. 투 포인터, 슬라이딩 윈도우
2. 이진 탐색
3. 동적 프로그래밍
4. 백트래킹
5. 그리디

---

## 6. 실전 팁

### 문제 풀이 전 체크리스트
- [ ] 입력/출력 형식 정확히 이해
- [ ] 제약 조건 확인 (범위, 음수 가능성 등)
- [ ] 간단한 예시로 로직 검증
- [ ] 엣지 케이스 고려 (빈 입력, 단일 요소 등)
- [ ] 시간/공간 복잡도 예상

### 막힐 때 대처법
1. 무작정 코드부터 작성하지 말 것
2. 손으로 예시 풀어보기
3. 비슷한 문제 찾아보기
4. 브루트포스 → 최적화 순서로 접근
5. 필요하면 솔루션 보되, 이해 후 스스로 재구현

---

## 7. 추천 리소스

### 온라인 강의
- Coursera: Algorithms Specialization (Stanford)
- LeetCode Explore Cards (무료)

### 책
- "Cracking the Coding Interview" - Gayle Laakmann McDowell
- "Elements of Programming Interviews in Python"

### 연습 사이트
- LeetCode (Easy → Medium → Hard 순서)
- HackerRank
- Codeforces (알고리즘 대회)

---

## 8. 다음 단계

각 항목별로 구체적인 코드 구현이 필요하면 개별적으로 요청하세요:

**예시:**
- "이진 트리 빌더 함수 구현해줘"
- "비트 마스크로 부분 집합 생성하는 방법 알려줘"
- "연결 리스트 역순 변환 코드 작성해줘"

하나씩 차근차근 학습하시면 리트코드 문제 풀이 실력이 크게 향상될 것입니다!
