# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findTarget(self, root, k):
#         seen = set()

#         def dfs(node):
#             if not node:
#                 return False
            
#             if (k - node.val) in seen:
#                 return True
            
#             seen.add(node.val)
            
#             return dfs(node.left) or dfs(node.right)
        
#         return dfs(root)

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(7)

# k = 9   

# sol = Solution()
# print(sol.findTarget(root, k))
  


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def pathsum(self, root, k):
#         seen = set()

#         def dfs(node):
#             if not node:
#                 return False
            
#             if (k - node.val) in seen:
#                 return True
            
#             seen.add(node.val)
            
#             return dfs(node.left) or dfs(node.right)
        
#         return dfs(root)

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(11)
# root.left.left.left=TreeNode(3)
# root.left.left.right=TreeNode(-2)
# root.left.right.right = TreeNode(1)

# k = 8

# sol = Solution()
# print(sol.pathsum(root, k))


# class Node:
#     def __init__(self,val=None,Next=None):
#         self.val=val
#         self.Next=Next

# class SinglyLinkedList:
#     def __init__(self):
#         self.start=None

#     def is_empty(self):
#         if self.start==None:
#             return None    

#     def insert_at_start(self,val):
#         newNode=Node(val,self.start)
#         self.start=newNode

#     def insert_at_end(self,val,temp):
#         newNode=Node(val)
#         if self.start is None:
#             self.start=newNode
#         else:
#             temp=self.start
#             while temp.Next:
#                 temp=temp.Next
#                 temp.Next=newNode

#     def display(self,temp):
#         temp=self.start
#         while temp:
#             print(temp.val,end="->")       
#             temp=temp.next
#         print("None")    

#     def search(self,val):
#         temp=self.start
#         while temp:
#             if temp.val==val:
#                 return temp
           
#             temp=temp.Next
#             return None
        

# def insert_after(self, key, val):
#     if self.start is None:
#         return
    
#     temp = self.start
    
#     while temp:
#         if temp.val == key:       
#             newNode = Node(val)    
#             newNode.next = temp.next
#             temp.next = newNode
#             return
#         temp = temp.next

#     def print(self,temp):
#         temp=self.start
#         while temp:
#             print(temp.val,end="->")       
#             temp=temp.next
#         print("None")    
          

#     def delete_first(self):
#         if self.start is None:
#             return None
#         else:
#             self.start=self.start.Next
        
#     def delete_last(self):  
#         if self.start is None:
#             return None  
#         elif self.start.next is None:
#             self.start=None
#         else:
#                 temp=self.start
#         while temp.next is not None:
#             temp=temp.Next
#             temp.prev.next=None

#     def delete_after(self,val):  
#         if self.start is None:
#             return None  
#         temp=self.start
#         while temp and temp.data!=val:
#             temp=temp.Next
#         if temp and temp.Next:
#             temp.Next=temp.Next.Next
            


#     def reverse(self):
#         prev=None
#         current=self.start
#         while current:
#             current=current.next
#             current.next=current
#             current.next=prev
#             prev=prev.next


            

# class Node:
#     def __init__(self,val=None,next=None):
#         self.val=val
#         self.next=next

# class SinglyLinkedList:
#     def __init__(self):
#         self.start = None
        
#     def is_empty(self):
#         return self.start is None
        
#     def insert_at_start(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             self.start=new_Node
#         else:
#             new_Node.next=self.start
#             self.start= new_Node

#     def insert_at_end(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             self.start=new_Node
#         else:
#             temp=self.start
#             while temp.next:
#                 temp=temp.next
#             temp.next=new_Node        

#     def insert_after(self,Target_val,val):
#         new_Node=Node(val)
#         if self.start is None:
#             self.start=new_Node
#             return
#         temp=self.start    
#         while temp:
#             if temp.val==Target_val:
#                 new_Node.next=temp.next
#                 temp.next=new_Node
#                 return
#             temp=temp.next    

#     def delete_first(self):
#         if self.start is None:
#             return None
#         else:
#             self.start=self.start.next     
  
#     def delete_end(self):
#        if self.start is None:
#         return None
#        if self.start.next is None:
#         self.start = None
#         return
#        temp = self.start
#        while temp.next.next is not None:
#         temp = temp.next
#        temp.next = None

#     def delete_after(self,data):
#         if self.start is None:
#          return None
#         temp=self.start
#         while temp:
#             if temp.val==data:
#                 if temp.next is None:
#                     return
#                 temp.next=temp.next.next
#             temp=temp.next 

#     def print(self):
#         temp=self.start
#         while temp:
#             print(temp.val,end="->")
#             temp=temp.next
#         print("None")        
            

#     def display(self):
#         temp=self.start
#         while temp:
#             print(temp.val,end="->")
#             temp=temp.next
#         print("None")        

# SLL=SinglyLinkedList()
# SLL.insert_at_start(2)            
# SLL.insert_at_start(4)            
# SLL.insert_at_start(6)            
# SLL.insert_at_start(8)  
# SLL.insert_at_start(10)
# SLL.insert_at_end(20)
# SLL.insert_at_end(30)

# SLL.insert_after(2,18)
# SLL.insert_after(20,18)
# SLL.delete_first()
# SLL.delete_end()
# SLL.delete_after

# SLL.display()




# class Node:
#     def __init__(self,val=None,next=None):
#         self.val=val
#         self.next=next

# class SinglyLinkedList:
#     def __init__(self):
#         self.start=None

#     def is_empty(self):
#        return self.start is None

#     def insert_at_starting(self,val):
#         new_Node=Node(val)
#         new_Node.next=self.start
#         self.start=new_Node        
        
#     def insert_at_end(self,val):
#         new_Node=Node(val)
#         if self.start is not None:
#             temp=self.start
#             while temp.next is not None:
#              temp=temp.next
#             temp.next=new_Node
#         else:
#             self.start=new_Node       

#     def insert_at_middle(self,item,val):
#         new_Node=Node(val)
#         temp=self.start
#         while temp is not None:
#          if temp.val==item:
#           new_Node.next=temp.next         
#           temp.next=new_Node
#          temp=temp.next

#     def delete_first(self):
#        if self.start is not None:
#           self.start=self.start.next
#        else:
#           return None        
       
#     def delete_last(self):
#        if self.start is None:
#           return None
#        if self.start.next is None:
#           self.start=None
#        if self.start is not None:
#           temp=self.start
#           while temp.next.next is not None:   
#             temp=temp.next 
#           temp.next=None


#     def delete_after(self,item):
#        if self.start is None:
#           return None
#        if self.start.next is None:
#           self.start=None
#        if self.start is not None:
#           temp=self.start  
#           while temp is not None and temp.next is not None: 
#            if temp.val==item:
#              temp.next=temp.next.next
#            temp=temp.next  
                   
        
#     def display(self):
#         temp=self.start
#         while temp:
#             print(temp.val,end=" ")
#             temp=temp.next

# SLL=SinglyLinkedList()
# SLL.insert_at_starting(5)
# SLL.insert_at_starting(4)
# SLL.insert_at_starting(3)
# SLL.insert_at_starting(2)
# SLL.insert_at_starting(1)

# SLL.insert_at_end(10)
# SLL.insert_at_end(9)
# SLL.insert_at_end(8)
# SLL.insert_at_end(7)
# SLL.insert_at_end(6)

# SLL.insert_at_middle(1,100)
# SLL.insert_at_middle(2,200)
# SLL.insert_at_middle(6,3000)
# SLL.insert_at_middle(8,40000)

# SLL.delete_first()
# SLL.delete_last()
# SLL.delete_after(10)

# SLL.display()



# class Node:
#     def __init__(self,val=None,prev=None,next=None):
#         self.prev=prev
#         self.val=val
#         self.next=next

# class DoublyLinkedList:
#     def __init__(self):
#         self.start=None

#     def is_empty(self):
#         if self.start is None:
#             return None

#     def insert_at_start(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             self.start=new_Node
#         else:
#             new_Node.next=self.start
#             self.start.prev=new_Node 
#             self.start=new_Node

#     def insert_at_end(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             self.start=new_Node
#         if self.start.next is not None:
#             temp=self.start
#             while temp.next is not None:
#                 temp=temp.next      
#             temp.next=new_Node 
#             new_Node.prev=temp

#     def insert_at_middle(self, val, item):
#      new_Node = Node(val)

#      if self.start is None:
#         self.start = new_Node
#      else:
#         temp = self.start

#         while temp is not None:
#             if temp.val == item:
#                 new_Node.next = temp.next
#                 new_Node.prev = temp
#                 if temp.next is not None:
#                     temp.next.prev = new_Node
#                 temp.next = new_Node
#                 return
#             temp = temp.next

#     def delete_at_start(self):
#         if self.start is None:
#             return None
#         if self.start.next is None:
#             self.start=None
#         else:
#             self.start=self.start.next       

#     def delete_at_end(self):
#         if self.start is None:
#             return None
#         if self.start.next is None:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next is not None:
#                 temp=temp.next      
#             temp.prev.next=None               

#     def delete_at_middle(self,item):
#         if self.start is None:
#             return None
#         if self.start.next is None:
#             self.start=None
#         else:
#             temp=self.start
#             while temp is not None:
#                 if temp.val==item:
#                     temp.next=temp.next.next
#                     temp.next.next.prev=temp.next
#                 temp=temp.next                


#     def display(self):
#         temp=self.start
#         while temp is not None:
#             print(temp.val,end=" ")
#             temp=temp.next

# DLL=DoublyLinkedList()
# DLL.insert_at_start(5)         
# DLL.insert_at_start(4)                                     
# DLL.insert_at_start(3)                                     
# DLL.insert_at_start(2)                                     
# DLL.insert_at_start(1)     

# DLL.insert_at_end(10)
# DLL.insert_at_end(9)
# DLL.insert_at_end(8)
# DLL.insert_at_end(7)
# DLL.insert_at_end(6)

# DLL.insert_at_middle(0,10)
# DLL.insert_at_middle(00,9)
# DLL.insert_at_middle(000,8)
# DLL.insert_at_middle(0000,7)
# DLL.insert_at_middle(00000,8)

# DLL.delete_at_start()
# DLL.delete_at_end()
# DLL.delete_at_middle(8)

# DLL.display()


# class Node:
#     def __init__(self,val=None,prev=None,next=None):
#         self.val=val
#         self.prev=prev
#         self.next=next

# class CircularLinkedList:
#     def __init__(self):
#         self.start=None

#     def is_empty(self):
#         if self.start is None:
#             return None

#     def insert_at_start(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             new_Node.next=new_Node
#             self.start=new_Node
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#                 temp=temp.next
#             temp.next=new_Node    
#             new_Node.next=self.start
#             self.start=new_Node

#     def insert_at_end(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             new_Node.next=new_Node
#             self.start=new_Node
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#                 temp=temp.next
#             self.start.prev=new_Node
#             temp.next=new_Node
#             new_Node.next=self.start     

#     def insert_at_middle(self,val,item):
#         new_Node=Node(val)
#         if self.start is None:
#             new_Node.next=new_Node
#             self.start=new_Node
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#                  if temp.val==item:
#                     new_Node.next=temp.next
#                     new_Node.prev=temp
#                     temp.next.prev=new_Node
#                     temp.next=new_Node
#                  temp=temp.next
#                  if temp==self.start:
#                      break
    
#     def delete_first(self):
#         if self.start is None:
#             return None
#         if self.start==self.start.next:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#                 temp=temp.next    
#             temp.next=self.start.next
#             self.start.prev=temp
#             self.start=self.start.next

#     def delete_last(self):
#         if self.start is None:
#             return None
#         if self.start==self.start.next:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next.next!=self.start:
#                 temp=temp.next
#             temp.next=self.start     

#     def delete_middle(self,item):
#         if self.start is None:
#             return None
#         if self.start==self.start.next:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#                 if temp.val==item:
#                     temp.next=temp.next.next
#                 temp=temp.next    


#     def display(self):
#         temp=self.start
#         while temp is not None:
#             print(temp.val,end=" ")
#             temp=temp.next
#             if temp==self.start:
#                 break

# CLL=CircularLinkedList()
# CLL.insert_at_start(10)
# CLL.insert_at_start(9)  
# CLL.insert_at_start(8)  
# CLL.insert_at_start(7)  
# CLL.insert_at_start(6)  

# CLL.insert_at_end(1)
# CLL.insert_at_end(2)
# CLL.insert_at_end(3)
# CLL.insert_at_end(4)
# CLL.insert_at_end(5)

# CLL.insert_at_middle(68,6)
# CLL.insert_at_middle(88,7)
# CLL.insert_at_middle(98,9)
# CLL.insert_at_middle(200,2)
# CLL.insert_at_middle(4000,4)

# CLL.delete_first()
# CLL.delete_first()

# CLL.delete_last()
# CLL.delete_last()
# CLL.delete_middle(10)
# CLL.display()


# class Node:
#     def __init__(self,val=None,prev=None,next=None):
#         self.val=val
#         self.prev=prev
#         self.next=next
        
# class DoublyCircularLinkedList:
#     def __init__(self):
#         self.start=None

#     def is_emmpty(self):
#         if self.start is None:
#             return None

#     def insert_at_start(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             new_Node.next=new_Node
#             new_Node.prev=new_Node
#             self.start=new_Node
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#              temp=temp.next
#             new_Node.next=self.start 
#             new_Node.prev=temp
#             temp.next=new_Node
#             self.start.prev=new_Node
#             self.start=new_Node

#     def insert_at_end(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             new_Node.next=new_Node
#             new_Node.prev=new_Node
#             self.start=new_Node
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#                 temp=temp.next
#             new_Node.prev=temp
#             new_Node.next=self.start
#             temp.next=new_Node
#             self.start.prev=new_Node

#     def insert_in_Middle(self,val,item):
#         new_Node=Node(val)
#         if self.start is None:
#             new_Node.prev=new_Node
#             new_Node.next=new_Node
#             self.start=new_Node
#         else:
#             temp=self.start
#             while temp:
#                 if temp.val==item:
#                  new_Node.next=temp.next
#                  new_Node.prev=temp
#                  temp.next.prev=new_Node
#                  temp.next=new_Node       

#                 temp=temp.next   
#                 if temp==self.start:
#                     break  

#     def delete_at_start(self):
#         if self.start is None:
#             return None
#         else:
#             temp=self.start
#             while temp.next!=self.start:
#                 temp=temp.next 
#             temp.next=self.start.next
#             self.start=self.start.next
#             self.start.prev=temp         

#     def delete_at_end(self):
#         if self.start is None:
#             return None
#         if self.start.next==self.start:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next.next!=self.start:
#                 temp=temp.next
#             temp.next=self.start      
#             self.start.prev=temp

#     def delete_middle(self,item):
#         if self.start is None:
#             return None
#         if self.start.next==self.start:
#             self.start=None
#         else:
#             temp=self.start
#             while temp:
#                 if temp.val==item: 
#                     temp.prev.next = temp.next
#                     temp.next.prev = temp.prev
#                 temp=temp.next
#                 if temp==self.start:
#                     break               
         

#     def display(self):
#         temp=self.start
#         while temp:
#             print(temp.val,end=" ")
#             temp=temp.next

#             if temp==self.start:
#              break

# DCLL=DoublyCircularLinkedList()
# DCLL.insert_at_start(1)                   
# DCLL.insert_at_start(2)                     
# DCLL.insert_at_start(3)                     
# DCLL.insert_at_start(4)                     
# DCLL.insert_at_start(5) 

# DCLL.insert_at_end(6)
# DCLL.insert_at_end(7)
# DCLL.insert_at_end(8)
# DCLL.insert_at_end(9)
# DCLL.insert_at_end(10)

# DCLL.insert_in_Middle(100,1)
# DCLL.insert_in_Middle(500,5)
# DCLL.insert_in_Middle(800,8)
# DCLL.insert_in_Middle(400,4)

# DCLL.delete_at_start()
# DCLL.delete_at_end()

# DCLL.delete_middle(4)

# DCLL.display()

# class Node:
#     def __init__(self,val=None,next=None):
#         self.val=val
#         self.next=next

# class SinglyLinkedList:
#     def __init__(self):
#         self.start=None

#     def is_empty(self):
#         if self.start is None:
#             return None
        
#     def insert_at_start(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             self.start=new_Node
#         else:
#             new_Node.next=self.start
#             self.start=new_Node

    # def display(self):
    #     temp=self.start
    #     while temp:
    #         print(temp.val,end=" ")
    #         temp=temp.next   

#     def middle_term(self):
#         if self.start is None:
#             return None
        
#         slow=self.start
#         fast=self.start    
#         while fast is not None and fast.next is not None:
#           slow=slow.next
#           fast=fast.next.next
#         return slow.val     

#     def detect_cycle(self):
#         if self.start is None:
#             return None
#         slow=self.start
#         fast=self.start
#         while fast is not None and fast.next is not None:
#             slow=slow.next
#             fast=fast.next.next

#             if slow==fast:
#                 return True
            
#         return False
        
#     def n_node(self,n):
#         count=0
#         temp=self.start
#         while temp:
#             count+=1
#             temp=self.start  
#             pos=count-n
#             temp=self.start
#             for i in range(pos):  
#                 temp=temp.next
#             return temp.val    
        
#     def remove_duplicate(self):   
#         if self.start is None:
#             return None
#         temp=self.start
#         while temp.next is not None:
#             if temp.val==temp.next.val:
#                 temp.next=temp.next.next
#             else:
#                 temp=temp.next     
                 
#     def reverse_list(self):
#         if self.start is None:
#             return None
#         prev=None
#         temp=self.start
#         while temp:
#             nxt=temp.next
#             temp.next=prev
#             prev=temp
#             temp=nxt
#         self.start=prev    

     
#     def middle_element(self):
#         if self.start is None:
#             return None
#         slow=self.start
#         fast=self.start
#         while fast is not None and fast.next is not None:
#             slow=slow.next
#             fast=fast.next.next

#         return slow.val                    
    
#     def search_element(self,item):
#         if self.start is None:
#             return None
#         else:
#             temp=self.start
#             while temp:
#                 if temp.val==item:
#                     return temp
#                 temp=temp.next
#             return None
        
#     def duplicate_element(self):
#         if self.start is None:
#             return None
#         temp=self.start
#         while temp.next is not None:
#             if temp.val==temp.next.val:
#                 return temp.next
#             temp=temp.next 
#         return None       

# SLL=SinglyLinkedList()
# SLL.insert_at_start(50)         
# SLL.insert_at_start(40)                            
# SLL.insert_at_start(30)                            
# SLL.insert_at_start(20)  
# SLL.insert_at_start(10)
# SLL.insert_at_start(40)

# print("middle term=",SLL.middle_term())
# print(SLL.detect_cycle())
# print(SLL.n_node(2))
# result = SLL.search_element(30)
# if result:
#     print("found:",result.val)
# else:
#     print("not foound")    

# result = SLL.duplicate_element()

# if result:
#     print("Duplicate:", result.val)
# else:
#     print("No Duplicate Found")
# SLL.display()
# print()

# class Node:
#     def __init__(self,val=None,next=None):
#         self.val=val
#         self.next=next

# class SinglyLinkedList:
#     def __init__(self):
#         self.start=None

#     def insert_at_start(self,val):
#         new_Node=Node(val)
#         if self.start is None:
#             self.start=new_Node
#         else:
#             new_Node.next=self.start
#             self.start=new_Node
#     def display(self):
#         temp=self.start
#         while temp:
#             print(temp.val,end=" ")
#             temp=temp.next     

#     def Count_Perfect_square_Numbers_in_a_Linked_List(self):
#         if self.start is None:
#             return None
#         temp=self.start
#         count=0
#         while temp:
#            n=temp.val
#            i=1
#            while i*i<=n:
#                 if i*i==n:
#                  count+=1
#                  break
#                 i+=1
#            temp=temp.next
#         return count 


# SLL=SinglyLinkedList()
# SLL.insert_at_start(123)         
# SLL.insert_at_start(25)                            
# SLL.insert_at_start(820)                            
# SLL.insert_at_start(9)  
# SLL.insert_at_start(16)
# SLL.insert_at_start(4)
# SLL.display()
# print()
# print("Count Perfect Square Numbers in a Linked List:",SLL.Count_Perfect_square_Numbers_in_a_Linked_List())


prices=list(map(int,input("enter the prices:").split(",")))
min_price=prices[0]
max_profit=0
result=[]
for i in range(len(prices)):
    if prices[i]<min_price:
        min_price=prices[i]
    profit=prices[i]-min_price    
    if profit>max_profit:
        max_profit=profit
print("max and min profit difference:",max_profit)            


   