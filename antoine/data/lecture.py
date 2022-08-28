import json
import numpy as np



#fonction which create a txt file from a list of dictionary 
def write_txt(d,i):
    #create and open a file.txt for the molecule of interest
    new_file=open(f"{d[i]['name']}.txt",'a+')
    #boucle pour toutes les clés ('name','position','reaction')
    for k1 in d[i].keys():


        #'position'
        if type(d[i][k1])== dict:
            new_file.write(k1.upper())
            new_file.write('\n')
            for k2 in d[i][k1].keys():             
                new_file.write(' ')
                new_file.write(str(d[i][k1][k2]))


        #'reaction'
        elif type(d[i][k1])==list :
            new_file.write(k1.upper())
            # on regarde chaque élément de la liste indépendamment
            for ind1 in np.arange(0,len(d[i][k1])):
                # examine toutes les clés 'cycles','coreactants','products,'enzymes','type','coefthermo'
                for k3 in d[i][k1][ind1].keys():
        
                    new_file.write('\n')
                    new_file.write(k3)                  
                    new_file.write(':')
                    new_file.write('\n')
                    # the format for the key's value are not the same so we need to check before normalize it 
                    if type(d[i][k1][ind1][k3]) ==list :
                        #check how many values are contain in the key
                        for ind2 in np.arange(0,len(d[i][k1][ind1][k3])) :
                            if type(d[i][k1][ind1][k3][0]) == list :
                                for ind3 in np.arange(len(d[i][k1][ind1][k3][ind2])):
                                    new_file.write(('').join(d[i][k1][ind1][k3][ind2][ind3]))
                                    new_file.write(' ') 
                                
                            else:
                                new_file.write((''.join(d[i][k1][ind1][k3][ind2])))
                                new_file.write(' ')
                    else :
                        new_file.write(str(d[i][k1][ind1][k3]))
                new_file.write('\n'*2)


                
        #'name'
        else :
            new_file.write(k1.upper())
            new_file.write('\n')   
            new_file.write(d[i][k1])

        new_file.write('\n'*2)
        
    new_file.close()

# convert all the data from a json file to txt files 
def boucle_txt(js):
    
    with open(js) as cycles_data:
        data =json.load(cycles_data)
    
    i=0
    while i< len(data):

        write_txt(data,i)
        i+=1

boucle_txt('cycles_data.json')      
    

    