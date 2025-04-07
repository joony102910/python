def main():
    num = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 "))

    if num == 1:
        expr = input("*** 수식을 입력하세요: ")
        result1 = eval(expr)
        print(expr, "결과는", result1, "입니다")
        return
    if num == 2:
        num1 = int(input("***첫 번째 숫자를 입력하세요: "))
        num2 = int(input("***두 번째 숫자를 입력하세요: "))
        result2 = sum(range(num1, num2 + 1))
        print(num1, "+...+", num2, "는", result2, "입니다.")    
        return
    
    
    else:
        print("1이나 2를 입력해주세요")
        main()

main()