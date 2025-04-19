# happy_number



class happy_number():
    def __init__(self):
        return

    def split(self,num):
        lis=[]
        while num!=0:
            lis.append(num%10)
            num=num//10
        return lis
    def judge(self,lis):
        su=0
        for i in lis:
            su+=i**2
        return su
    def feeder(self,num):
        try:
            lis=self.split(num)
            ans=self.judge(lis)
            if ans==1:
                return True
            return self.feeder(ans)
        except:
            return False

a=happy_number()
print(a.feeder(19))