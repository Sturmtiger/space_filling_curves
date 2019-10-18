import turtle


class LSystem:
    def __init__(self, curve_type, order_number):
        self.order_number = order_number
        self.variables = curve_type.__dict__['VARIABLES']
        self.constants = curve_type.__dict__['CONSTANTS']
        self.theta = curve_type.__dict__['THETA']
        self.production_rules = curve_type.__dict__['PRODUCTION_RULES']
        self.axiom = curve_type.__dict__['AXIOM']

    def run(self):
        for char in self.__prepare():
            if char == 'F':
                turtle.forward(10)
            elif char == '+':
                turtle.left(self.theta)
            elif char == '-':
                turtle.right(self.theta)

        turtle.done()

    def __prepare(self):    # prepare order string to perform by turtle module
        order_set = self.axiom
        for _ in range(self.order_number):
            order = str()
            for char in order_set:
                if char in self.variables:
                    order += self.production_rules[char]
                else:   # if char is constant
                    order += char   # constant
            order_set = order
        return order_set
