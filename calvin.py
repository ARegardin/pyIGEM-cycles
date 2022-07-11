from molecule import Molecule
from reaction import Reaction

import math

molecules = {
       "RuBP" : Molecule(0, 10, 0),
       "3PG" : Molecule(0, 10, 0),
       "BPG" : Molecule(0, 10, 0),
       "G3P" : Molecule(0, 10, 0),
        "R5P" : Molecule(0, 0, 0)
    }

reactions = {
        "RuBisCo" : Reaction("michaelis"),
        "Reaction1" : Reaction("michaelis"),
        "Reaction2" : Reaction("michaelis"),
        "Reaction3" : Reaction("michaelis"),
        "Reaction4" : Reaction("michaelis"),
    }

for key in reactions:
    reactions[key].speed_func = lambda x : math.sqrt(x)

reactions["RuBisCo"].add_reagent(molecules["RuBP"], 1)
reactions["RuBisCo"].add_product(molecules["3PG"], 1)

reactions["Reaction1"].add_reagent(molecules["3PG"], 1)
reactions["Reaction1"].add_product(molecules["BPG"], 1)

reactions["Reaction2"].add_reagent(molecules["BPG"], 1)
reactions["Reaction2"].add_product(molecules["G3P"], 1)

reactions["Reaction3"].add_reagent(molecules["G3P"], 1)
reactions["Reaction3"].add_product(molecules["R5P"], 1)

reactions["Reaction4"].add_reagent(molecules["R5P"], 1)
reactions["Reaction4"].add_product(molecules["RuBP"], 1)

for i in range(10):
    for key in reactions:
        reactions[key].react(1)

    print("Time : " + str(i))
    for key in molecules:
        print(key + " quantity : " + str(molecules[key].quant))
    print("--------------------")
