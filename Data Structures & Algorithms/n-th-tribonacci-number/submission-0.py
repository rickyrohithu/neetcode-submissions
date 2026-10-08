class Solution:
    dp={}
    def tribonacci(self, n: int) -> int:
        def trib(i):
            if(i==0):
                return 0
            if(i==1):
                return 1
            if(i==2):
                return 1
            if i in self.dp:
                return self.dp[i]
            if(i>2):
                c=trib(i-1)+trib(i-2)+trib(i-3)
            self.dp[i]=c
            return c
        return trib(n)
        