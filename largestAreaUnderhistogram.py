# # stack=[]
# # array=[1,2,3,2,4,2,3,4]
# # myMap=dict()
# # i=0
# # while i<len(array):   
# #     elementToBePushed=array[i]
# #     if not stack:
# #         stack.append([elementToBePushed,1])
# #     elif elementToBePushed>stack[-1][0]:
# #         stack.append([elementToBePushed,1])
# #     elif elementToBePushed<stack[-1][0]:
# #         poppedOutElement=stack.pop()
# #         value=myMap.setdefault(poppedOutElement[0],poppedOutElement[1])
# #         if(value<poppedOutElement[1]):
# #             myMap[poppedOutElement[0]]=poppedOutElement[1]
# #         topOfStack=stack[-1]
# #         topOfStack[1]=topOfStack[1]+poppedOutElement[1]
# #         i=i-1    
# #     else:
# #         topOfStack=stack[-1]
# #         topOfStack[1]+=1
# #     i=i+1    
# #     print(stack)    
# # while(stack):
# #     poppedOutElement=stack.pop()
# #     value=myMap.setdefault(poppedOutElement[0],poppedOutElement[1])
# #     if(value<poppedOutElement[1]):
# #         myMap[poppedOutElement[0]]=poppedOutElement[1]
# #     if stack:
# #         stack[-1][1]+=poppedOutElement[1]    
# # print(myMap)
    



# stack=[1,2,3,4,5,6]
# def func(stack,pos,sizeofStack):
#     if stack:
#         x=stack.pop()
#         if(pos==((sizeofStack-1)//2)):
#             return
#         func(stack,pos-1,sizeofStack)
#         stack.append(x)

# func(stack,len(stack)-1,len(stack))
# print(stack)

fh = open("hello.txt", "r")
print (fh.read())
fh.close()