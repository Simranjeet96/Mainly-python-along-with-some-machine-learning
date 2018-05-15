
# import sys
# array=[1, 3, 4, 0, 4]
# reqSum=sum(array)/3
# if int(reqSum)!=reqSum:
#     print(-1)
#     sys.exit(0)
# I=-1
# J=-1
# i=0
# j=0
# currentSum=0
# while(i<len(array)):
#     currentSum=currentSum+array[i]
#     if currentSum==reqSum:
#         I=i
#         break    
#     else:
#         i=i+1
# if I!=-1:
#     j=i+1
#     currentSum=0
#     while(j<len(array)):
#         currentSum=currentSum+array[j]
#         if currentSum==reqSum:
#             J=j
#             break    
#         else:
#             j=j+1
# else:
#     print(-1)
#     sys.exit(0)

# if J==-1:
#     print(-1)
#     sys.exit(0)
# else:
#     print(I,J)


# def lcs(string1,string2):
#     assert(len(string1)>=1 and len(string2)>=1)
#     if string1[0] == string2[0]:
#         if len(string1)>1 and len(string2)>1:
#             return string1[0] + lcs(string1[1:],string2[1:])
#         else:
#             return string1[0]
#     else:
#         if len(string1)>1:
#             ans1=lcs(string1[1:],string2)
#             ans1len = len(ans1)
#         else:
#             ans1=''
#             ans1len = 0
#         if len(string2)>1:
#             ans2=lcs(string1,string2[1:])
#             ans2len = len(ans2)     
#         else:
#             ans2=''
#             ans2len=0
#         if ans1len>ans2len:
#             return ans1
#         else:
#             return ans2     

# # print(lcs('simranjeet','savindermanjeet'))

# def lrs(string):

#     def helper(string1,string2,pos1=0,pos2=0):

#         if string1[0]==string2[0]:
#             if pos1==pos2:
#                 return helper(string1,string2[1:],pos1,pos2+1) if len(string2)>1 else ''
#             else:
#                 return string1[0] + helper(string1[1:],string2[1:]) if len(string1)>1 and len(string2)>1 else ''    
    
#         ans1=helper(string1,string2[1:],pos1,pos2+1) if len(string2)>1 else ''
#         ans2=helper(string1[1:],string2,pos1+1,pos2) if len(string1)>1 else ''

#         return max((ans1,ans2),key=lambda s:len(s))

#     return helper(string,string)

# print(lrs('AABEBCDD'))

# def lps(string):
    
#     if string[0]==string[-1]:
#         if len(string)==1:
#             return string[0]
#         if len(string)==2:
#          return string[0]+string[-1]
#         return string[0]+lps(string[1:-1])+string[-1]

#     ans1=lps(string[1:]) if len(string)>1 else string[0]
#     ans2=lps(string[:-1]) if len(string)>1 else string[0]
#     return max((ans1,ans2),key=lambda s: len(s))

# print(lps('GEEKSFORGEEKS'))


def func(string,callno=0,temp=''):
    
    if len(string)==0 and callno==3:
        print(temp.strip())
        return 
    for i in range(len(string)):
        temp=temp+' '+string[:i+1]
        func(string[i+1:],callno+1,temp)
        index=temp.rfind(' ')
        temp=temp[:index]
maximum=(9999,)
def function(givenList,callno=0,temp=None):
    global maximum
    if callno>2:
        return
    if len(givenList)==0:
        if maximum[0]>max(temp):
            maximum=(max(temp),list(temp))
        return 
    for i in range(len(givenList)):
        temp.append(sum(givenList[:i+1]))
        function(givenList[i+1:],callno+1,temp)
        temp.pop(-1)

# function([10,10,10,10],temp=[])
# print(maximum)

def functoo(var):
    def helper():
        nonlocal var
        print(var)
    helper()
        

functoo(1)        















