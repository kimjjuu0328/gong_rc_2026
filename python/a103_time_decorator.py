from functools import wraps
import time


def check_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(
            f"실행 시간: {end_time - start_time:.6f}초"
        )

        return result

    return wrapper


@check_time
def test():

    total = 0

    for i in range(100000000):
        total += i

    print("계산 완료")


def main():

    test()


if __name__ == "__main__":
    main()