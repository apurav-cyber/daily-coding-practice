import numpy as np 
# creating one dimational array 
arry_1d = np.array([1,2,3,4,5,6,7])
print("one dimational array",arry_1d)
#crearting 2 dimational array 
arry_2d = np.array([[12,34,56,67],[34,56,78,90]])
print("two dimational arry",arry_2d)
#creating a 2d array of zeros 
arry_0d = np.zeros((3,6))
print("array consisting only zero values")
print(arry_0d)
#creating an array ranged from 0 to 9 
arry_range =   np.arange(0,9)
print("array by range ")
print(arry_range)
#creating an array by five evenly spaced value 
arry_space = np.linspace(1,30,5)
print("evenly spaced array")
print(arry_space)
#shape and size of an array 
print("shape of an array name arry_2d",arry_2d.shape)
print("size of an array name arry_2d",arry_2d.size)
#data type of an array 
print("data type of an array",arry_2d.dtype)
#array consisting ones 
arry_ones = np.ones((3,7))
print("array conisting only 1 ",arry_ones)