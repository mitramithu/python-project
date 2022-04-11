#1. adding values to tuple

tuple=(1,2)
list=list(tuple)
list.append(3)
tuple=tuple(list)
print(tuple)

#2.

tuple=(1,2,3,4)
tuple=tuple+(12,)
print(tuple)

