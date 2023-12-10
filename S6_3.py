def count_repeated_digits(input_string):
    dig_count = {}

    for dig in input_string:
        dig = int(dig)
        dig_count[dig] = dig_count.get(dig, 0) + 1

    sorted_digits = sorted(dig_count.items(), key=lambda x: x[1], reverse=True)

    res = {}
    for dig, count in sorted_digits[:3]:
        res[dig] = count

    return res


input_string = "546723487920134"
res_dict = count_repeated_digits(input_string)

print("Словарь из трех самых часто встречаемых чисел:", res_dict)