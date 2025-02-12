def solution(survey, choices):
    characters = ["RT", "CF", "JM", "AN"]
    table = {alpha: 0 for alpha in list("RTCFJMAN")}
    for s, choice in zip(survey, choices):
        if choice >= 4:
            table[s[1]] += choice - 4
        else:
            table[s[0]] += 4 - choice

    result = []
    for c in characters:
        result.append(c[0] if table[c[0]] >= table[c[1]] else c[1])

    return ''.join(result)


print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])) # "TCMA"