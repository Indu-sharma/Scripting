# Problem : Find the duplicate elements/check duplicity in the list. 

"""
Solution-1: Keep track of visited list.
Time Complexity: O(n^2), Space Complexity : O(n)
"""

my_list = [5, 4, 1, 2, 3, 5]
visited = []
for i in my_list:
    if i not in visited:
        visited.append(i)
    else:
        print(i)
"""
Solution-2: Use Counter module
Time Complexity: O(n), Space Complexity : O(n)
"""
from collections import Counter

my_list = [5, 4, 1, 2, 3, 5]
c = Counter(my_list)
for k in c:
    if c[k] > 1:
        print(k)

"""
Solution-3: Using Set 
Time Complexity: O(1), Space Complexity : O(1)
Constraints: 
1. It only checks if the duplicate elements exist.  
"""
my_list = [5, 4, 1, 2, 3, 5]
my_set = set(my_list)
if len(my_set) < len(my_list):
    print('Duplicate Exists')

"""
Solution-4 : Using Sorting 
Time Complexity : O(nlogn) , Space Complexity: O(1)
"""
my_list = [5, 4, 1, 2, 3, 5]
my_list.sort()
prev = my_list[0]
for i in my_list[1:]:
    if i == prev:
        print(f'{i}')
    else:
        prev = i
"""
Find the duplicate number in the array using O(n) time complexity and O(1) space complexity.

Solution - 5
Ex-
a  = [5, 4, 1, 2, 3, 5]
Step-1: Check a[a[0]] -> a[5] and if its > 0, a[a[0]] = - a[a[0]].
Step-2: Else, Duplicate exists.
Step-3: Repeat for all the Elements of the list.

OutPut:
Print all the duplicate numbers i.e 5

Constraints:

1. Values in the list should be in the range of 0 to len(a) - 1
2. This solution doesn't work if array is ReadOnly.
3. This solution only works if all the elements in the list are positive.


"""
my_list = [5, 4, 1, 2, 3, 5]
for i in range(len(my_list)):
    if my_list[abs(my_list[i])] < 0:
        print(f'{abs(my_list[i])}')
    else:
        my_list[abs(my_list[i])] = - my_list[abs(my_list[i])]