def main():
    tu = tuple()
    print(tu, type(tu))
    tu = ( 1, 2) #원소 추가 제가 변경이 안된다.
    print(tu, type(tu))
    print(tu[0])
    for ele in tu:
        print(ele)  #list 하고 같은 기능을 가진 컨테이너
    # system 내부적으로 안전적 으로 데이터를 전달하기 위해
    tu_1 = 1,2  
    print(tu_1, type(tu_1))
    a = 10
    b = 20
    # swap C 스타일 
    tmp = a
    a = b
    b = ( a,b)
    # swap python 스타일  #소괄호가 생략 될 수 있다.

if __name__ == "__main__":
    main()