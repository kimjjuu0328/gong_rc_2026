import os

os.environ.setdefault("QT_QPA_PLATFORM", "wayland")

import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(100, 110)
    data1 = np.random.random(10) * 100 + 30
    data2 = np.random.random(10) * 100 + 30

    fig = plt.figure(figsize=(10, 4))
    fig.suptitle("Two Bar Charts - Horizontal Layout")

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.barh(x, data1, height=0.5, color="skyblue")
    ax1.set_title("First Horizontal Bar Chart")
    ax1.set_xlabel("value")
    ax1.set_ylabel("x")

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.barh(x, data2, height=0.5, color="orange")
    ax2.set_title("Second Horizontal Bar Chart")
    ax2.set_xlabel("value")
    ax2.set_ylabel("x")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
