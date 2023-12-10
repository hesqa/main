import math

z = [12, 25, 3, 48, 71]
x = [5, 18, 40, 62, 98]
c = [4, 21, 37, 56, 84]


def main(z, x, c):
    max_z = sorted(z)[-1]
    max_x = sorted(x)[-1]
    max_c = sorted(c)[-1]
    min_z = sorted(z)[0]
    min_x = sorted(x)[0]
    min_c = sorted(c)[0]
    max_p = (max_z + max_x + max_c) / 2
    max_s = math.sqrt((max_p * (max_p - max_z) * (max_p - max_x) * (max_p - max_c)))
    min_p = (min_z + min_x + min_c) / 2
    min_s = math.sqrt((min_p * (min_p - min_z) * (min_p - min_x) * (min_p - min_c)))
    print(f'Площадь треугольника из минимальных стророн {min_s}')
    print("Площадь треугольника из максимальных строн", max_s)


if __name__ == "__main__":
    main(z, x, c)
