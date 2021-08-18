# 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.

from datetime import datetime

print(datetime.today().strftime("%Y-%m-%d"))
