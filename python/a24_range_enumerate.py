def main():

    print(range(10))
    print(range(0, 10, 1))

    a = range(10)

    print(list(a))

    print(list(range(5, 10, 3)))

    a = list(range(10))

    for i in range(0, 100, 2):
        a.append(i + 1)
        print(a)
        #list comparehension
    a = [i + 1 for i in range(100)]
    print(a)

    list_b = ["a", "b", "c", "d", "e", "f"]
    for index, value in enumerate(list_b):
        print(index, "원소:", value)
    list_c = ["에이", "비", "씨", "디", "이", "에프"]
    for i in range(6):
        print(list_b[i], list_c[i])
    for b,c in zip(list_b, list_c):
        print(b,c)    


if __name__ == "__main__":
    main()
    