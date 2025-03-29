# candy distribute
# There are N children lined up from left to right. Each child has a certain number of candies in his hand, and the total number of candies is a multiple of N. Calculate the minimum number of adjustments to make each child have the same number of candies.
#
# The adjustment rules are as follows:
# Rule 1: Each child's candies can only be adjusted to the hands of two children on the left and right;
# Rule 2: The first child's candies can only be adjusted to the hands of the second child;
# Rule 3: The last child's candies can only be adjusted to the hands of the second to last child.
# For example: The original number of candies for children 1 to 3 is 6, 4, and 2 respectively.
# n=0
class candy_distribute():
    def __init__(self):
        return
    def dis(self,lis):
        global n
        target=sum(lis)/len(lis)
        if len(set(lis))==1:
            return
        for i in range(len(lis)):
            if lis[i]>target and i<=len(lis)-2:
               lis[i+1]+=lis[i]-target
               lis[i]=target
               n+=1
        self.dis(lis[::-1])
        # for j in range(len(lis),-1):
        #     if lis[i] > target:
        #         lis[i + 1] += lis[i] - target
        #         lis[i] = target
        #         n+=1

a=candy_distribute()
print(a.dis([2,4,6]))
print(n)