class Solution:
    dp={}
    def climbStairs(self, n: int) -> int:
        def ways(i):
            if i in self.dp:
                return self.dp[i]
            if(i==0):
                return 1
            if i<0:
                return 0
            c=ways(i-1)
            c1=ways(i-2)
            self.dp[i]=c+c1
            return c+c1
        return ways(n)
        