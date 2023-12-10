def avergens(*args):
    if not args:
        return 0
    z =sum(args)
    x = len(args)
    c = z/ x
    return c

if __name__ == "__main__":
    result = avergens(2, 4, 5, 7, 1, 5, 8)
    print(f"Среднее арифметическое: {result}")