class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def tcost(i):
            if i in dp:
                return dp[i]
            if(i==len(cost)):
                return 0
            if(i>len(cost)):
                return float('inf')
            c1=cost[i]+tcost(i+1)
            c2=cost[i]+tcost(i+2)
            dp[i]=min(c1,c2)
            return min(c1,c2)
        return min(tcost(0),tcost(1))
        
        