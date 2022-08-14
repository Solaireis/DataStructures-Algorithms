
# create array of integers from
import array as arr 

# A)
array_int = arr.array('i', [1,2,3,4,5,6,7,8,9,10])
print(array_int)

# B)
array_int.insert(1,3)
print(array_int)

# C)
array_int.pop(-1)
print(array_int)

# D)
array_int.append(11)
print(array_int)

# E)
array_int.reverse()
print(array_int)

counters = [0] * 8
print(counters)