class Solution:
    def findMin(self, a: List[int]) -> int:
        l=0
        r=len(a)-1
        while(l<r):
            m=(l+r)//2
            if a[m]>a[r]:
                l=m+1
            else:
                r=m
        return a[l]
                
                    
        