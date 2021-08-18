def math(e):
    """
    code here
    """


while True:
    order = input("수식입력(1), 프로그램 종료(2) :")
    if order == "1":
        ex = input("수식을 입력하세요 :")
        print(math(ex))
    else:
        break
