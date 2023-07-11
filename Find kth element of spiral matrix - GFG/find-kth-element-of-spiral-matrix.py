#User function Template for python3

class Solution:
    def findK(self, A, n, m, k):
        left = 0
        right = m - 1
        top = 0
        bottom = n - 1
        dir = 0  # direction: 0 - left to right, 1 - top to bottom, 2 - right to left, 3 - bottom to top
    
        result = []
        while left <= right and top <= bottom:
            if dir == 0:
                for i in range(left, right + 1):
                    result.append(A[top][i])
                top += 1
            elif dir == 1:
                for i in range(top, bottom + 1):
                    result.append(A[i][right])
                right -= 1
            elif dir == 2:
                for i in range(right, left - 1, -1):
                    result.append(A[bottom][i])
                bottom -= 1
            elif dir == 3:
                for i in range(bottom, top - 1, -1):
                    result.append(A[i][left])
                left += 1
    
            dir = (dir + 1) % 4
    
        if k > len(result):
            return -1
    
        return result[k - 1]

        # Write Your Code here


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends