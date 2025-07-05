



class LCF_GCM():
      def __init__(self):
          return

      def LCF(self,a,b):
          if b==0:
              return a
          else:
              return self.LCF(b,a%b)

      def GCM(self,a,b):
          return a*b//self.LCF(a,b)

      def feeder(self,lis):
          yue=self.LCF(lis[0],lis[1])
          bei=self.GCM(lis[0],lis[1])
          for i in lis[2:]:
              bei=self.GCM(bei,i)

              yue=self.LCF(yue,i)

          return yue,bei

a=LCF_GCM()
print(a.feeder([2,4,6]))