# Lazy Evaluation (지연 평가)

## 핵심 개념
"필요할 때만 계산한다" — 미리 다 계산해두지 않고, 실제로 값이 필요한 순간에 계산.

반대 개념: **Eager Evaluation (즉시 평가)** — 미리 다 계산해두는 방식.

---

## 알고리즘에서의 예시

### 1. BST Iterator (173번)
```python
# Eager: 처음에 inorder 전체 계산 → O(N) 공간
self.vals = []
self.inorder(root)  # 다 저장해둠

# Lazy: next() 호출 때마다 필요한 만큼만 계산 → O(H) 공간
def next(self):
    node = self.stk.pop()
    self._push_left(node.right)  # 지금 당장 필요한 것만 처리
    return node.val
```

### 2. Generator (Python)
```python
# Eager: 리스트 → 메모리에 다 올림
squares = [x**2 for x in range(10**9)]  # 메모리 폭발

# Lazy: 제너레이터 → 필요할 때만 계산
squares = (x**2 for x in range(10**9))  # 메모리 O(1)
next(squares)  # 그때그때 계산
```

### 3. 무한 수열
```python
# Lazy 없이는 무한 수열 표현 불가
# 제너레이터로 무한 피보나치
def fib():
    a, b = 0, 1
    while True:
        yield a        # 호출될 때만 값 생성
        a, b = b, a + b
```

### 4. 백트래킹 / 탐색
- DFS는 lazy: 모든 경로를 미리 계산하지 않고 한 경로씩 탐색
- BFS도 필요한 레벨만 처리

---

## 실무에서의 예시

### 데이터베이스 ORM (Django/SQLAlchemy)
```python
# 이 시점엔 쿼리 실행 안 함 (lazy)
users = User.objects.filter(active=True)

# 실제 데이터 접근할 때 쿼리 실행
for user in users:  # 여기서 DB hit
    print(user.name)
```

### React (렌더링)
- 상태가 바뀐 컴포넌트만 재렌더링 → 필요할 때만 계산

### Haskell
- 기본이 lazy evaluation → 무한 리스트 기본 지원

---

## 언제 Lazy가 유리한가?

| 상황 | 이유 |
|------|------|
| 전체 결과가 필요 없을 때 | 앞 몇 개만 쓰면 나머지 계산 낭비 |
| 데이터가 무한하거나 매우 클 때 | 메모리에 다 올릴 수 없음 |
| 계산 비용이 클 때 | 안 쓸 수도 있는 값을 미리 계산하면 낭비 |
| 공간 복잡도를 줄이고 싶을 때 | O(N) → O(H) 또는 O(1)로 개선 가능 |

## 언제 Eager가 유리한가?

| 상황 | 이유 |
|------|------|
| 전체 결과를 반드시 써야 할 때 | lazy의 오버헤드가 오히려 손해 |
| 계산을 재사용할 때 | 캐싱 효과 |
| 코드 단순성이 중요할 때 | lazy는 구현이 복잡해질 수 있음 |

---

## 면접 포인트
- "왜 O(N) 대신 O(H) 공간이 가능한가?" → Lazy evaluation으로 필요한 만큼만 스택에 유지
- BST Iterator 스택 방식이 대표적인 lazy 패턴
