from collections import defaultdict


def solution(tickets):
    plans = defaultdict(list)
    ticket_used = [False] * len(tickets)
    for a, b in tickets:
        plans[a].append(b)
    answer = []
    for p in plans.values():
        p.sort()

    def ticked_all_used():
        for used in ticket_used.values():
            if not used:
                return False
        return True
    def dfs(start, picked):
        if ticked_all_used():
            answer.append(picked)
            return

        for i in range(len(tickets)):
            if tickets[i][0] != start: continue
            if ticket_used[i]: continue

            ticket_used[i] = True
            dfs(tickets[i][1], )

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
