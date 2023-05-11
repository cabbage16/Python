while True:
    dlqfur = int(input('입력할 진법(2,8,10,16진법만가능):'))
    if not(dlqfur >= 2 and dlqfur <= 36 or dlqfur != 0):
        print("잘못된 입력,또는 출력입니다.")
    cnffur = int(input('출력할진법(2,8,10,16진법만가능):'))
    if not(cnffur >=2 and cnffur <= 36 or cnffur != 0):
        print("잘못된 입력,또는 출력입니다.")
    n = int(input('수 입력:'),dlqfur)
    if(cnffur == 2):
        print(bin(n))
    elif(cnffur == 8):
        print(oct(n))
    elif(cnffur == 10):
        print(n)
    else:
        print(hex(n))