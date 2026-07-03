# pip install matplotlib
import os

os.environ.setdefault("QT_QPA_PLATFORM", "wayland")

import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    data1 = np.random.random(10)
    data2 = np.random.random(30).reshape(10, 3)

    fig = plt.figure(figsize=(8, 6))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(data1)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(data2)

    plt.show()


if __name__ == "__main__":
    main()
