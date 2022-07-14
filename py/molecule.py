#CLASS

class Molecule :
    def __init__(self, name="None", quant=0, disp=0, e=0):
        self.quant = quant
        self.e = e
        self.disp = disp
        self.name = name
