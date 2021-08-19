"""
지금 시각을 UTC+0(세계 표준시)을 기준으로 나타냈을 때의 
서울의 연도, 월, 일을 한 줄에 하나씩 순서대로 출력한다.
"""

from datetime import datetime, timedelta

date = datetime.now() + timedelta(hours=9)
print(date.year)
print(date.month)
print(date.day)
