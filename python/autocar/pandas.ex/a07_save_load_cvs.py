from pathlib import Path

import numpy as np
import pandas as pd


def main():
    value = [[32, 68, 220, 72], [28, 30, 0, 12], [38, 81, 0, 91]]
    columns = ["온도", "습도", "강수량", "불쾌지수"]
    index = ["초여름", "늦봄", "한여름"]
    df = pd.DataFrame(value, index=index, columns=columns, dtype=np.uint8)

    csv_path = Path(__file__).with_name("weather.csv")

    df.to_csv(csv_path, encoding="utf-8-sig")
    print("CSV 저장 완료")
    print(csv_path)

    loaded_df = pd.read_csv(csv_path, index_col=0)
    print(loaded_df)


if __name__ == "__main__":
    main()
