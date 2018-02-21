# /usr/bin/python

import numpy as np
import sys
from numpy import linalg as LA

def graded_zero_vector(lenght):
	zeroVec = np.zeros((lenght,1))
	return(zeroVec)
	
print('Shape:', graded_zero_vector(50).shape)
print('Shape:', graded_zero_vector(123).shape)

def graded_vec_i(lenght):
	vec = np.linspace(0,lenght-1,num=lenght,dtype=int)
	return vec

print('Sum:', sum(graded_vec_i(10)))
print('Vector:', graded_vec_i(10))

def graded_generate_pauli():
    pauliX = np.matrix([[0, 1], [1, 0]])
    pauliY = np.matrix([[0, -1j], [1j, 0]])
    pauliZ = np.matrix([[1, 0], [0, -1]]) 
    return(pauliX, pauliY, pauliZ)

print('Pauli X:', graded_generate_pauli()[0])

def graded_pauli_check(coordinate): # coordinate can be 'X', 'Y' or 'Z'    
    coord_index_map = {'X':0, 'Y':1, 'Z':2}
    pauli_index = coord_index_map[coordinate]
    ### Start code here
    
    #retreive the corresponding Pauli matrix (use the function above)
    pauliMatrix = graded_generate_pauli()[0]
    
    # calculate its determinant
    det = pauliMatrix[0,0]*pauliMatrix[1,1]-pauliMatrix[0,1]*pauliMatrix[1,0]

    # calculate its square
    square = LA.matrix_power(pauliMatrix,2)

    # calculate its trace
    trace = pauliMatrix[0,0]+pauliMatrix[1,1]
    ### End code here
    return(det, square, trace)
    
print('Determinant:', graded_pauli_check('Y')[0])
print('Trace:', graded_pauli_check('Y')[2])
