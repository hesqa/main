def uppercase_decorator(func):
    def wrapper(text):
        upper_text = text.upper() # Преобразуем текст в верхний регистр.
        return func(upper_text) # Вызываем оригинальную функцию с преобразованным текстом.
    return wrapper

@uppercase_decorator # Функция, которая будет использовать декоратор.
def print_message(text):
    print(text)

@uppercase_decorator
def get_length(text):
    length = len(text)
    print(f"Длина текста: {length}")

print_message("zxcvbnm12345!") # Вызываем функции
get_length("zxcvbnm12345!")