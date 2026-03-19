# Floyd's Cycle Detection Algorithm (토끼와 거북이 알고리즘)

## 핵심 아이디어

두 포인터를 다른 속도로 이동시켜 사이클을 감지한다.
- **slow**: 1칸씩 이동
- **fast**: 2칸씩 이동

사이클이 있으면 fast가 결국 slow를 따라잡아 **같은 노드에서 만난다.**
사이클이 없으면 fast가 먼저 끝(None)에 도달한다.

---

## 기본 패턴

```python
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # 사이클 있음
return False  # 사이클 없음
```

---

## 왜 반드시 만나는가? (수학적 근거)

사이클 길이를 `λ`, 사이클 시작까지 거리를 `μ`라 하면:

- slow가 `k`칸 이동했을 때, fast는 `2k`칸 이동
- 둘 다 사이클 안에 있으면 `(2k - k) = k`가 사이클 길이의 배수가 되는 순간 만남
- 즉, 최대 `λ`번 이동 안에 반드시 만남

**결론**: 사이클이 존재하면 **반드시 만나고**, `O(N)` 안에 감지 가능.

---

## 활용 문제 유형

### 1. 사이클 존재 여부 (141. Linked List Cycle)
```python
# 위의 기본 패턴 그대로 사용
```

### 2. Happy Number (202. Happy Number)
숫자의 각 자리 제곱합을 반복하면 결국 1 또는 사이클로 수렴한다.
- 1에 수렴 → Happy Number
- 사이클 → Not Happy Number

```python
slow = n
fast = getSquares(n)
while fast != 1 and slow != fast:
    slow = getSquares(slow)
    fast = getSquares(getSquares(fast))
return fast == 1
```

### 3. 사이클 시작 노드 찾기 (142. Linked List Cycle II)
만난 지점에서 한 포인터를 head로 옮기고, 둘 다 1칸씩 이동하면 사이클 시작점에서 만남.

```python
# 만난 후
slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next
return slow  # 사이클 시작 노드
```

**수학적 근거**: 만난 지점에서 head까지 거리 = 사이클 시작점까지 거리 (μ)

---

## Set vs Floyd 비교

| | Set 방식 | Floyd 방식 |
|---|---|---|
| 시간복잡도 | O(N) | O(N) |
| 공간복잡도 | **O(N)** | **O(1)** |
| 구현 난이도 | 쉬움 | 보통 |
| 사이클 시작점 찾기 | 가능 (visited에서 확인) | 가능 (추가 로직 필요) |

**실전**: 공간이 중요하거나 면접에서는 Floyd, 빠르게 구현할 때는 Set.

---

## 핵심 요약

1. slow/fast 둘 다 head에서 출발
2. `fast and fast.next` 조건 — fast가 2칸 이동하므로 next.next 접근 전 체크 필수
3. 사이클 있으면 반드시 O(N) 안에 만남
4. 공간복잡도 O(1) — Set 대비 최대 장점
5. Happy Number, 사이클 감지, 사이클 시작점 찾기에 모두 응용 가능
