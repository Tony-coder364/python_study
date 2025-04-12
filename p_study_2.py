#Problem
# Coding implementation:
# Given a positive integer N, arrange the positive integers between 1 and N (including 1 and N) in the order of increasing even numbers and decreasing odd numbers.
# For example:
# The given positive integer is 5, and the even numbers between 1 and 5 are 2 and 4, which are arranged in increasing order of even numbers as [2, 4], and the odd numbers between 1 and 5 are 1, 3, 5, which are arranged in decreasing order of odd numbers as [5, 3, 1], so the output result is: 2, 4, 5, 3, 1.
#
# Input description:
# Input a positive integer N
#
# Arrange all positive integers between 1 and N (including 1 and N) in the order of increasing even numbers and decreasing odd numbers, and output them with an English comma between positive integers (output even numbers first, then odd numbers)
# Sample input:_3.py_
# 5
# Sample output:
# 2, 4, 5, 3, 1


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
