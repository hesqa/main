z = [
    10.2, 14.8, 19.3, 22.7, 12.5,
    33.1, 38.9, 21.6, 26.4, 17.1,
    30.2, 35.7, 16.9, 27.8, 24.5,
    16.3, 18.7, 31.9, 12.9, 37.4
    ]

from collections import Counter

def mos(z):
    for i in z:
            if str(i).startswith("10"):
                return i

if __name__ == "__main__":
    print("Три лучших результата: ", sorted(z)[0:3])
    print("Три худших результата: ", sorted(z)[-4:-1])
    print("Все результатаы начиная с 10: ", mos(z))