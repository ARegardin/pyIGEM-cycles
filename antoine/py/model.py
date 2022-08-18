#!!! Early version of the model, there is only a function that is able to pull out data from a .json file formatted as cycles_data.json and structure it in an array.


#Hypothesis :
# All the cycles are working in the same compartment,
# uniform probability for disponibility,
# annex molecules(phosphates, water, ...) always infinitely disponible, 
# some homologic/isoformic proteins may be confused (e.g: Aldolase, ...),
# reactions for the PPP taken from the KEGG restricted Pentose Phosphate cycle (-> doesn't imply bDFructose16P2 for example),
# reversible enzyme-catalyzed reactions are (for now) treated as working exactly the same in the 2 directions, we followed the informations on reveribility given by KEGG,
# this is a step-by-step discrete model, the cinetic of all the reactions are presumed equivalent,

#!!! ->S.amb : Rpi=Rpi(B)? and others...

import json
import numpy as np
import scipy
import matplotlib.pyplot as plt
from collections import namedtuple

dict_path = "data/cycles_data.json"
mol_names = ["aDGlucose","aDGlucose6P","bDFructose6P","bDFructose16P2","bDGlucose","bDGlucose6P","DErythrose4P","DGluconate6P","DGlucono15Lactone6P","DHAP","DRibose5P","DRibulose5P","DRibulose15BisPhosphate","DSedoHeptulose7P","DSedoHeptulose17P2","DXylulose5P","G3P","Glycerate2P","Glycerate3P","Glycerate13P2","Phosphoenolpyruvate","Pyruvate"]
enz_names=[]

#Parameters of the model
global_thermo=1

global_mol_quantity = {
    "aDGlucose":0,
    "aDGlucose6P":0,
    "bDFructose6P":0,
    "bDFructose16P2":0,
    "bDGlucose":0,
    "bDGlucose6P":0,
    "DErythrose4P":0,
    "DGluconate6P":0,
    "DGlucono15Lactone6P":0,
    "DHAP":0,
    "DRibose5P":0,
    "DRibulose5P":0,
    "DRibulose15BisPhosphate":0,
    "DSedoHeptulose7P":0,
    "DSedoHeptulose17P2":0,
    "DXylulose5P":0,
    "G3P":0,
    "Glycerate2P":0,
    "Glycerate3P":0,
    "Glycerate13P2":0,
    "Phosphoenolpyruvate":0,
    "Pyruvate":0 #
}


def extract_molecule_json(dict_path, mol_name, reactenzyme=None, parameters=None, pos=False):
    r = [mol_name]
    with open(dict_path, 'r') as open_file:
        json_dict = json.load(open_file)
    molindex = mol_names.index(mol_name)

    if reactenzyme!=None:

        reacts = json_dict[molindex]["reactions"]
        ind_enz = []
        for k in range(len(reacts)):
            if reacts[k]["enzyme"]==reactenzyme:
                ind_enz.append(k)

        if parameters!=None:
            for i in ind_enz:
                s=[]
                for j in range(len(parameters)):
                    s.append(reacts[i][parameters[j]])
                r.append(s)

        else:
            for i in ind_enz:
                r.append(reacts[i])

    else:
        r.append(json_dict[molindex]["reactions"])

    if pos==True:
        r.append(json_dict[molindex]["position"]) 

    return r

#print(extract_molecule_json(dict_path, "aDGlucose", reactenzyme="Glucokinase", parameters=["coreactants", "type"]))

#
#def group_reactants(mol_names):
#
#
#
#
#def update_reactions(last_reacts, mol_quantity)
#    #We select the reactions that can happen in the next step
#    for i in range(len(last_reacts)):
#        for j in range

#def create_graph(vertices, edges):




#if __name__=="__main__":
    
