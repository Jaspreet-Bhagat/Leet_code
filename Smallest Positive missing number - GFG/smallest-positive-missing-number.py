#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        n = len(arr)
        
        # Step 1: Separate positive elements from non-positive elements
        positive_nums = [x for x in arr if x > 0]
        positive_count = len(positive_nums)
        
        # Step 2: Modify the positive elements in-place to match their respective indices
        for i in range(positive_count):
            while positive_nums[i] > 0 and positive_nums[i] <= positive_count and positive_nums[positive_nums[i] - 1] != positive_nums[i]:
                # Swap the elements to their correct positions
                positive_nums[positive_nums[i] - 1], positive_nums[i] = positive_nums[i], positive_nums[positive_nums[i] - 1]
        
        # Step 3: Find the first index that does not match the value (missing number)
        for i in range(positive_count):
            if positive_nums[i] != i + 1:
                return i + 1
        
        # If all positive numbers from 1 to positive_count are present, the missing number is positive_count + 1
        return positive_count + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends