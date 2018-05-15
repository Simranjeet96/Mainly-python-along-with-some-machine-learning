# # import pyperclip
# # prev=''
# # while(True):
# #     sentence=pyperclip.paste()
# #     if(sentence and prev!=sentence):
# #         prev=sentence
# #         print(eval('a=[]'))


# class User(object):
#     """docstring for User"""
#     def __init__(self, arg):
#         super(User, self).__init__()
#         self.arg = arg
# # print(User(1).__getattribute__())
# # print(getattr(User(1),'p',None))
# # sorted([User(1),User(2),User(3)],key=lambda x: getattr(x,'arg',None))        
# x=User(1)
# for attrname in dir(x):
#     print('x.{} = {!r}'.format(attrname, getattr(x, attrname),getattr(x, attrname)))


# # def trie(root,string):
# #  for i in string:
# #   root=root.setdefault(i,{})
# # root={}
# # trie(root,'simran') 
# # trie(root,'simcard') 

# # print(root['s']['i']['m']['r']['a']['n'] == {})
