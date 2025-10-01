import copy
original_list = [1, [2, 3], [4, [5, 6]]]
copied_list = copy.deepcopy(original_list)
original_list[2][1][0] = 7
print(original_list)  
print(copied_list)
