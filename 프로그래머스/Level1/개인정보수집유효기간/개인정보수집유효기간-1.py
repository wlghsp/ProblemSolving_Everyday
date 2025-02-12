def get_days(date):
    year, month, day = map(int, date.split('.'))
    return (year - 2000)  * (28 * 12) + (month - 1) * 28 + day

def solution(today, terms, privacies):
    answer = []
    term_db = {k: int(v) * 28 for k, v in (t.split() for t in terms)}

    today_days = get_days(today)
    for i, privacy in enumerate(privacies):
        date, policy = privacy.split()
        days = get_days(date)
        expiration_days = days + term_db[policy] - 1
        if today_days > expiration_days: # 오늘날짜가 유효기간보다 크거나 같다면
            answer.append(i + 1)

    return answer


print(solution(
"2022.05.19",
    ["A 6", "B 12", "C 3"], # "약관종류 유효기간"
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"] # "날짜 약관종류"
)) # [1, 3]