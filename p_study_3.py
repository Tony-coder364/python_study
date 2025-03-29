#Determine the square palindrome number
# Many palindromic squares are palindromic because the number squared is a "simple" palindrome,
# for example 10012 = 1002001. But there are other palindromes that are not so simple and whose squares are palindromes,
# for example 26**2 = 676, 264**2 = 69696, 307**2 = 94249, 836**2 = 698896.
class square_palindromic_number():
    def __init__(self):
        return
    def judge(self,n):
        extract_root=n**0.5
        extract_root=int(extract_root)
        if extract_root**2==n:
            cop=str(n)
            if cop[::-1]==str(n):
                return True
        return False

    def feed(self,M):
        count=0
        for i in range(100,M+1):
            if self.judge(i) is True:
               count+=1
        return count
a=square_palindromic_number()
print(a.feed(500))