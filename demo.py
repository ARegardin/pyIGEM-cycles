from molecule import Molecule
from reaction import Reaction

mol1 = Molecule(0, 0, 0)
mol2 = Molecule(0, 10, 0)

react1 = Reaction()
react1.add_reagent(mol2, 1)
react1.add_product(mol1, 1)

react1.react(1)

print(mol1.quant)
print(mol2.quant)
