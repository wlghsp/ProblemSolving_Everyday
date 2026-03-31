# 📚 프로젝트 문서 맵

## 현재 상태
프로젝트 전반에 걸쳐 산재된 문서들을 정리한 맵입니다.

---

## 🎯 핵심 문서 (루트 레벨)

| 파일 | 위치 | 설명 |
|------|------|------|
| **CLAUDE.md** | `/` | **[중요]** 프로젝트 작업 규칙, 명령어, 파일 생성 규칙 |
| **README.md** | `/` | 프로젝트 개요 |
| **LeetCode_Fundamentals_Study_Guide.md** | `/` | LeetCode 학습 가이드 |

---

## 📂 알고리즘 학습 관련 문서

### LeetCode 반복 풀이 (진행중)
```
/LeetCode/반복풀이/
├── progress.md              # 전체 진행표 (누적 중요)
├── week_2026_03_30.md      # 현재 주간 계획표 (최신)
├── week_2026_03_23.md      # 지난주 계획표
└── (이전 주간 계획표들...)
```

**핵심:**
- `progress.md`: 모든 풀이 기록의 진원지
- `week_*.md`: 주차별 계획 및 실행 결과

### 알고리즘 개념 문서 (LeetCode/)
```
/LeetCode/
├── floyd_cycle_detection.md          # Floyd Cycle Detection 알고리즘
├── linked_list_problems.md           # 연결 리스트 관련 정리
├── tree_problems.md                  # 트리 관련 정리
├── 풀이_계획.md                       # 풀이 계획
└── /leetcode148_Sort_List/
    └── 병합정렬_가이드.md            # 병합정렬 가이드
```

### 개념 노트 (독립)
```
/notes/
├── lazy_evaluation.md     # Lazy Evaluation 개념
```

---

## 💡 메모리 시스템 (Claude AI 기억)

```
/.claude/projects/.../memory/
├── MEMORY.md                        # 메모리 인덱스 (마스터)
└── two_pointer_greedy_proof.md      # Two Pointer Greedy 증명
```

**목적:** 미래 대화에서 학습 내용 참조

---

## 📊 기타 학습 폴더 (우선순위 낮음)

| 폴더 | 설명 |
|------|------|
| `/카카오 코테 6주 합격!` | 카카오 코딩테스트 학습 (이전 교과) |
| `/Baekjoon_Levels/` | 백준 문제 (Bronze/Silver/Gold) |
| `/구름레벨/` | 구름레벨 문제 |
| `/코드업/` | 코드업 문제 |
| `/프로그래머스/` | 프로그래머스 문제 |
| `/기타/` | 기업 코딩테스트, HackerRank 등 |

---

## 🔧 현재 산재 문제

### 문제점
1. **개념 문서 위치 불명확**
   - `floyd_cycle_detection.md` → LeetCode 폴더
   - `lazy_evaluation.md` → notes 폴더
   - `병합정렬_가이드.md` → leetcode148 하위

2. **메모리 시스템 분산**
   - Claude 메모리: `/.claude/projects/.../memory/`
   - 일반 문서: `/notes/`, `/LeetCode/`

3. **계획 문서 혼재**
   - `풀이_계획.md` (구식)
   - `week_*.md` (현행)

---

## ✅ 추천 정리 방안

### 옵션 A: 최소 정리 (지금 바로)
1. `/notes/` 폴더를 `/LeetCode/concepts/`로 통합
2. `병합정렬_가이드.md`를 `/LeetCode/concepts/`로 이동
3. 구식 `풀이_계획.md` 삭제

### 옵션 B: 완전 정리 (권장)
```
/LeetCode/
├── 반복풀이/              # 기존
├── concepts/              # NEW: 알고리즘 개념 모음
│   ├── floyd_cycle_detection.md
│   ├── linked_list_problems.md
│   ├── tree_problems.md
│   ├── merge_sort_guide.md
│   ├── lazy_evaluation.md
│   └── two_pointer_greedy_proof.md
├── floyd_cycle_detection.md (삭제)
└── (다른 문서들)
```

**메모리 시스템은 유지** (자동 참조용)

---

## 📝 권장사항

**현재 상황:**
- ✅ 반복풀이 진행은 체계적 (progress.md + week_*.md)
- ❌ 개념 문서는 산재되어 있음

**우선순위:**
1. 개념 문서를 `/LeetCode/concepts/`로 통합
2. `two_pointer_greedy_proof.md` 등 최신 메모리 문서도 여기 복사
3. 매월 1회 메모리 → 개념 폴더 병합

**예상 시간:** 10-15분 (지금 바로 가능)

---

당신이 결정해주세요:
- **옵션 A**: 가볍게 정리 (notes → concepts)
- **옵션 B**: 완전 정리 (모든 개념 통합)
- **현상 유지**: 지금처럼 계속

어떻게 할까요?