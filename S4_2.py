import random

def main():
    cub = random.randint(1, 6)
    print("Вы бросили кубик")
    print(f"Выпало: {cub}")
    if cub == 5 or cub == 6:
        print("Вы победили, везунчик!")
    elif cub == 3 or cub == 4:
        main()
    else:
        print("Не повезло..")

if __name__ == "__main__":
    main()