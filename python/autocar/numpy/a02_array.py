import numpy as np
import cv2
import os
from pathlib import Path


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
    print(arr.ndim)
    print(arr.shape)
    arr = np.arange(5)
    print(arr)
    arr = np.arange(5, 15, 2)
    print(arr)

    #zeros
    arr = np.zeros(5)
    print(arr)
    arr = np.zeros((2, 2, 2))
    print(arr)
    img_path = Path(__file__).with_name("car.jpg")
    img = cv2.imread(str(img_path)) if img_path.exists() else None
    if img is None:
        print(f"{img_path} 파일이 없어서 예제용 빈 이미지를 사용합니다.")
        img = np.zeros((100, 200, 3), dtype=np.uint8)
    img2 = np.zeros((100, 200))
    img3 = np.zeros_like(img)

    img4 = np.zeros(img.shape)
    print(type(img))

    #ones
    arr = np.ones(5)
    print(arr)
    arr = np.ones((2, 2))
    print(arr)
    img5 = np.ones_like(img)
    print(img5.shape)

    #full
    arr = np.full(5, 255)
    print(arr)
    arr = np.full((2, 2), 255)
    img6 = np.full_like(img, 255)
    if os.environ.get("SHOW_IMAGE") == "1":
        cv2.imshow("img6", img6)
        cv2.waitKey()

    #eye
    arr = np.eye(5)
    print(arr)

    #random
    arr1 = np.random.random((5,5))
    arr2 = arr1.dot(arr)
    print(arr)
    print(arr1)
    print(arr2)

if __name__ == "__main__":
    main()
