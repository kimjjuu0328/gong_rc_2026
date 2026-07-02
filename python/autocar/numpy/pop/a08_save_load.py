from pathlib import Path

import numpy as np


def main():
    BASE = Path(__file__).parent.parent
    image = np.load(BASE / "sample_image.npy")

    print(image)
    print("shape:", image.shape)
    print("dtype:", image.dtype)
    print("left top pixel:", image[0, 0])

if __name__ == "__main__":
    main()
    
