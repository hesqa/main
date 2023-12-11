class phone:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self.__price = price

    def use(self):
        print(f"I'm currently using an {self._model} by {self._brand} that I bought for {self.__price}")

my_phone = phone("Xiaomi", "11T Pro", "30000")
print(my_phone._brand)
my_phone.use()