
def maximumUnits(boxTypes, truckSize):
    # 유닛으로 내림차순 정렬하기
    boxTypes.sort(key= lambda x : x[1], reverse=True)
    cnt = 0
    ans = 0
    for box, unit in boxTypes:
        # 박스와 유닛을 곱하기 전에 갯수 확인
        cnt += box
        if cnt > truckSize:
            # 박스를 실은 갯수가 초과했을 때, 남은 공간만큼 유닛 계산하여 싣기
            ans += (truckSize - (cnt - box)) * unit
            break
        ans += box * unit

    return ans





