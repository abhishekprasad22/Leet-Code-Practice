"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""

# Number of elements in num1
m = int(input("Enter the number of elements in num1: "))
# Number of elementsin num2
n = int(input("Enter the number of elements in num2: "))

num1 = []

for i in range(m+n):
    if i>=m:
        num1.append(0)
    
    else:
        elements = int(input(f"Enter element {i+1}: "))
        num1.append(elements)

print(num1)

num2 = []

for j in range(n):
    elements = int(input(f"Enter element {j+1}: "))
    num2.append(elements)

print(num2)

num1 += num2


def bubblesort(arr):
    l = len(arr)
    for i in range(l-1):
        swapped = False
        for j in range(0, l-i-1):
            if arr[j]>arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not swapped:
            return

bubblesort(num1)

for k in range(n):
    num1.remove(0)

print(num1)