import random
class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength

    def __str__(self):
        return self.brand + " " + self.model +" (" +str(self.strength*100) +" / 100 strength)"

    def does_break(self):
        if random.random() < 0.5*self.strength:
            return True
        else:
            return False
def main():
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    print(fender_vi.model)
    print(fender_vi.brand)
    print(fender_vi.strength)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    print(fender_vi)
    print(four_double_o_one)
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    number_of_tests = 100
    number_of_breaks = 0
    # I'm testing does_break() 100 times and keeping track of how many times it breaks
    for i in range(number_of_tests):
        if danelectro.does_break():
            number_of_breaks += 1
    percentage = (number_of_breaks / number_of_tests) * 100
    print(f"The {danelectro.model} broke {round(percentage)}% of the time in {number_of_tests} tests!")
main()