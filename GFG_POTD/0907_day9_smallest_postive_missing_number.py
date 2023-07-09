"""
Smallest Positive missing number
You are given an array arr[] of N integers including 0. The task is to find 
the smallest positive number missing from the array.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the 
smallest positive missing number in the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106
"""
def missingNumber(arr,n):
    pos_arr = [x for x in arr if x > 0]
    if len(pos_arr):
        if sum(pos_arr) == len(pos_arr)*(len(pos_arr)+1)/2:
            return max(pos_arr)+1
        for i in range(1, (max(pos_arr))+1):
            if i not in pos_arr: return i
        return max(pos_arr)+1
    else: return 1
    
if __name__ == "__main__":
    N = 5
    arr = [0,-10,1,3,-20]
    print(missingNumber(arr, N))
