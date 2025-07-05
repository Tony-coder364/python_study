#
# #定义节点类
# class Node():
#     def __init__(self,val,next=None):#val为必填值，next作为结尾时为空
#         self.val=val   #节点的值
#         self.next=next #指向的下一个目标
# #定义链表类
# class Link_Nodes():
#     def __init__(self):  #开始时链表为空
#         self.head=None
#     def create(self,lis):  #创建链表
#         dummy=current=Node(0)  #dummy 是哑节点，不属于链表内容；current 用作构建链表的游标
#         for i in lis:   #遍历给的列表
#             current.next=Node(i)  #current作为移动cursor，逐步创建后续链表
#             current=current.next  #current移向下一位
#         return dummy.next #返回 dummy.next，跳过 dummy 节点，返回真正链表的头部
#
    def delete(self,target,linkn):
        dummy=current=Node(0)
        while linkn:
            if linkn.val!=target:
                 current.next=Node(linkn.val)
                 current=current.next
            linkn=linkn.next
        return dummy.next

    # def delete(self,target,linkn):
    #     dummy=current=Node(0)
    #     current.next=linkn
    #     while current.next:
    #         if current.next.val==target:
    #             current.next=current.next.next
    #         else:
    #             current=current.next
    #     return dummy.next
#
#     def prink_Node(self,linkn):
#         while linkn:
#             print(linkn.val)
#             linkn=linkn.next
#
#
#
#
# b=Link_Nodes()
# linkk=b.create([1,2,3])
# b.delete(2,linkk)
# b.prink_Node(b.delete(2,linkk))



