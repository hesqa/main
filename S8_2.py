class phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def use(self):
        print(f"I'm currently using an {self.model} by {self.brand} that I bought for {self.price}")

my_phone = phone("Xiaomi", "11T Pro", "30000")
my_phone.use()

