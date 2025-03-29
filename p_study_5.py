#ming's backpack
# There is a schoolbag with a volume of m and n different commodities on Xiaolan's table, and each commodity is marked with the volume and value of the commodity.
# Xiaolan needs to meet the following requirements to select commodities to put into the schoolbag
# Requirement 1: The total volume of the selected commodities does not exceed the volume of the schoolbag;
# Requirement 2: The total value of the selected commodities is the largest.
# Please help Xiaolan calculate the maximum value of the commodities that can be put into the schoolbag.
# Input description:
# In the first line, enter two positive integers m and n, m represents the volume of the schoolbag,
# and n represents the number of goods. A comma separates the two positive integers
# In the second line, enter n positive integers representing the volume of the goods, separated by a comma
# In the third line, enter n positive integers representing the value of the goods,
# separated by a comma (the order of entering the value of the goods corresponds to the order of entering the volume of the goods)
class backpack():
    def __init__(self):
        return
    def best_solution(self,back_v,option_v,option_value):
        lis=[]
        count=0
        for i in range(len(option_v)):
            lis.append([option_v[i],option_value[i]])
        lis.sort(key=lambda x:x[1],reverse=True)
        for j in lis:
            if back_v-j[0]>=0:
                count+=j[1]
                back_v-=j[0]
        return count


#[[6, 5], [4, 2], [2, 1]]
a=backpack()
print(a.best_solution(11,[2,6,4],[1,5,2]))