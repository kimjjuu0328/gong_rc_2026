class add_test:
    def __add__(self, other):
        return "더하기 연산이 실행 되었다"
    

def main():
    print(2 ** 4) #2의 4제곱 입니다.
    print(2 ** 64) #2의 64제곱 입니다.
    print(18 //4) #18을 4로 나눈 몫입니다.

    
    print(18 // 3) #18을 3으로 나눈 몫입니다.
    print(type(18 // 3)) #18을 3으로 나눈 몫의 타입입니다.

    print(14 % 3) #14를 3으로 나눈 나머지입니다.
    a = add_test()
    b = add_test()
    print(a+b) 
    print( a + 123)
    print( a + 3.14)
    print("abcd" * 5)
    a = 5
    a += 1
    print(a++)

if __name__ == "__main__":
    main()
