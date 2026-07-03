import os

os.environ.setdefault("QT_QPA_PLATFORM", "wayland")

import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(100, 110)
    data = np.random.random(10) * 100 + 30

    fig = plt.figure(figsize=(8, 6))

    ax1 = fig.add_subplot(2, 1, 1)
    ax1.bar(x, data, width=0.5)
    ax1.set_title("Bar Chart - width=0.5")
    ax1.set_xlabel("x")
    ax1.set_ylabel("value")

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.bar(x, data, width=0.5, align="edge")
    ax2.set_title("Bar Chart - align='edge'")
    ax2.set_xlabel("x")
    ax2.set_ylabel("value")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
