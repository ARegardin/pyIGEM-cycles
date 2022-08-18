#Loading the JSON files

import json
#data_path="Cours/iGem_model/data/"
#data_path="data/"


mol_names = ["aDGlucose","aDGlucose6P","bDFructose6P","bDFructose16P2","bDGlucose","bDGlucose6P","DErythrose4P","DGluconate6P","DGlucono15Lactone6P","DHAP","DRibose5P","DRibulose5P","DRibulose15BisPhosphate","DSedoHeptulose7P","DSedoHeptulose17P2","DXylulose5P","G3P","Glycerate2P","Glycerate3P","Glycerate13P2","Phosphoenolpyruvate","Pyruvate"]




# with open(data_path+"DHAP.json") as f:
#     d=json.load(f)
#     print(d["name"])
#     print(d["reactions"])



def create_lines(Name_):
    # Takes a .txt file formatted like the ones in /oldtxtdata, stores the separated lines in an array, cleans them (removing \r),
    # deletes all the lines that don't describe a reaction
    # -> Returns an array of strings containing all the descriptions of a molecule's reactions
    filein="data/oldtxtdata/"+Name_+".txt"
    reactions=[]
    with open(filein) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    delindex=[]
    for n in range(len(lines)):
        if len(lines[n])<30:
            delindex.append(n)
    delindex.reverse()
    for n in delindex:
        del lines[n]
    return lines


def store_lines(Name_):
    # Takes an array of reactions descriptions (the ones thatcreate_lines() returns)
    # And splits each of the reactions into an array describing its parameters
    # The function is also grouping the reactions of a molecule that are strictly the same, but present in more than 1 cycle
    # Returns an array of sub-arrays with the following structure:
    # [[reaction1],[reaction2], ..., [reaction n]]
    # with reaction i = [[coreactants i (="None" if no coreactants)], [products i], enzyme i, type i]
    test=[]
    reactions=[]
    lines=create_lines(Name_)
    print("lines",lines)
    for i in range(len(lines)):
        if "Coreactants" in lines[i]:
            coreact=True
        else:
            coreact=False
        line=lines[i].split(" ")
        for j in range(len(line)):
            line[j]=line[j].split("Coreactants:")[-1]
            line[j]=line[j].split("Products:")[-1]
            line[j]=line[j].split("Enzyme:")[-1]
            line[j]=line[j].split("Type:")[-1]
            line[j]=line[j].split(",")
            while isinstance(line[j],list)==True and len(line[j])==1:
                line[j]=line[j][0]

        test.append(lines[i].split(lines[i].split(" ")[0]+" "))
        print("test",test)

        if i==0:
            print("i==0",line)
            if coreact==True:
                print("coreact")
                ordering=[[line[0]],[line[1]],[line[2]],line[3],line[4]]
            else:
                ordering=[[line[0]],["None"],[line[1]],line[2],line[3]]
            reactions.append(ordering)

        else:
            repeat=0
            for j in range(i):
                print(i,j)
                if repeat==0:
                    if test[i]==test[j]:
                        repeat=1
                        reactions[j][0].append(line[0])
                    elif j==i-1:
                        if coreact==True:
                            ordering=[[line[0]],[line[1]],[line[2]],line[3],line[4]]
                            print("ordering cr",ordering)
                        else:
                            ordering=[[line[0]],["None"],[line[1]],line[2],line[3]]
                            print("ordering nc", ordering)
                        reactions.append(ordering)
        
    return reactions

print("return_test", store_lines("DGlucono15Lactone6P"))



def write_subdict(Name_):
    # Write a dictionnary containing all the informations about the reactions of a molecule
    # For the structure of the returned dict, see the "sub_dictionnary = " line.
    reactions = store_lines(Name_)
    sub_dictionary = {"name":Name_, "position":{"x":0,"y":0}, "reactions":[ {"cycles":reactions[i][0], "coreactants":reactions[i][1], "products":reactions[i][2], "enzyme":reactions[i][3], "type":reactions[i][4], "coefthermo":1} for i in range(len(reactions)) ] }
    #coefthermo: if the reaction is reversible: represents free gibbs energy parted in the 2 ways of reaction in function of the equilibrium constant
    #            if the reaction is nonreversible: represents the gibbs energy consumed by the enzyme for the 1-way reaction
    return sub_dictionary

#print(write_subdict("DHAP"))


def Mainwrite_dict(fileout, mol_names):
    # Writes all the sub-dictionnaries corresponding to every molecule in one .json file
    moldict=[]
    for i in range(len(mol_names)):
        moldict.append(write_subdict(mol_names[i]))
    outjson = open(fileout, "w")
    json.dump(moldict,outjson, indent=4)
    outjson.close()
    return 1


#Building the file:
###    print(Mainwrite_dict("data/cycles_data.json", mol_names))
