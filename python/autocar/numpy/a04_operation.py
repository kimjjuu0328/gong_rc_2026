import numpy as np


def main():
    x = np.arange(40).reshape(8, 5)
    print(x)

    y = np.arange(39, -1, -1).reshape(8, 5)
    print(y)

    # linspace: 내부 원소의 개수를 지정
    z = np.linspace(30, 100, 40).reshape(8, 5)
    print(z)

    s1 = x + y
    print(s1)

    s2 = x - z
    print(s2)

    s3 = x / z
    print(s3)

    # Broadcasting
    x = x + 5
    print(x)

    x = np.array([1, 2, 3, 4, 5])
    print(x)

    # matmul
    s5 = np.matmul(x, y.T)
    print(s5)

    s6 = x.dot(y.T)
    print(s6)

    # 역행렬
    A = np.array([
        [1, 2],
        [3, 4]
    ])

    inv_A = np.linalg.inv(A)
    print(A)
    print(inv_A)
    print(A @ inv_A)

    # 연립방정식 풀이
    # 1x + 4y + 5z = 10
    # 2x + 3y + 8z = 20
    # -3x + 2y + 5z = -50

    A = np.array([
        [1, 4, 5],
        [2, 3, 8],
        [-3, 2, 5]
    ])

    b = np.array([10, 20, -50])

    # 방법 1
    result = np.linalg.solve(A, b)

    # 방법 2 (역행렬 이용)
    # a_inv = np.linalg.inv(A)
    # result = a_inv @ b

    x, y, z = result

    print(f"x:{x}, y:{y}, z:{z}")


if __name__ == "__main__":
    main()