# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
#



class process_commands():
    def __init__(self):
        self.lis=[]
        pass

    def insert(self,*params):
        pos=params[0]
        num=params[1]
        self.lis.insert(pos,num)

    def print(self,*args):
        print(self.lis)

    def remove(self,*param):
        num=param[0]
        self.lis.remove(num)

    def append(self,*param):
        num=param[0]
        self.lis.append(num)

    def sort(self,*param):
        self.lis.sort()

    def pop(self,*param):
        self.lis.pop()

    def reverse(self,*param):
        self.lis.reverse()

class recieve_commands():
    def __init__(self):
        pass
    def recieve(self):
        repeat = int(input(":"))
        connect = process_commands()
        for i in range(repeat):
            command=input(":").split(" ")
            service=command[0]
            parameter=None if len(command)==1 else list(map(int,command[1:]))
            getattr(connect,service)(parameter)



a=recieve_commands()
a.recieve()


