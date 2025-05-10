# Meetingroom Reservation



class mettingroom_reservation():
        def __init__(self):
            return
        def reservation(self,lis):
            count=1
            li=sorted(lis,key=lambda x:x[1])
            current=li[0]
            for i in range(1,len(li)):
                if li[i][0]>=current[1]:
                    current=li[i]
                    count+=1
            return count



a=mettingroom_reservation()
print(a.reservation([[9,12],[15,20],[10,15]]))