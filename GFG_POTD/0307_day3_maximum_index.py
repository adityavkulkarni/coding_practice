"""
Given an array arr[] of n positive integers. The task is to find the maximum 
of j - i subjected to the constraint of arr[i] <= arr[j].

Example 1:

Input:
n = 9
arr[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output: 
6
Explanation: 
In the given array arr[1] < arr[7]  satisfying 
the required condition (arr[i] <= arr[j])  thus 
giving the maximum difference of j - i which is
6(7-1).
Example 2:

Input:
N = 2
arr[] = {18, 17}
Output: 
0
Explanation: 
We can either take i and j as 0 and 0 
or we cantake 1 and 1 both give the same result 0.
Your Task:
Complete the function maxIndexDiff() which takes array arr and size n, as 
input parameters and returns an integer representing the answer. You don't 
have to print answer or take inputs. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 106
0 ≤ Arr[i] ≤ 109
"""

def maxIndexDiff(arr,n):
        """if n < 2: return 0
        res = []
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] <= arr[j]:
                    res.append(j-i)
        return max(res) if len(res) else 0
        """
        md = 0 
        l = [0]*n
        r = [0]*n
        l[0] = arr[0]
        for i in range(1, n):
            l[i] = arr[i] if arr[i]<l[i-1] else l[i-1]
            
        r[n-1] = arr[n-1]
        for j in range(n-2, -1, -1):
            r[j] = arr[j] if arr[j]>r[j+1] else r[j+1]
        
        i = 0
        j = 0
        md = -1
        while(i<n and j<n):
            if l[i] <= r[j]:
                md = md if md > j-i else j-i
                j += 1
            else:
                i += 1
        return md
            
if __name__ == "__main__":
    arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    n = 9
    print(maxIndexDiff(arr, n))