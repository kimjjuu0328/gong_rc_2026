import random


def sum_all(a, b, c, *value):
    total = a + b + c

    for i in value:
        total += i

    average = total / (len(value) + 3)
    return total, average


def main():
    list_a = [random.randint(0, 100) for _ in range(100)]
    s, a = sum_all(*list_a)
    print(f"합계는 {s}, 평균은 {a}")


if __name__ == "__main__":
    main()
