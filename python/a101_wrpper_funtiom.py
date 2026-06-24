def simple_wrapper(func):

    def wrapper():
        print("func 실행 전 코드..")

        func()

        print("func 실행 후 코드..")

    return wrapper


@simple_wrapper
def print_hello():
    print("print_hello 함수가 실행됨")


def main():
    print_hello()


if __name__ == "__main__":
    main()