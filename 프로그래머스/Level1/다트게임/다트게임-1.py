def solution(dartResult):
    scores = []
    area = {'S' : 1, 'D' : 2, 'T' : 3}
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            score = 0
            # 1. 점수 처리
            if dartResult[i:i + 2] == '10':
                score = 10
                i += 2
            else:
                score = int(dartResult[i])
                i += 1

            # 2. 보너스 처리
            score = score ** area[dartResult[i]]
            i += 1
            # 3. 옵션 처리 전에 숫자 담기
            scores.append(score)

            # 4. 옵션 처리 전 확인
            if i >= len(dartResult): break

            # 5. 옵션 처리
            if dartResult[i] == '*': # 앞과 현재점수 2배
                if len(scores) > 1:
                    scores[-2] *= 2
                scores[-1] *= 2
                i += 1
            elif dartResult[i] == '#': # 점수를 마이너스 처리
                scores[-1] *= -1
                i += 1
        else:
            i += 1

    return sum(scores)

print(solution("1S2D*3T")) # 37
print(solution("1D2S#10S")) # 9
print(solution("1D2S0T")) # 3
print(solution("1S*2T*3S")) # 23
print(solution("1D#2S*3S")) # 5
print(solution("1T2D3D#")) # -4
print(solution("1D2S3T*")) # 59
