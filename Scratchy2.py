# # from bs4 import BeautifulSoup
# # import requests

# # response=requests.get('http://www.stat.cmu.edu/~cshalizi/350/lectures/')
# # soup = BeautifulSoup(response.text, 'lxml')
# # i=1
# # for item in soup.find_all('a'):
# #     # print(item['href'])
# #     html=requests.get(response.url+item['href']).text
# #     soupObj=BeautifulSoup(html,'lxml')
# #     for Item in soupObj.find_all('a'):
# #         if('.pdf' in response.url+item['href']+Item['href']):
# #             with open('pdf{}.pdf'.format(i),'wb') as f:
# #                 f.write(requests.get(response.url+item['href']+Item['href']).content)
# #             i=i+1 


# # a=257
# # b=257
# # print(a is b)


# # import pickle

# # class MyClass:
# #     a=10
# #     def __init__(self):
# #         self.word="hello"

# # # obj=MyClass()        

# # with open("obj.pickle","rb") as f:
# #     obj=pickle._load(f)

# # print(obj)
# # print(obj.a)    

# # from my_module import say_goodbye
# # print(__package__)



# # def info(object, spacing=10, collapse=1):
# #     """Print methods and doc strings.
    
# #     Takes module, class, list, dictionary, or string."""
# #     methodList = [method for method in dir(object) if callable(getattr(object, method))]
# #     processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
# #     print ("\n".join(["%s %s" %
# #                       (method.ljust(spacing),
# #                        processFunc(str(getattr(object, method).__doc__)))
# #                      for method in methodList]))

# # import math
# # info(math,collapse=0)


# class Node:
#     nextref=None
#     pass
# head=Node()
# head.data=10

# # print("head.__dir__()\n",head.__dir__())
# # print()
# # print("dir(head)\n",dir(head))
# # print()
# # print("head.__dict__\n",head.__dict__)
# # print()
# # print("Node.__dict__\n",Node.__dict__)
# # print()
# # print("Node.__dir__\n",Node.__dir__)
# # print()
# # print("dir(Node)\n",dir(Node))
# # print()
# # print("Node.__name__\n",Node.__name__)
# # print()
# # print("Node().__name__\n",Node().__name__)


# print(head.__module__)    

from pytube import YouTube
 

#where to save
SAVE_PATH = "D:/" #to_do
 
#link of the video to be downloaded
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
 
try:
    #object creation using YouTube which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error") #to handle exception
 
#filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')
 
yt.set_filename('GeeksforGeeks Video') #to set the name of the file
 
#get the video with the extension and resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
    #downloading the video
    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')