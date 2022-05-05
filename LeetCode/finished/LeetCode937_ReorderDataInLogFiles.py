
def reorderLogFiles(logs):
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # identifier를 제외한 문자열을 키로 두어서 정렬을 하고, 동일한 경우에는 [0]을 기준으로 정렬되도록 하였다.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits



logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))