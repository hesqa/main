ui = input("Введите последовательность чисел, разделенных пробелом: ")

numbers_list = ui.split()
numbers_list = [int(num) for num in numbers_list]

numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)