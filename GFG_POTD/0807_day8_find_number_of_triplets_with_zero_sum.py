"""
Find triplets with zero sum
Given an array arr[] of n integers. Check whether it contains a triplet that 
sums up to zero. 

Note: Return 1, if there is at least one triplet following the condition else 
return 0.

Example 1:

Input: n = 5, arr[] = {0, -1, 2, -3, 1}
Output: 1
Explanation: 0, -1 and 1 forms a triplet
with sum equal to 0.
Example 2:

Input: n = 3, arr[] = {1, 2, 3}
Output: 0
Explanation: No triplet with zero sum exists. 

Your Task:
You don't need to read input or print anything. Your task is to complete the 
boolean function findTriplets() which takes the array arr[] and the size of 
the array (n) as inputs and print 1 if the function returns true else print 0 
if the function returns false. 

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constrains:
1 <= n <= 104
-106 <= Ai <= 106
"""
def findTriplets(arr, n):
    triplets = []
    arr.sort()  
    for i in range(n-2):
        left = i + 1
        right = n - 1

        while left < right:
            triplet_sum = arr[i] + arr[left] + arr[right]

            if triplet_sum == 0:
                triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
                return 1
            elif triplet_sum < 0:
                left += 1
            else:
                right -= 1

    return 0

if __name__ == "__main__":
    n = 3
    arr = [1,2,3]
    print(findTriplets(arr, n))
