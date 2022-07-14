from molecule import Molecule
from reaction import Reaction
import loader
import math

molecules = {}
reactions = {}

loader.build_model_dir("../data", molecules, reactions)

for i in range(10):
    for key in reactions:
        reactions[key].react(1)

    print("Time : " + str(i))
    for key in molecules:
        print(key + " quantity : " + str(molecules[key].quant))
    print("--------------------")
