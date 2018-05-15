class Node(object):
    """docstring for Node"""
    def __init__(self, data,left=None,right=None,height=None):
        super(Node, self).__init__()
        self.data = data
        self.left=left
        self.right=right
        self.height=height

# def leftMostNodeOf(root):
#     assert(root is not None)
#     if root.left is None:
#         return root
#     return leftMostNodeOf(root.left)

# def rightMostNodeOf(root):
#     assert(root is not None)
#     if root.right is None:
#         return root
#     return rightMostNodeOf(root.right)

# # def linearizeBST(root):
# #     head=None 
# #     def helper(root):
# #         nonlocal head
# #         if root.left:
# #             helper(root.left)
# #         if root.left is not None:
# #             rightMostNodeOf(root.left).right=root
# #             root.left=None
# #         elif head is None:
# #             head=root
# #         if root.right is not None:        
# #             temp=root.right
# #             root.right=leftMostNodeOf(root.right)
# #         if root.right:
# #             helper(temp)    
# #     helper(root)
# #     return head

# # # 9
# # # 6 27
# # # 5 8
# # # 20 29
# # # -1 -1
# # # 7 -1
# # # -1 24
# # # -1 33
# # # -1 -1
# # # -1 -1
# # # -1 -1

# def MakeBinaryTreeFromInputBreadthWise():
#     root=Node(int(input("enter root ")))
#     queue=[root]
#     while queue:
#         current=queue.pop(0)
#         print("enter both children of",current.data,"with space between them")
#         leftdata,rightdata=input().split(' ')
#         leftdata=int(leftdata)
#         rightdata=int(rightdata)
#         if leftdata!=-1:
#             current.left=Node(leftdata)
#             queue.append(current.left)
#         if rightdata!=-1:
#             current.right=Node(rightdata)
#             queue.append(current.right)
#     return root

def PrintBinaryTreeLevelWise(root):
    queue=[root]
    while queue :
        current=queue.pop(0)
        print(current.data,"and its height is ",current.height)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# def MakeBstTreeToVine(root):
#     head=None
#     def linearizeBST(root):
#         nonlocal head
#         if root.left:
#             rightMostNode=rightMostNodeOf(root.left)
#             temp=root.left
#             root.left=rightMostNode
#             linearizeBST(temp)
#             rightMostNode.right=root
#         elif head is None:
#             head=root
#         if root.right:
#             leftMostNode=leftMostNodeOf(root.right)        
#             temp=root.right
#             root.right=leftMostNode
#             linearizeBST(temp)
#             leftMostNode.left=root
#     linearizeBST(root)
#     return head
# root=MakeBinaryTreeFromInputBreadthWise()                
# # PrintBinaryTreeLevelWise(root)
# root=MakeBstTreeToVine(root)
# print(root.data)        
# while(root.right):
#     print(root.right.data)
#     root=root.right


# 50
# 17 76
# 9 23
# 54 -1
# -1 14
# 19 -1
# -1 72
# 12 -1
# -1 -1
# 67 -1
# -1 -1
# -1 -1

def RRrotation(root):
    print('RR')
    temp=root.right.left
    Newroot=root.right
    Newroot.left=root
    root.right=None
    if temp:
        InsertIntoBalancedBst(Newroot,nodeToBeInsert=temp)
    else:
        root.height=root.height-1
    return Newroot

def RLrotation(root):
    print('RL')
    currentRoot=LLrotation(root.right)
    root.right=currentRoot
    return RRrotation(root)

def LLrotation(root):
    print("LL")
    temp=root.left.right
    Newroot=root.left
    Newroot.right=root
    root.left=None
    if temp:
        InsertIntoBalancedBst(Newroot,nodeToBeInsert=temp)
    else:
        root.height=root.height-1
    return Newroot


def LRrotation(root):
    print("LR")
    currentRoot=RRrotation(root.left)
    root.left=currentRoot
    return LLrotation(root)

def InsertIntoBalancedBst(root,element=None,nodeToBeInsert=None):    
    if root is None:
        if not nodeToBeInsert:
            root=Node(element,height=1)
            return root
        else:
            root=nodeToBeInsert
            return root    
    if nodeToBeInsert:    
        element=nodeToBeInsert.data
    if element<root.data:
        leftSubtreeRoot=InsertIntoBalancedBst(root.left,element,nodeToBeInsert)
        root.left=leftSubtreeRoot
    else:
        rightSubtreeRoot=InsertIntoBalancedBst(root.right,element,nodeToBeInsert)    
        root.right=rightSubtreeRoot

    if root.left:
        heightOfLeftSubtree=root.left.height
    else:
         heightOfLeftSubtree=0
    if root.right:
        heightOfRightSubtree=root.right.height
    else:
         heightOfRightSubtree=0

    if abs(heightOfLeftSubtree - heightOfRightSubtree)<=1:
        root.height=1+max(heightOfLeftSubtree,heightOfRightSubtree)
        return root
    elif heightOfRightSubtree > heightOfLeftSubtree:
        if root.right.right and root.right.left:
            if (root.right.height == root.right.right.height + 1):
                # do RR rotation
                return RRrotation(root)
            else:
                # do RL rotation    
                return RLrotation(root)    
        elif root.right.right:
            # do RR
            return RRrotation(root)
        else:       
            # do RL
            return RLrotation(root)           
    else:
        if root.left.left and root.left.right:
            if root.left.height== 1 + root.left.left.height:
                # do LL rotation
                return LLrotation(root)
            else:
                # LR rotation
                return LRrotation(root)
        elif root.left.left:
            # do LL rotation
            return LLrotation(root)
        else:
            # do LR rotation
            return LRrotation(root) 

root=None
while(True):
    element=int(input())
    if element!=-1:
        root=InsertIntoBalancedBst(root,element)
        print(PrintBinaryTreeLevelWise(root))
        print('*'*20)
    else:
        break    





