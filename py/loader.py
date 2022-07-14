from molecule import Molecule
from reaction import Reaction

import os

# - Creates an array of all the files of a directory
def get_files_from_dir(path):
    arr = []
    for f in os.listdir(path):
        arr.append(f)
    return arr

# - Opens a file, returns an array of the content
def open_file(path):
    f = open(path, "r")
    content = f.read()

    raw = content.split("\n")
    clean = []

    for line in raw:
        if len(line) > 0:
            if line[0] != "#":
                clean.append(line)
    return clean

# - Builds a model from a directory
def build_model_dir(path, molecules, reactions):
    files = get_files_from_dir(path)
    
    # First we create each molecule
    # each file is a molecule
    for molfile in files:
        lines = open_file(path + "/" + molfile)
        a = Molecule()

        for i in range(len(lines)):
            if lines[i] == "NAME":
                a.name = lines[i + 1]

        molecules[a.name] = a

    # Then each reaction
    for molfile in files:
        lines = open_file(path + "/" + molfile)
        current_molname = "None"
        reading_products = False
        for i in range(len(lines)):
            if not reading_products:
                if lines[i] == "NAME":
                    current_molname = lines[i + 1]
                if lines[i] == "PRODUCTS":
                    reading_products = True
            else:
                reaction_raw = lines[i].split()
                b = Reaction()
                b.add_reagent(molecules[current_molname], 1)
                b.add_product(molecules[reaction_raw[0]], 1)

                reactions[len(reactions)] = b
