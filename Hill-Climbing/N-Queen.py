import random

def Solution(board,n):
    
    print("\n{}-Queen Solution:: \n".format(n))
    for i in range(0,n):
        for j in range(0,n):
            if j==board[i]:
                print(1,end=' ')
            else:
                print(0,end=' ')
        print()        
    
def getScore(board,i,n):
    score=0
    for j in range(0,n):
        if i==j:
            continue
        if board[i]==board[j]:
            score+=1
            continue
        if abs(board[i]-board[j])==abs(i-j):
            score+=1
            continue
    return score

def getBoardScore(board,n):
    score=0
    for i in range(0,n-1):
        score+=getScore(board,i,n)
    return score

def searchBoardHeuristic(board,n):

    newBoard=[ [0]*n ]*n
    for i in range(0,n):
        newBoard[i]=board[i]
    
    ids=[i for i in range(0,n)]
    random.shuffle(ids)
    
    for i in ids:
        choice=[]
        choice.append(newBoard[i])
        temp=newBoard[i]
        score=getScore(newBoard,i,n)
        
        for j in range(0,n):
            newBoard[i]=j
            k=getScore(newBoard,i,n)
            if k==score:
                choice.append(j)
            if k<score:
                choice=[]
                choice.append(j)
                score=k
        newBoard[i] = choice[ random.randint(0,len(choice)-1) ]

    return newBoard     

def findSolutionState(board,n):
    max_itr=0
    while max_itr<2000:
        tempBoard=searchBoardHeuristic(board,n)
        for i in range(n):
            board[i]=tempBoard[i]
        if getBoardScore(board,n)==0:
            break
        max_itr+=1    
    
    for i in range(n):
        board[i]=tempBoard[i]
    return board    
                
def makeRandomBoard(board,n):
    for i in range(n):
        board[i] = random.randint(0,n-1)

def NQueenHillClimbing(n):
    board=[ [0]*n ]*n
    makeRandomBoard(board,n)
    while getBoardScore(board,n)!=0:
        makeRandomBoard(board,n)
        findSolutionState(board,n)
        
    Solution(board,n)
    
try:
    n=int(input("Enter value of N: "))
    if n<=0:
        raise ValueError
    elif n<4 and n>1:
        raise Exception
    else:
        NQueenHillClimbing(n)

except ValueError:
    print("\nerr! Please input non-negative integer for N")        
except Exception:
    print("\nThere is no solution for N = 2 and N = 3")
