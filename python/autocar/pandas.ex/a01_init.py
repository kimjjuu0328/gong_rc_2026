# pip install pandas

import numpy as np
import pandas as pd


def main():
    arr = np.array([10, 20, 30], dtype=np.int8)
    sr = pd.Series(arr)
    print(sr, type(sr))
    sr[1] = 40
    print(sr[1])

    value = [32, 68, 220, 72]
    index = ["온도", "습도", "강수량", "불쾌지수"]
    sr2 = pd.Series(value, index=index, dtype=np.int16)
    print(sr2, type(sr2))
    print(sr2["온도"], sr2.iloc[0])

if __name__ == "__main__":
    main()
