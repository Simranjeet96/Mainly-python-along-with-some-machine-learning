class Node(object):
    """docstring for Node"""
    def __init__(self, data,left=None,right=None):
        super(Node, self).__init__()
        self.data = data    
        self.left=left
        self.right=right


def isBST(root,upperLimit=None,lowerLimit=None):
    if upperLimit and root.data:
        for i in upperLimit:
            if(root.data>i):
                return False
    else:
        upperLimit=[]            
    if lowerLimit and root.data:
        for i in lowerLimit:
            if(root.data<i):
                return False
    else:
        lowerLimit=[]
    leftAnswer=None
    rightAnswer=None                               
    if root.left:
        upperLimit.append(root.data)
        leftAnswer=isBST(root.left,upperLimit,lowerLimit)
        upperLimit.remove(root.data)
    if root.right:
        lowerLimit.append(root.data)
        rightAnswer=isBST(root.right,upperLimit,lowerLimit)
        lowerLimit.remove(root.data)
    if root.left and root.right:
        return leftAnswer and rightAnswer
    else:
        return leftAnswer or rightAnswer         


def is_bst(node,lowerLimit=None,upperLimit=None):
    if lowerLimit is not None and node.data<lowerLimit:
        return False
    if upperLimit is not None and upperLimit<node.data:
        return False
    is_left_bst=True
    is_right_bst=True
    if node.left is not None:
        is_left_bst=is_bst(node.left,lowerLimit,node.data)
    if is_left_bst and node.right is not None:
        is_right_bst=is_bst(node.right,node.data,upperLimit)    
    return is_left_bst and is_right_bst
        






n1=Node(3)
n2=Node(10)
n3=Node(6,None,n1)
n4=Node(8,n3,n2)
n5=Node(4,None,n4)

print(is_bst(n5))        