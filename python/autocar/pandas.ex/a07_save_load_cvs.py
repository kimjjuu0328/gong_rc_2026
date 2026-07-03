

import numpy as np
import pandas as pd
import seaborn as sns


def main():
    BASE = Path(__file__).parent
    df = pd.read_cvs(BASE / "weather.cvs", index_col=0,)
    print(df)
    df = sns.load_dataset("titanic")
    df.to_cvs(BASE / "titanic.cvs")

if __name__ == "__main__":
    main()  