inputMatrix=["0 0 1 1 1 1 1 0 0 0".split(),"0 0 0 0 1 0 0 0 0 0".split(),"1 1 1 1 1 0 0 0 0 0".split(),"0 0 0 0 1 0 0 0 0 0".split(),"1 0 1 1 1 1 0 0 0 0".split(),"1 0 1 0 1 1 0 0 0 0".split(),"1 0 1 1 1 1 0 1 1 1".split(),"1 1 1 1 1 1 0 1 0 0".split(),"0 0 0 0 0 1 1 1 0 0".split()]#input matrix will have 1 where it is path and 0 where it is wall
for i in inputMatrix:
	print(i)

print()
print()
def no_of_dirnToGo(currX,currY,travelled):#it will return list like[u,d,l]it also takes into account is it travelled and also is it possible to go 
	directions=[]
	
	if(currY-1>=0 and inputMatrix[currY-1][currX]=='1' and (currX,currY-1) not in travelled):
			directions.append('u')
	if(currX+1<len(inputMatrix[0]) and inputMatrix[currY][currX+1]=='1' and (currX+1,currY) not in travelled):
			directions.append('r')
	if(currY+1<len(inputMatrix) and inputMatrix[currY+1][currX]=='1' and (currX,currY+1) not in travelled):
		directions.append('d')
	if(currX-1>=0 and inputMatrix[currY][currX-1]=='1' and (currX-1,currY) not in travelled):
			directions.append('l')
			
	return directions		


answers=[]
def func(path,currX,currY,DestX,DestY,travelled):#path='',travelled=[] for calling function
	global answers
	if(currX==DestX and currY==DestY):
		answers.append(path)
		return 
	if(no_of_dirnToGo(currX,currY,travelled)==0):
		return 
	else:		
		for i in no_of_dirnToGo(currX,currY,travelled):

			if(i=='u'):	
				path=path+i
				travelled.append((currX,currY-1))
				func(path,currX,currY-1,DestX,DestY,travelled)
				path=path[:-1]
				travelled.remove((currX,currY-1))	
			elif(i=='r'):
				path=path+i
				travelled.append((currX+1,currY))
				func(path,currX+1,currY,DestX,DestY,travelled)
				path=path[:-1]	
				travelled.remove((currX+1,currY))
			elif(i=='d'):
				path=path+i
				travelled.append((currX,currY+1))
				func(path,currX,currY+1,DestX,DestY,travelled)
				path=path[:-1]	
				travelled.remove((currX,currY+1))
			elif(i=='l'):
				path=path+i
				travelled.append((currX-1,currY))
				func(path,currX-1,currY,DestX,DestY,travelled)
				path=path[:-1]	
				travelled.remove((currX-1,currY))
		return 		

path=''
travelled=[]

currX,currY,DestX,DestY=input('enter start and destination').split()
currX=int(currX)
currY=int(currY)
DestX=int(DestX)
DestY=int(DestY)
func(path,currX,currY,DestX,DestY,travelled)
length=len(answers[0])
value=0

for i in answers[1:]:

	if len(i)<length:
		length=len(i)
		value=i
print(value)	
input('bye')