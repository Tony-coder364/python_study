#Pick_Fruit


class Fruit():
    def __init__(self):
        pass
    def select(self,num):
        dp=[0]*len(num)
        dp[0]=num[0]
        dp[1]=max(num[1],dp[0])
        for i in range(2,len(num)):
            dp[i]=max(dp[i-1],dp[i-2]+num[i])
        return dp


a=Fruit()
print(a.select([1,5,2,1]))