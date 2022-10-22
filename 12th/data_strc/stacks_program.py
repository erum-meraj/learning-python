'''  Write a program  to implement a stack for  book details (bookno, book name).'''
top=None
def isempty(stk):
   if stk==[]:
      return True
   else:
      return False

def Push(stk,item):
   stk.append(item)
   top=len(stk)-1


def Pop(stk):
   if isempty(stk):
      return "underflow"
   else:
      item=stk.pop()
      if len(stk)==0:
         top=None
      else:
         top=len(stk)-1
      return item

      
def Peek(stk):
   if isempty(stk):
      return "underflow"
   else:
      top=len(stk)-1
      return stk[top]

def Display(stk):
   if isempty(stk):
      print("Stack is empty")
   else:
      top=len(stk)-1
      print("Book No---Book Name")
      #print(stk[top],"     <--top")                            
      for a in range(top,-1,-1):
         print(stk[a])


#main function

stack=[]

while True:
   print("1.push")
   print("2.Pop")
   print("3.Peek")
   print("4.Display")
   print("5.Exit")
   ch=int(input("Enter your choice(1-5):"))
   if ch==1:
      bno= input("enter  book no.")
      bname=input("enter book name ")
      item=[bno, bname]
      Push(stack,item)
   elif ch==2:
      item=Pop(stack)
      if item=="underflow":
         print("Staack is empty")
      else:
         print("Popped item is",item)

   elif ch==3:
      item=Peek(stack)
      if item=="underflow":
         print("Staack is empty")
      else:
         print("Topmost item is",item)
   elif ch==4:
      Display(stack)
   elif ch==5:
      break
   else:
      print("Invalid")
                               

                                          








              














                            
              
              
