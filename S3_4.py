pr = input("Введите предложение на английском: ")
print("Длина предложения: ", len(pr))
lowercase_pr = pr.lower()
print("Предложение в нижнем регистре: ", lowercase_pr)
vowels = "aeiou"
vowel_count = sum(1 for char in lowercase_pr if char in vowels)
print("Количество гласных: ", vowel_count)
replaced_predlozh = lowercase_pr.replace("ugly", "beauty")
print("Предложение с заменой 'ugly' на 'beauty': ", replaced_predlozh)
starts_with_the = lowercase_pr.startswith("the")
ends_with_end = lowercase_pr.endswith("end")

if starts_with_the:
    print("Предложение начинается с 'The'")
else:
    print("Предложение не начинается с 'The'")
if ends_with_end:
    print("Предложение заканчивается на 'end'")
else:
    print("Предложение не заканчивается на 'end'")