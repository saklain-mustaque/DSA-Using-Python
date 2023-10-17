from array import *

arr = array('i',[1,2,3])
# print(arr[1])
methods = list()
for method in dir(arr):
    if not method.startswith('__'):
        methods.append(method)

print(methods)
arr.append(4)
