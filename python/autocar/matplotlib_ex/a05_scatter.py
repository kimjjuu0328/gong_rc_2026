import os

os.environ.setdefault("QT_QPA_PLATFORM", "wayland")

import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    data1 = np.random.random(1000).reshape(2, 500) * 2 + 0.5
    data2 = np.random.random(1000).reshape(2, 500) * 2
    data3 = np.random.random(1000).reshape(2, 500) * 2 - 0.5

    plt.scatter(data1[0], data1[1], s=10, label="data1")
    plt.scatter(data2[0], data2[1], s=10, label="data2")
    plt.scatter(data3[0], data3[1], s=10, label="data3")
    plt.title("Scatter Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
