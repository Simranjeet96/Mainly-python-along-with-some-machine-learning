def evaluate(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='-' or board[i][j]!=board[i][0]):
                break
        else:
            return 10
    for i in range(3):
        for j in range(3):
            if(board[j][i]=='-' or board[j][i]!=board[0][i]):
                break
        else:
            return 10

    for i in range(3):
        if(board[i][i]=='-' or board[i][i]!=board[0][0]):
            break        
    else:
        return 10

    for i in range(3):
        if(board[2-i][i]=='-' or board[2-i][i]!=board[0][2]):
            break        
    else:
        return 10

    return 0


def boardIsFull(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='-'):
                return False
    return True  


def bestMove(board,player,opponent):
    evBoard=evaluate(board)
    if(evBoard==0 and boardIsFull(board)==True):
        return 0,None,None
    if(evBoard==10 and player=='o'):
         return 10,None,None
    if(evBoard==10 and player=='*'):
        return 10,None,None 
    print(board)        
    maximum=-1000
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]=='-'):
                board[i][j]=player
                callAns=bestMove(board,opponent,player)
                if(callAns[0]>maximum):
                    maximum=callAns[0]
                    besti=i
                    bestj=j      
                board[i][j]='-'    
                        
    return -1*maximum,besti,bestj


board =[['o', '-', '-' ],
        [ '-', '*', '-' ],
        [ 'o', '-', '-' ]]

print(evaluate(board))
ans=bestMove(board,"*","o")        
print(ans[0],ans[1],ans[2])

