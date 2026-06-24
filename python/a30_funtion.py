def print_hello(a: int, value: str): 
    
    for _ in range(a):
        print(value)
    return "execution OK!"

def main():
    result = print_hello(3, "Hi")  # type hint
    print(result)


if __name__ == "__main__":
    main()
