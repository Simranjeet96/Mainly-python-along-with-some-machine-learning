# parent-i then children-2*i+1,2*i+2


class Heap(object):
            """docstring for Heap"""
            def __init__(self):
                super(Heap, self).__init__()
                self.array=[]            
                self.lastIndex=-1
                self.key=None
            def push(self,elements,key=None):
                if not key:
                    self.key=lambda x:x
                if not self.key:
                    self.key=key

                for element in elements:
                    self.array.append(element)
                    self.lastIndex=self.lastIndex+1
                    self.heapifyUp()    

            def heapifyUp(self,pos=None):
                if not pos:
                    pos=self.lastIndex
                if pos==0:
                    return
                if self.key(self.array[pos])<self.key(self.array[(pos-1)//2]):
                    self.array[pos],self.array[(pos-1)//2]=self.array[(pos-1)//2],self.array[pos]
                    self.heapifyUp((pos-1)//2)

            def pop(self):
                if not self.array:
                    return None
                toBeRet=self.array.pop(0)
                self.lastIndex=self.lastIndex-1
                if self.array:    
                    self.array.insert(0,self.array.pop())
                    self.heapifyDown()
                return toBeRet

            def heapifyDown(self,pos=0):
                if pos>self.lastIndex:
                    return
                minimumPos=min([pos,2*pos+1,2*pos+2],key=lambda s: self.check(s))
                if minimumPos!=pos:
                    self.array[minimumPos],self.array[pos]=self.array[pos],self.array[minimumPos]
                    self.heapifyDown(minimumPos)
            def check(self,pos):
                if pos>self.lastIndex:
                    return 99999
                else:
                    return self.key(self.array[pos])    


heap=Heap()
heap.push([2,1,3],key=lambda x:-x)
heap.push([12,21,30],key=lambda x:-x)

print(heap.array)
print(heap.pop())
print(heap.pop())
print(heap.pop())


























# def wraps(func1):
#     def innerFunc(func2):
#         func2.__doc__=func1.__doc__
#         func2.__name__=func1.__name__
#         return func2
#     return innerFunc

# def outerfunc(func):
#     print("executing!!!!"+func.__name__)
#     @wraps(func)
#     def innerFunc(*args,**kwargs):
#         return func(*args,**kwargs)
#     return innerFunc    

# @outerfunc
# def say_hello(name):
#     print("hello"+name+say_hello.__name__)

# say_hello(" simranjeet singh ")










                            