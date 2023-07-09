"""
Merge Without Extra Space
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing
order. Merge them in sorted order without using any extra space. Modify arr1 
so that it contains the first N elements and modify arr2 so that it contains 
the last M elements.

Example 1:

Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation:
After merging the two 
non-decreasing arrays, we get, 
0 1 2 3 5 6 7 8 9.
Example 2:

Input: 
n = 2, arr1[] = [10 12] 
m = 3, arr2[] = [5 18 20]
Output: 
arr1[] = [5 10]
arr2[] = [12 18 20]
Explanation:
After merging two sorted arrays 
we get 5 10 12 18 20.
Your Task:
You don't need to read input or print anything. You only need to complete the 
function merge() that takes arr1, arr2, n and m as input parameters and 
modifies them in-place so that they look like the sorted merged array when 
concatenated.

Expected Time Complexity:  O((n+m) log(n+m))
Expected Auxilliary Space: O(1)

Constraints:
1 <= n, m <= 105
0 <= arr1i, arr2i <= 107
"""
def merge(arr1, arr2, n,m):
    i = 0
    j = 0
    k = n - 1
    while (i <= k and j < m):
        if (arr1[i] < arr2[j]):
            i += 1
        else:
            temp = arr2[j]
            arr2[j] = arr1[k]
            arr1[k] = temp
            j += 1
            k -= 1
  
    arr1.sort()
    arr2.sort()
if __name__ == "__main__":
    arr1 = [13, 17, 18, 19, 20, 22, 22, 27, 36, 39, 46, 48, 50]
    arr2 = [4, 12, 45]
    n = 13
    m = 3
    merge(arr1, arr2, n, m)
    print(f"arr1: {arr1}\narr2: {arr2}")