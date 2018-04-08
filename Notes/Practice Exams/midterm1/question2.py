# What is printed when the following Python code is executed?

import copy

lst1 = [1, [2, 3], [4, 5], 6]
lst2 = lst1
lst3 = lst1[ : ]
print("before, lst3 = ", lst3)
lst4 = copy.deepcopy(lst1)

lst1[0] = 10
print("1, lst3 = ", lst3)
lst1[1][1] = 30
print("after, lst3 = ", lst3)
print("lst1 =", lst1)
print("lst2 =", lst2)
print("lst3 =", lst3)
print("lst4 =", lst4)