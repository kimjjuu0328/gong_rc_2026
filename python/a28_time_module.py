import time


def main():
    print(time.asctime())
    print(time.time())
    print(time.clock_gettime_ns(time.CLOCK_MONOTONIC))

    ptime = time.time()  # previous time
    cnt = int()
    while time.time() < ptime + 5:
        cnt += 1
    print(f"이 컴퓨터는 5초 동안 {cnt:,d} 카운트가 진행 되었다")


if __name__ == "__main__":
    main()
