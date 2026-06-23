import datetime


def main():

    list_a = []
    list_b = list()

    print(type(list_a))
    print(type(list_b))

    ptime = datetime.datetime.now()

    list_c = [1, 2, 3.3, "choi", ptime, True]

    print(list_c[3])
    print(list_c[-1])

    list_c[0] = "kim"

    print(list_c)

    list_d = [[1, 2, 3], [4, 5, 6],[7 ,8, 9]]
    print(list_d[1][2]) # 6
    print(list_d[0][1]) # 2

    #print(list_d[3])
    #갯수 확인 len > 내부 메소드 len을 호출 하는 함수
    print(len(list_d))
    print(list_d.__len__()) # 내부 메소드 호출

if __name__ == "__main__":
    main()