#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        x = m-l+1
        y = r-m 
        L= [0]*(x) 
        R= [0]*(y) 
      
        for i in range(0,x): 
            L[i] = arr[l+i] 
      
        for j in range(0,y): 
            R[j] = arr[m+1+j] 
        i = 0
        j = 0     
        k = l    
        while i<x and j<y: 
            if L[i] <= R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
            k += 1
      
        while i < n1: 
            arr[k] = L[i] 
            i += 1
            k += 1
        
    def mergeSort(self,arr, l, r):
        #code here
        if l<r:
            m=l+(r-l)//2
            
            self.mergeSort (arr, l, m)
            self.mergeSort (arr, m+1, r)
            self.merge (arr, l, m, r)


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
