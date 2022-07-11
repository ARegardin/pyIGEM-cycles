from molecule import Molecule
from reaction import Reaction

import math

mol1 = Molecule(0, 0, 0)
mol2 = Molecule(0, 10, 0)

react1 = Reaction("michaelis")
react1.speed_func = lambda x : math.sqrt(x)
react1.add_reagent(mol2, 1)
react1.add_product(mol1, 9)

react1.react(10)

print(mol1.quant)
print(mol2.quant)
