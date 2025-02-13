def solution(data, ext, val_ext, sort_by):
    sort_str_idx = {col_name: idx for idx, col_name in enumerate(["code", "date", "maximum", "remain"])}

    answer = [d for d in data if d[sort_str_idx[ext]] < val_ext]

    answer.sort(key=lambda x: x[sort_str_idx[sort_by]])

    return answer


print(solution(
[[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
"date",
20300501,
"remain"
)) # [[3,20300401,10,8],[1,20300104,100,80]]