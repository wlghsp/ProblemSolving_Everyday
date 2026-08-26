# 알고리즘 마스터 로드맵

유형별로 "작은 연습 세트(Level 1~N)"를 먼저 소화하고, 졸업하면 해당 유형의 실전 LeetCode 문제를
`반복풀이/` 주간 계획표에 우선 배치하는 방식으로 진행한다.

## 진행 방식

1. 트랙 하나를 고른다 (아래 순서 권장, 필요하면 순서 무시하고 골라도 됨)
2. 그 트랙 폴더에 Level 1 연습 파일을 요청해서 만든다 (`{트랙} 연습` 같은 식으로 요청)
3. Level을 하나씩 졸업하면서 다음 Level로 진행
4. 트랙의 마지막 Level까지 졸업하면 → `반복풀이/`에 해당 유형 실전 문제를 우선 배치해서 패턴 인식 훈련으로 연결
5. 이 문서의 상태 표를 갱신 (Claude가 자동 업데이트)

## 트랙 순서 (기초 → 응용 → 결합)

| 순서 | 트랙 | 폴더 | 선행 트랙 |
|---|---|---|---|
| 1 | Array / Two Pointer | `array_two_pointer/` | - |
| 2 | Sliding Window | `sliding_window/` | Two Pointer |
| 3 | Hash Map | `hash_map/` | - |
| 4 | Stack | `stack/` | - |
| 5 | Binary Search | `binary_search/` | - |
| 6 | Linked List | `linked_list/` | - |
| 7 | Backtracking (순열/조합) | `permutation_combination/` | - |
| 8 | Bit Manipulation | `bitmask/` | - |
| 9 | Tree / BST | `tree_bst/` | - |
| 10 | Graph / BFS / DFS | `graph_bfs_dfs/` | Tree |
| 11 | Heap | `heap/` | - |
| 12 | Greedy | `greedy/` | - |
| 13 | DP (기본 -> 상태 정의) | `dp/` | Backtracking 권장 |
| 14 | DP over Bitmask (TSP 등 결합) | `bitmask/` (Level 5~6) | DP + Bit Manipulation |

### DP 트랙 세부 Level 목차 (`dp/`)

| Level | 주제 | 핵심 감각 |
|---|---|---|
| 1 | 1D DP 기초 (계단 오르기 경우의 수 / 최소비용) | 점화식 `dp[i] = f(dp[i-1], dp[i-2])` 세우기 |
| 2 | 공간 최적화 (배열 -> 변수 롤링) | O(N) 배열을 O(1) 변수 몇 개로 줄이기 |
| 3 | 상태 확장 (마지막 행동을 상태에 포함) | `dp[i][state]` 형태로 전이 분기 늘리기 |
| 4 | INF/불가능 상태 안전하게 다루기 | `float('inf')` 패턴, 덧셈 오염 방지 |
| 5 | 부분열/구간 DP (LIS류) | O(N^2) 이중 루프 점화식 감각 |
| 6 | 종합 (상태 확장 + 공간 최적화 결합) | 연속 제약이 있는 상태 DP 스스로 설계 |

## 상태 표

| 트랙 | 최고 Level | 상태 | 비고 |
|---|---|---|---|
| Bit Manipulation | Level 6 존재 (`bitmask/`) | 진행 중 | Level 1, 2, 3 [x] 완료 (2026-08-23). 다음: Level 4 (`conflict_selection`) 리뷰 진행 중 |
| Backtracking (순열/조합) | Level 2 (`permutation_combination/`) | 진행 중 | Level 1 `permute`, `permute_count` [x] 완료 (2026-08-23). Level 2 `combine`, `combine_count` [x] 완료 (2026-08-25). 다음: Level 3 |
| DP | Level 4 (`dp/`) | 진행 중 | Level 1, 2, 3, 4 [x] 완료 (2026-08-26). 다음: Level 5 (구간 DP) 또는 바로 Level 6(종합, "피로도 계단" 문제) 도전 가능 |
| 나머지 | - | 미착수 | - |

## 규칙 (CLAUDE.md 연장)

- 연습 파일은 함수 시그니처 + 힌트 주석 + 테스트 케이스만 생성, 정답 코드는 넣지 않는다
- 표준 라이브러리로 문제를 우회하는 것 금지 (예: `itertools.permutations`, `bin().count("1")`, `math.factorial`)
- Level 하나를 힌트 없이 통과 + 이해도 질문에 답하면 다음 Level로
- 트랙 하나를 끝까지 졸업하면 이 표의 "상태"를 "졸업"으로 갱신하고 해당 유형 실전 문제를 `반복풀이/`에 우선 배치
