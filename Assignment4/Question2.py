# Write a Python program to triple all numbers of a given list of integers. 
# Use Python map.



list_1 = [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:[3, 6, 9, 12, 15, 18, 21]

triple = list(map(lambda list_1:list_1*3, list_1))
print("Triple of list number :",triple)
