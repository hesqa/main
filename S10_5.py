class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def divide_numbers(a, b): # Функция, которая может вызвать исключение.
    if b == 0:
        raise CustomException("Делить на ноль нельзя!")
    else:
        return a / b

try: # Фрагмент кода, который обрабатывает исключение.
    result = divide_numbers(30, 3)
    print("Результат деления:", result)
except CustomException as e:
    print("Исключение:", e.message)

try:
    result = divide_numbers(5, 0)
    print("Результат деления:", result)
except CustomException as e:
    print("Исключение:", e.message)