def solution(tickets):
    ticket_used = [False] * len(tickets)

    def all_ticket_used():
        for used in ticket_used:
            if not used: return False
        return True

    def get_path(picked):
        result = ["ICN"]
        for i in picked:
            result.append(tickets[i][1])
        return result


    answer = []
    def dfs(start, picked):
        if all_ticket_used():
            result = get_path(picked)
            answer.append(result)
            return

        for i in range(len(tickets)):
            if ticket_used[i]: continue
            if tickets[i][0] != start: continue

            ticket_used[i] = True
            dfs(tickets[i][1], picked + [i])
            ticket_used[i] = False

    dfs("ICN", [])
    answer.sort()
    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
