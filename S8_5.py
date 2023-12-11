class j:
    def drink(self):
        return "It's pretty tasty!"

class w:
    def drink(self):
        return "The taste is much worse than the juice"

def drink_drinks(drink):
        return drink.drink()

dr_j = j()
dr_w = w()

print(drink_drinks(dr_j))
print(drink_drinks(dr_w))