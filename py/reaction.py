import math

class Reaction:
    def __init__(self, t = "linear"):
        self.reagents = []
        self.products = []
        self.type = t

        self.constants = []
        self.speed_func = lambda x : x
        
    def add_reagent(self, reagent, cst):
        self.reagents.append(reagent)
        self.constants.insert(0, cst)
        
    def add_product(self, product, cst):
        self.products.append(product)
        self.constants.append(cst)

    def react(self, dt, step = 1):
        for i in range(0, dt, step):

            if self.type == "linear":
                self.react_linear(step)

            if self.type == "michaelis":
                self.react_michaelis(step)
            
            # Check if reagent are at zero or negative quantity
            reagent_at_zero = False
            for j in range(len(self.reagents)):
                if self.reagents[j].quant <= 0:
                    reagent_at_zero = True
                    self.reagents[j].quant = 0
            if reagent_at_zero:
                break

    def react_linear(self, dt):
        mod = math.floor(len(self.constants)/2)
        for i in range(len(self.reagents)):
            self.reagents[i].quant -= dt * self.constants[mod - 1 - i]
        for i in range(len(self.products)):
            self.products[i].quant += dt * self.constants[mod + i]

    def react_michaelis(self, dt):
        mod = math.floor(len(self.constants)/2)
        speed = abs(self.speed_func(self.reagents[0].quant))
        
        for i in range(len(self.reagents)):
            self.reagents[i].quant -= speed * dt * self.constants[mod - 1 - i]
        for i in range(len(self.products)):
            self.products[i].quant += speed * dt * self.constants[mod + i]
        
        for i in range(len(self.reagents)):
            if self.reagents[i].quant < 0:
                for j in range(len(self.products)):
                    self.products[j].quant += self.reagents[i].quant * self.constants[mod + i] / self.constants[mod - 1 - j]
                self.reagents[i].quant = 0

