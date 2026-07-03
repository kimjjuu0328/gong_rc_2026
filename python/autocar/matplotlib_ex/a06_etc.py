import os

os.environ.setdefault("QT_QPA_PLATFORM", "wayland")

import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = np.random.random(10)
    x = np.arange(len(data))

    fig = plt.figure(figsize=(8, 6))

    ax = fig.add_subplot(2, 3, 1)
    ax.hist(data)
    ax.set_title("hist")

    ax = fig.add_subplot(2, 3, 2)
    ax.pie(data)
    ax.set_title("pie")

    ax = fig.add_subplot(2, 3, 3)
    ax.step(x, data)
    ax.set_title("step")

    ax = fig.add_subplot(2, 3, 4)
    ax.boxplot(data)
    ax.set_title("boxplot")

    ax = fig.add_subplot(2, 3, 5)
    ax.fill_between(x, data)
    ax.set_title("fill_between")

    ax = fig.add_subplot(2, 3, 6)
    X, Y = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))

    Z = np.sin(X) + np.cos(Y)
    ax.contour(X, Y, Z)
    ax.set_title("contour")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
