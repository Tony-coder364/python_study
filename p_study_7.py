#square difference



class Square_difference():
    def __init__(self):
        return

    def calculate(self,lis):
        new_lis=[]
        average=sum(lis)/len(lis)
        for i in range(len(lis)):
            new_lis.append((lis[i]-average)**2)
        s_d=(sum(new_lis)/len(new_lis))**0.5
        return s_d

a=Square_difference()
print(a.calculate([100,60,40]))
# 1077.7205024873015
# 0.0