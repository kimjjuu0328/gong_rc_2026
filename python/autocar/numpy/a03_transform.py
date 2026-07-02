import numpy as np

def main():
    arr = np.arange(100)
    print(arr)

    reshp = arr.reshape((2, 5, 5, 2))
    print(reshp, reshp.shape)

    print(reshp[1][3][3][1])
    print(reshp[1, 3, 3, 1])
    print(reshp[1, :, 2:4, 1], reshp[1, :, 2:4, 1].shape)

    fl = reshp.flatten()
    print(fl)
    print(fl.shape)


if __name__ == "__main__":
    main()