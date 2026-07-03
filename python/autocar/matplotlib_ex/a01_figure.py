import numpy as np
import os

os.environ.setdefault("QT_QPA_PLATFORM", "wayland")

import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt


def main():
    data = np.random.random(10)
    plt.plot(data)
    plt.show()
    


if __name__ == "__main__":
    main()
