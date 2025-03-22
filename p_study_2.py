#

class sorting():
    def __init__(self):
        return
    def sort_1(self,n):
        lis=[]
        for i in range(1,n+1):
           lis.append(i)
        return [i for i in lis if i%2==0]+ [i for i in lis if i%2!=0][::-1]


a=sorting()
print(a.sort_1(5))
