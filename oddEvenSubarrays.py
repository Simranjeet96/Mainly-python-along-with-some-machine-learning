# # 1 2 3 3 2
# givenList=[1,2,1,2]
# numberOfSubArrays=0
# for i in range(len(givenList)):
#     counterOdd=0
#     counterEven=0
#     for j in range(i,len(givenList)):
#         if givenList[j]%2==0:
#             counterEven=counterEven+1
#         else:
#             counterOdd=counterOdd+1
#         if counterEven==counterOdd:
#             numberOfSubArrays=numberOfSubArrays+1

# print(numberOfSubArrays)


# givenList=[]
# turnedIntoList=[]
# for i in givenList:
#     turnedIntoList.append((i%2)*2-1)#given -1 on even and 1 on odd
# mapping={0:[-1]}
# answers=[]
# sum=0
# for i in range(len(turnedIntoList)):
#     sum=sum+turnedIntoList[i]
#     for j in mapping.get(sum,[]):
#         answers.append((j+1,i))

#     mapping.setdefault(sum,[]).append(i) 


# print(answers)


# class Person(object):
#     def __init__(self, name, ssn, address):
#         self.name = name
#         self.ssn = ssn
#         self.address = address
#     def __hash__(self):
#         return hash(self.ssn)
#     def __eq__(self, other):
#         return self.ssn == other.ssn

# bob = Person('bob', '1111-222-333', None)
# jim = Person('jim bo', '1111-222-333', 'sf bay area')

# dmv_appointments = {}
# dmv_appointments[bob] = 'tomorrow'
# print(dmv_appointments[jim])
