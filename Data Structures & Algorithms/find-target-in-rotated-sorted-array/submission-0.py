class Solution:
    def search(self, a: List[int], target: int) -> int:
        l=0
        r=len(a)-1
        while(l<=r):
            m=(l+r)//2
            if(a[m]==target):
                return m
            if(a[l]<=a[m]):
                if(a[l]<=target and a[m]>=target):
                    r=m-1
                else:
                    l=m+1
            else:
                if(a[m]<=target and a[r]>=target):
                    l=m+1
                else:
                    r=m-1
        return -1

        