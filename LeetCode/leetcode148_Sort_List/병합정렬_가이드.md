# 병합정렬 (Merge Sort) 완벽 가이드

## 📌 이 문서의 목적

LeetCode 148번을 풀기 위해 꼭 알아야 할 병합정렬 개념을 정리했습니다.
연결 리스트 버전이 어렵다면 배열 버전부터 시작하세요!

---

## 📚 1단계: 배열 병합정렬 (기본)

**연결 리스트가 어렵다면? 먼저 배열 버전을 이해하세요!**

### 병합정렬이란?

**분할 정복(Divide and Conquer) 알고리즘:**
1. **분할(Divide)**: 배열을 반으로 나누기
2. **정복(Conquer)**: 각 부분을 재귀적으로 정렬
3. **병합(Merge)**: 정렬된 두 부분을 합치기

### 동작 원리

```
[4, 2, 1, 3]
     ↓ 분할
[4, 2]  [1, 3]
     ↓ 분할
[4] [2]  [1] [3]
     ↓ 병합 (정렬하며)
[2, 4]  [1, 3]
     ↓ 병합 (정렬하며)
[1, 2, 3, 4]
```

### 배열 병합정렬 코드

```python
def merge_sort_array(arr):
    """배열을 병합정렬로 정렬"""
    # 베이스 케이스: 길이가 1 이하면 이미 정렬됨
    if len(arr) <= 1:
        return arr

    # 1. 분할: 중간 인덱스로 나누기
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 2. 재귀: 각 부분을 정렬
    left = merge_sort_array(left)
    right = merge_sort_array(right)

    # 3. 병합: 정렬된 두 배열을 합치기
    return merge_arrays(left, right)


def merge_arrays(left, right):
    """두 정렬된 배열을 하나로 병합"""
    result = []
    i = j = 0

    # 양쪽 배열을 비교하며 작은 값부터 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 테스트
arr = [4, 2, 1, 3]
print(merge_sort_array(arr))  # [1, 2, 3, 4]
```

### 단계별 동작 예시

```python
# 입력: [4, 2, 1, 3]

# 1단계: 분할
merge_sort_array([4, 2, 1, 3])
  ├─ merge_sort_array([4, 2])
  │   ├─ merge_sort_array([4]) → [4]
  │   └─ merge_sort_array([2]) → [2]
  │   └─ merge([4], [2]) → [2, 4]
  └─ merge_sort_array([1, 3])
      ├─ merge_sort_array([1]) → [1]
      └─ merge_sort_array([3]) → [3]
      └─ merge([1], [3]) → [1, 3]

# 2단계: 병합
merge([2, 4], [1, 3]) → [1, 2, 3, 4]
```

---

## 🔄 2단계: 배열 vs 연결 리스트 비교

### 핵심 차이점

| 단계 | 배열 | 연결 리스트 |
|------|------|-------------|
| **분할** | `mid = len(arr) // 2` | Slow & Fast Pointer |
| **접근** | `arr[mid]` (O(1)) | 처음부터 순회 (O(n)) |
| **병합** | 새 배열 생성 (O(n) 공간) | 포인터만 조작 (O(1) 공간) |
| **공간 복잡도** | O(n) | O(log n) (재귀만) |

### 배열 - 중간 찾기

```python
# 간단! 인덱스로 바로 접근
mid = len(arr) // 2
left = arr[:mid]
right = arr[mid:]
```

### 연결 리스트 - 중간 찾기 (어려움!)

```python
# Slow & Fast Pointer 필요
def get_mid(head):
    slow = head
    fast = head.next  # 한 칸 앞서 시작

    while fast and fast.next:
        slow = slow.next        # 1칸 전진
        fast = fast.next.next   # 2칸 전진

    return slow  # slow가 중간 노드
```

**왜 fast를 한 칸 앞서 시작?**
- [1, 2]를 정확히 [1] | [2]로 분할하기 위해
- fast = head로 시작하면 분할이 안 됨

### 배열 - 병합

```python
# 새 배열에 복사 (공간 O(n))
def merge_arrays(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 연결 리스트 - 병합 (효율적!)

```python
# 포인터만 조작 (공간 O(1))
def merge(l1, l2):
    dummy = ListNode(0)  # 더미 노드
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # 남은 노드 연결
    tail.next = l1 if l1 else l2

    return dummy.next
```

---

## 🎯 왜 연결 리스트가 더 어려운가?

### 배열의 장점
✅ 중간 접근이 쉬움: `arr[len//2]`
✅ 직관적: 슬라이싱으로 쉽게 분할
✅ 시각화 쉬움: 인덱스로 위치 파악

### 연결 리스트의 어려움
❌ 중간 접근 어려움: 처음부터 순회 필요
❌ Slow & Fast Pointer 개념 필요
❌ 포인터 조작 실수하기 쉬움

### 하지만 연결 리스트의 장점!
✅ **공간 효율적**: 병합 시 새 메모리 불필요
✅ **포인터만 조작**: O(1) 추가 공간
✅ **면접 빈출**: 포인터 조작 능력 테스트

---

## 💻 3단계: 연결 리스트 병합정렬

### 전체 코드

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 베이스 케이스
        if not head or not head.next:
            return head

        # 1. 중간 노드 찾기
        mid = self.get_mid(head)
        right = mid.next
        mid.next = None  # 리스트 절단!

        # 2. 재귀 정렬
        left = self.sortList(head)
        right = self.sortList(right)

        # 3. 병합
        return self.merge(left, right)

    def get_mid(self, head):
        """Slow & Fast Pointer로 중간 찾기"""
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, l1, l2):
        """두 정렬된 리스트 병합"""
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next
```

### 동작 예시

```
입력: 4 -> 2 -> 1 -> 3

1단계: 중간 찾기 (mid = 2)
[4 -> 2] | [1 -> 3]

2단계: 재귀 분할
[4] [2] | [1] [3]

3단계: 병합
[2 -> 4] | [1 -> 3]

4단계: 최종 병합
[1 -> 2 -> 3 -> 4]
```

---

## 🤔 자주하는 실수

### 1. 중간 노드를 끊지 않음

```python
# ❌ 잘못된 코드
mid = get_mid(head)
right = mid.next
# mid.next = None 을 안 함! → 무한 재귀

# ✅ 올바른 코드
mid = get_mid(head)
right = mid.next
mid.next = None  # 반드시 끊어야 함!
```

### 2. Fast Pointer 시작 위치 실수

```python
# ❌ 둘 다 같은 위치
slow = head
fast = head  # → [1,2]일 때 분할 안 됨

# ✅ Fast를 한 칸 앞서 시작
slow = head
fast = head.next  # → 정확히 반으로 나눔
```

### 3. Merge에서 남은 노드 처리 안 함

```python
# ❌ while만 돌고 끝
while l1 and l2:
    # ...
# 남은 노드 처리 안 함

# ✅ 남은 노드 연결
tail.next = l1 if l1 else l2
```

---

## ⏱️ 복잡도 분석

### 시간 복잡도: O(n log n)

**왜 O(n log n)인가?**
- **분할**: log n 레벨 (절반씩 나눔)
- **병합**: 각 레벨에서 O(n) 작업
- **총**: O(n) × log n = O(n log n)

```
레벨 0: [8개] - n번 작업
레벨 1: [4개][4개] - n번 작업
레벨 2: [2개][2개][2개][2개] - n번 작업
레벨 3: [1][1][1][1][1][1][1][1] - n번 작업

총 레벨: log n
각 레벨 작업: O(n)
→ O(n log n)
```

### 공간 복잡도

**배열:** O(n)
- 병합할 때마다 새 배열 생성

**연결 리스트:** O(log n)
- 재귀 호출 스택만 사용
- 포인터 조작으로 병합 (추가 공간 없음)

---

## 📝 학습 순서 추천

### 1단계: 배열 병합정렬 완벽 이해
```python
arr = [4, 2, 1, 3]
result = merge_sort_array(arr)
print(result)  # [1, 2, 3, 4]
```

### 2단계: Slow & Fast Pointer 연습
- LeetCode 876: Middle of the Linked List

### 3단계: 연결 리스트 병합 연습
- LeetCode 21: Merge Two Sorted Lists

### 4단계: 연결 리스트 병합정렬 도전!
- LeetCode 148: Sort List

---

## 💡 디버깅 팁

막혔다면 각 단계를 출력해보세요:

```python
def sortList(head):
    print(f"Sorting: {list_to_array(head)}")

    if not head or not head.next:
        return head

    mid = get_mid(head)
    print(f"Mid value: {mid.val}")

    right = mid.next
    mid.next = None

    left = sortList(head)
    right = sortList(right)

    result = merge(left, right)
    print(f"Merged: {list_to_array(result)}")

    return result
```

---

## 🚀 추가 학습 자료

### 관련 문제
1. LeetCode 21: Merge Two Sorted Lists (병합 연습)
2. LeetCode 876: Middle of the Linked List (중간 찾기)
3. LeetCode 206: Reverse Linked List (포인터 조작)
4. LeetCode 148: Sort List (최종 목표!)

### 다음 단계
- **Follow-up**: Bottom-up Merge Sort로 O(1) 공간 달성
- **응용**: k개의 정렬된 리스트 병합 (LeetCode 23)

---

화이팅! 병합정렬을 완벽히 이해하면 많은 문제가 쉬워집니다! 🔥
