def print_n_times(n, *args, abc="abc", defg="defg", **keyargs):
    # positional, default, variable-length, keyword, variable-length-keyword
    for _ in range(n):
        print(args)
        print(abc, defg)
        print(type(keyargs), keyargs)
        for k, v in keyargs.items():
            print(k, v)


def general_f(*args, **kwargs):
    print(args)
    print(kwargs)


def main():
    print_n_times(3, "choi", "su", "gil", "is", "teacher!")
    print_n_times(3, "test", defg="마지막 문자", abc="첫 문자", a=1, b="sdf", df="sdf")
    general_f(1, 2, 4, k="234")


if __name__ == "__main__":
    main()    
