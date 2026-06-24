import math


class MinusError(Exception):

    def __init__(self):

        message = "음수는 허용되지 않습니다."

        super().__init__(message)


def main():

    user_input = input("정수 입력: ")

    try:

        number_input = int(user_input)

        if number_input < 0:
            raise MinusError()

        print(f"원의 반지름: {number_input}")
        print(f"원의 둘레: {number_input * 2 * math.pi}")
        print(f"원의 넓이: {math.pi * number_input ** 2}")

    except MinusError as e:

        print("사용자 정의 예외 발생")
        print(e)

    except ValueError as e:

        print("정수를 입력해주세요.")
        print("에러:", e)

    finally:

        print("------ 프로그램이 종료되었습니다 -----")


if __name__ == "__main__":
    main()