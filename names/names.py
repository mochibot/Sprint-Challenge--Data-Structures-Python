import time
import sys, os
dir_name = os.getcwd()
sys.path.append(dir_name + '\\binary_search_tree') 
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open(dir_name + '\\names\\' + 'names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(dir_name + '\\names\\' + 'names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Original code: O(n^2) runtime - 
# Results: 64 duplicates, runtime: 13.625582933425903 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# With binary search tree - 
# Results: 64 duplicates, runtime: 0.3467855453491211 seconds
# bst1 = BinarySearchTree(names_1[0])
# for name_1 in names_1[1:]:
#     bst1.insert(name_1) 

# duplicates = []
# for name_2 in names_2:
#     if bst1.contains(name_2):
#         duplicates.append(name_2)

# Trying stretch - only using standard Python collections 
# Results: 64 duplicates, runtime: 2.2046401500701904 seconds
# duplicates = [i for i in names_2 if i in names_1]

# Another approach with binary search
# Results: 64 duplicates, runtime: 0.10193634033203125 seconds
sorted_names_1 = [i for i in names_1]
sorted_names_1.sort()

def check_name(arr, target):
    if len(arr) == 0:
        return False
    low = 0
    high = len(arr) - 1
    while high >= low:
        middle = (low + high) // 2
        if target == arr[middle]:
            return True
        elif target < arr[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return False

duplicates = []
for name_2 in names_2:
    if check_name(sorted_names_1, name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

