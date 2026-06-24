from functools import wraps

def simple_wrapper(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("func 실행 전 코드..")

        result = func(*args, **kwargs)

        print("func 실행 후 코드..")

        return result

    return wrapper


@simple_wrapper
def print_hello(n, v):

    print("n =", n)
    print("v =", v)
    print("print_hello 함수가 실행됨")


def main():

    print_hello(10, 20)


if __name__ == "__main__":
    main()