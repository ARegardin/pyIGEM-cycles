import math

class Reaction:
    def __init__(self):
        self.reagents = []
        self.products = []
        self.type = "linear"
        self.constants = []
        
    def add_reagent(self, reagent, cst):
        self.reagents.append(reagent)
        self.constants.insert(0, cst)
        
    def add_product(self, product, cst):
        self.products.append(product)
        self.constants.append(cst)

    def react(self, dt):
        if self.type == "linear":
            self.react_linear(dt)

    def react_linear(self, dt):
        mod = math.floor(len(self.constants)/2)
        for i in range(len(self.reagents)):
            self.reagents[i].quant -= dt * self.constants[mod - 1 - i]
        for i in range(len(self.products)):
            self.products[i].quant += dt * self.constants[mod + i]
