import math

class Solution:
    def solution(self, fees, records):
        answer = []
        # fees 설명
        # 기본 시간, 기본 요금, 몇 분당?, 추가요금
        basic_time, basic_fee, per_min, plus_fee = fees

        # 차량 번호를 키로 사용하여 누적 주차 시간을 저장할 딕셔너리 초기화
        car = {}
        for idx in records:
            idx = idx.split()
            car[idx[1]] = 0 # 모든 차량의 누적 주차 시간을 0으로 초기화

        # 차량의 입차 시간을 기록하기 위한 딕셔너리 초기화
        dic = {}
        for idx in records:
            idx = idx.split()
            temp = idx[0].split(':') # 시:분 형태의 시간을 ':' 기준으로 분리
            in_time = int(temp[0]) * 60 + int(temp[1]) # 시간을 분 단위로 변환

            if idx[2] == 'IN': # 차량이 입차할 때
                dic[idx[1]] = in_time # 입차 시간을 기록

            elif idx[2] == 'OUT': # 차량이 출차할 때
                if idx[1] in dic.keys(): # 입차 기록이 있는 경우
                    car[idx[1]] += in_time - dic[idx[1]] # 누적 주차 시간 계산
                    dic[idx[1]] = -1 # 출차 처리 완료를 표시
        # 출차 기록이 없는 차량의 주차 시간 계산 (23:59 출차로 간주)
        for key, value in dic.items():
            if value != -1: # 입차는 했지만 출차 기록이 없는 경우
                car[key] = car[key] + (1439 - dic[key]) # 23:59(1439분) 기준으로 계산

        # 각 차량에 대해 요금 계산
        for key, value in car.items():
            if value <= basic_time: # 누적 시간이 기본 시간 이하인 경우
                answer.append((int(key), basic_fee)) # 기본 요금만 부과
            elif value > basic_time: # 누적 시간이 기본 시간을 초과한 경우
                tot_fee = basic_fee + math.ceil((value - basic_time) / per_min) * plus_fee # 추가 요금 계산
                answer.append((int(key), tot_fee))

        # 차량 번호를 기준으로 오름 차순 정렬
        answer.sort(key=lambda x: x[0])

        # 최종 요금만 추출하여 반환할 리스트 생성
        real_answer = []
        for key, money in answer:
            real_answer.append(money)

        return real_answer


