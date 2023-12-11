class phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def use(self):
        print(f"I'm currently using an {self.model} by {self.brand} that I bought for {self.price}")

class BCphone(phone):
    def __init__(self, brand, model, price, term_of_use):
        super().__init__(brand, model, price)
        self.term_of_use = term_of_use

    def sell(self):
        print(f"I am selling my {self.model} from {self.brand}, which i have been using for {self.term_of_use} for {self.price}")

my_phone = BCphone("Xiaomi", "11T Pro", "30000", "5 years")
my_phone.use()
my_phone.sell()

