#Model for metabolism

import numpy as np
import matplotlib.pyplot as plt

#CLASS


#DATA


#connecting the nodes
def react(A,B,E):
    if E>=A.e and A.stoe*A.quant>=1:
        B.quant += A.quant*A.stoe
        E = E+A.e*A.quant
        ret = 'react'
        
    else :
        ret = 0

    return ret

    

