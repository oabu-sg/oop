
class Calculator:
    pi = 3.14

    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2
        self.sum = None

    def add(self):
        self.sum = self.number1 + self.number2

    def print_sum(self):
        print(f"{self.number1} + {self.number2} = {self.sum}")

    def divide(self):
        if self.number2 != 0:
            division = self.number1 / self.number2
            print(f"{self.number1} / {self.number2} = {division}")
            return division
        return None

    def update_number2(self, new_num2):
        if new_num2 != 0:
            self.number2 = new_num2

    def print_numbers(self):
        print(f"**** self.number1 = {self.number1}")
        print(f"**** self.number2 = {self.number2}")

    def run_all(self):
        self.add()
        self.divide()

if __name__ == "__main__":
    calc_object = Calculator(15, 30)
    print(calc_object)

    calc_object2 = Calculator(210, 400)
    print(calc_object2)


    calc_object3 = Calculator(100, 5)
    print(calc_object3)

    calc_object_new = calc_object
    print(calc_object_new)
    '''
    calc_object.add()
    calc_object.update_number2(100)
    calc_object.print_sum()
    calc_object.add()
    calc_object.print_sum()

    calc_object2 = Calculator(210, 400)
    calc_object2.print_sum()
    calc_object2.add()
    calc_object2.print_sum()

    calc_object.print_numbers()
    calc_object.add()
    calc_object.divide()
    calc_object.run_all()

    
    calc_object.update_number2(50)
    #calc_object.number2 = 0
    calc_object.add()
    calc_object.divide()
    calc_object.run_all()


    calc_object2 = Calculator(210, 400)

    calc_object2.print_numbers()
    calc_object2.add()
    calc_object2.run_all()

    '''

