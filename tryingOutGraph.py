        
# # class StaticMethod(object):
# #     def __init__(self, func):
# #         self.func = func

# #     def __get__(self, obj, cls):
# #         print(obj,cls)
# #         return self.func


# # def staticmethod(func):
# #     print(func)
# #     return StaticMethod(func)

# # class Example:
# #     name = "Example"

# #     @staticmethod
# #     def static():
# #         print ("%s static() called" % Example.name)
# #     def func(arg):
# #         print(arg)    
# # class Offspring1(Example):
# #     name = "Offspring1"

# # class Offspring2(Example):
# #     name = "Offspring2"

# #     @staticmethod
# #     def static():
# #         print ("%s static() called" % Offspring2.name)


# # Example.static() 
# # # Offspring1.static() 
# # # Offspring2.static() 






# # words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]

# # from collections import Counter 
# # word_counts = Counter(words) 
# # morewords = ['why','sim','are','you','not','looking','in','my','eyes'] 
# # for word in morewords:
# #     word_counts[word] += 1

# # change=[1,7,10]
# # money=11

# # def func(left):
# #     if(left==0):
# #         return 0
# #     ans=9999
# #     for i in range(len(change)):
# #         if(left-change[i]>=0):
# #             ans=min(func(left-change[i]),ans)

# #     return ans+1

# # print(func(money))    

# from copy import deepcopy
# arrayOfNum=[2, 3, 5, 6, 8, 10]
# givensum=10

# def func(reqSum,pos,listof
#     ans=[],ans=[]):
#     if(reqSum==0):
#         listofans.append(deepcopy(ans))
#         return
#     if pos==len(arrayOfNum):
#         return     
#     if(reqSum - arrayOfNum[pos] >= 0):
#         ans.append(arrayOfNum[pos])
#         func(reqSum - arrayOfNum[pos],pos+1,listofans) 
#         ans.pop()
#     func(reqSum,pos+1,listofans)    

# answers=[]
# func(10,0,answers)
# print(answers)

# class  Node(object):
#     """docstring for  Node"""
#     def __init__(self, data,left=None,right=None):
#         super( Node, self).__init__()
#         self.data = data
#         self.left=left
#         self.right=right

# def makeBalancedBst(root):


#     leftHeight=makeBalancedBst(root.left)
#     rightHeight=makeBalancedBst(root.right)
# import math
# def func(val):
#     if(val-math.ceil(val)==0):
#         return True
#     return False

# def giveMeLcm(x,y): # only for ints
#     a=max(x,y)
#     if(a%x==0 and a%y==0):
#         return a
#     counter=2    
#     while(True):
#         val=a*counter
#         if(val%x==0 and val%y==0):
#             return val
#         counter=counter+1    


# NoOfHitsPerSecondBySonu=int(input("enter NoOfHitsPerSecondBySonu  "))
# NoOfHitsPerSecondByMonu=int(input("enter NoOfHitsPerSecondByMonu  "))
# s=1/NoOfHitsPerSecondBySonu
# m=1/NoOfHitsPerSecondByMonu
# timeIntervalAfterWhichToCheck=1/giveMeLcm(NoOfHitsPerSecondByMonu,NoOfHitsPerSecondBySonu)
# hits=0
# NoOfBarbarians=int(input("enter No of barbarians "))
# print("Now enter the hits reqd by barbarians ")
# nthBarbarianReqHits=[]
# while(NoOfBarbarians):
#     nthBarbarianReqHits.append(int(input())) 
#     NoOfBarbarians=NoOfBarbarians-1

# maxhitsReqd=max(nthBarbarianReqHits)
# counter=1
# ans=None
# answers=[]
# while(True):
#     i=timeIntervalAfterWhichToCheck*counter    
#     if ( func(i*(1/s)) and func(i*(1/m)) ):
#         ans="both"
#         hits=hits+2
#         answers.append(ans)
#         answers.append(ans)
#     elif func(i*(1/s)):
#         ans="sonu"
#         hits=hits+1
#         answers.append(ans)
#     elif func(i*(1/m)):
#         ans="monu"
#         hits=hits+1
#         answers.append(ans)

#     if(hits>=maxhitsReqd): # 1/3 s,1/2 m,2/3 s,3/3 s,2/2 m
#         break    
#     counter=counter+1

# for i in nthBarbarianReqHits:
#     print(answers[i-1])
