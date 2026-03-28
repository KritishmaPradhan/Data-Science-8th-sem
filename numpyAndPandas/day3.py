# introduction to pandas
import pandas as pd
mark = pd.Series([1,2,3], index = ["Ram", "Hem", "Siya"])
print(mark)
print(mark["Ram"])    # get element by custom made index
print(mark.loc["Ram"])        # gets location for corresp element of Ram
print(mark.iloc[2])        # gets index location

# get element by index
mark1 = pd.Series([1,2,3])
print(mark1[2])
print(mark1.info())           #detiled info about element
print(mark1.head(2))            # first two element
print(mark1.tail(2))            # last two element
print(mark1.describe())         # gives statictical measures mean modes....
print(mark1.isnull())           # give null value true or false
print(mark1[mark1 < 3])           # conditional query directly in index

dataset1 = pd.DataFrame({"name": ["kri", "greta", "min"],
                         "age": [23,22,10],
                         "marks": [45,55,40]})
print(dataset1)

#  new data set
dataset2 = pd.DataFrame({"a": ["greg", "greta", "nima"],
                         "b": [23,22,10],
                         "c": [45,55,40]},
                         index = [1,2,3],
                        columns = ["a", "b", "c"])
print(dataset2)

# introduction to numpy
import numpy as np
import random as random
student_mks = [1,2,3]
n = np.array([1,2,3], dtype= str)
print(type(student_mks))
print(type(n))
print(n)

#tuple
tuple_a = np.array([[1,5,8], (6,7,9)])
print(type(tuple_a))
print(tuple_a)
print(tuple_a[1])

zeros = np.zeros((2,3), dtype = int)   # array of zeros
print(zeros)

maualarray = np.arange(1,9,2)    # an array from elements 1 to 9 with step size 2
print(maualarray)

randomnum = np.random.random([2,2])
print(randomnum)
np.save("arraysave.npy",randomnum)

# mathematical operations in array
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print("the sum is", np.add(array1,array2))
print("the product is", array1*array2)




