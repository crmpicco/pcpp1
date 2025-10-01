import copy
title1 = ['Python', 'Course', [3, 10, 0]]
title2 = copy.copy(title1)
title1[2][1] = 11
print(title1)
print(title2)
