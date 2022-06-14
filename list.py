class Node:
   def __init__(self,pointer,data):
      self.pointer = pointer
      self.data = data

class List:
   def __init__(self):
      self.head = None
   
   def create(self,data):
      if(self.head == None):
         self.head = Node(None,data)

   def getHead(self):
      if(self.head != None):
         head = self.head
         return head

   def append(self,head,data):
      if(head.pointer != None):
         self.append(head.pointer,data)
      if(head.pointer==None):
         head.pointer = Node(None,data)
        


list = List()

list.create(34)
head = list.getHead()
list.append(head,45)
list.append(head,95)
list.append(head,78)
#newComment