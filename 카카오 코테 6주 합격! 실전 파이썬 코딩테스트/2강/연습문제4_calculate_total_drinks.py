def calculate_total_drinks(cups):
  # TODO
  total_drinks = 0

  # 교환 가능한 컵의 수가 4개 이상일 때까지 반복
  while cups >= 4:
      # 받을 수 있는 음료의 수
      drinks = cups // 4
      # 총 음료 개수 누적
      total_drinks += drinks
      # 남은 컵 + 새로 생긴 컵
      cups = (cups % 4) + drinks

  return total_drinks

# 테스트 케이스
print(calculate_total_drinks(6))  # 출력 예시: 1
print(calculate_total_drinks(13)) # 출력 예시: 4
print(calculate_total_drinks(25)) # 출력 예시: 8
print(calculate_total_drinks(50)) # 출력 예시: 16

