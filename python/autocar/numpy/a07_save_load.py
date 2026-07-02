from pathlib import Path

import numpy as np


def main():
    BASE = Path(__file__).parent
    s1 = np.random.randint(0, 10, 10, dtype=np.int8).reshape(2, -1)
    print(s1)
    np.save(BASE / "test.npy", s1)

if __name__ == "__main__":
    main()
    
