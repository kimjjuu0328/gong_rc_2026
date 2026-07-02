class A_test:
    def __repr__(self):
        return "A test 객체이다."


def main():
    print(12345)
    print(123, "kim", "joo", "hyung")
    print(3.12345)
    a = A_test()
    print(a)

    print("this is", "python", "class!!", sep="_", end="")
    print("this is", "python", "class!!", sep="-")


if __name__ == "__main__":
    main()
