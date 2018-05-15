class Node(object):
    """docstring for Node"""
    def __init__(self, data,left=None,right=None):
        super(Node, self).__init__()
        self.data = data    
        self.left=left
        self.right=right

def lca(root,first,second):
    if root is None:
        return (False,None)

    answerFromLeftSubtree=lca(root.left,first,second)
    answerFromRightSubtree=lca(root.right,first,second)
    
    if answerFromLeftSubtree[1] is not None: 
        return answerFromLeftSubtree
    if answerFromRightSubtree[1] is not None:    
        return answerFromRightSubtree

    if answerFromLeftSubtree[0] and answerFromRightSubtree[0]:
        return (True,root.data)
    elif answerFromLeftSubtree[0] and root.data in (first,second) or answerFromRightSubtree[0] and root.data in (first,second):
        return (True,root.data)
    elif root.data in (first,second):
        return (True,None)
    elif answerFromLeftSubtree[0] or answerFromRightSubtree[0]:
        return answerFromLeftSubtree if answerFromLeftSubtree[0] else answerFromRightSubtree
    else:
        return (False,None) 

def pathToX(root,x):
    listOfVisitedNodes=[]
    listOfVisitedNodes.append(root)
    def helper(root,listOfVisitedNodes,x):
        if root==None:
            return False
        if root.data==x:
            return True
        listOfVisitedNodes.append(root.left)    
        if not helper(root.left,listOfVisitedNodes,x):  
            listOfVisitedNodes.remove(root.left)    
            listOfVisitedNodes.append(root.right)
            if not helper(root.right,listOfVisitedNodes,x):
                listOfVisitedNodes.remove(root.right)
                return False
            else:
                return True    
        else :
            return True

    return listOfVisitedNodes if helper(root,listOfVisitedNodes,x) else []        



n1=Node(3)
n2=Node(10)
n3=Node(6,None,n1)
n4=Node(8,n3,n2)
n5=Node(4,None,n4)

for i in pathToX(n5,3):
    print(i.data)
