# 超级素数
# 提示信息：
# 在大于
# 1
# 的自然数中，除了
# 1
# 和它本身以外不再有其他因数的数，被称为素数，又叫质数。
# 超级素数是指一个素数，每去掉最后面的一个数字，总能保证剩下的数依然为素数。
# 比如：“373”就是一个超级素数，去掉个位的“3”后，“37”依然是素数；继续去掉“37”个位的 “7”后，“3”还是素数。
#
# 编程实现：
# 输入一个正整数
# n(10 ≤ n ≤ 108)，输出所有小于等于n的超级素数的个数。
# 输入描述：
# 输入一个正整数
# n(10 ≤ n ≤ 108)
# 输出描述：
# 输出所有小于等于n的超级素数的个数
# 样例输入1：
# 30
#
# 样例输出1：
# 6
#
# 样例输入2：
# 50
# 样例输出2：
# 8
#
# 样例输入3：
# 100
# 样例输出3：
# 13
#
# 样例输入4：
# 500
# 样例输出4：
# 21
#
# 样例输入5：
# 1000
# 样例输出5：
# 27


class super_primenumber():
    def __init__(self):
        return
    def Prime_judge(self,n):
        if n<2:
            return False
        if n==2:
            return True
        else:
            for i in range(2,n-1):
                if n%i==0:
                    return False
                else:
                    pass
        return True
    def Super_judge(self,i):
        while i!=0:
            if self.Prime_judge(i):
                i=i//10
            else:
                return False
        return True
    def Feeder(self,n):
        count=0
        for i in range(2,n):
            if self.Super_judge(i):
                count+=1
                print(i)
        return count



a=super_primenumber()
print(a.Feeder(30))
print(a.Prime_judge(1))




# reference!!!
# a= 1234
# while a!=0:
#     print(a//10)
#     a= a//10