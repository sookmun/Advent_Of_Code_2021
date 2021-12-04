def check(board,position):
    row=position[0]
    col=position[1]
    winRow=True
    winCol=True
    for a in range(5):
        if winRow==False and winCol==False:
            return False
        if winRow!=False:
            if board[row][a]!=True:
                winRow=False
            else:

                winRow=True
        if winCol !=False:
            if board[a][col]!=True:
                winCol=False

            else:
                winCol=True

    if winRow or winCol:
        return True
    else:
        return False


def find(board,number):

    for row in range(5):
        for col in range(5):
            if board[row][col]==number:
                board[row][col]=True
                return number,(row,col)
    return 0,None

def bingo():
    draws,allBoard=read()
    index=0

    draws=draws.split(",")
    while index<= len(draws):
        for round in range(5):
            index+=1
            if index>=len(draws):
                break
            for boardnum in range(len(allBoard)):
                winNum,position=find(allBoard[boardnum],draws[index])
                if position!=None:
                    flag=check(allBoard[boardnum],position)
                    if flag:
                        showmeBoard(allBoard[boardnum])
                        sumFinal(allBoard[boardnum],draws[index])
                        return


def sumFinal(board,finalnum):
    sum=0
    for line in board:
        for item in line:
            if item !=True:
                sum+=int(item)
    print("Sum of Unmarked:",sum)
    ans=sum*int(finalnum)
    print("ans:",ans)


def read():
    with open('day4_input.txt') as file:
        file=file.readlines()
        draws=file[0].strip('\n')

        newBoard=[]
        allBoard=[]
        for index in range(2,len(file)):
            if file[index]=='\n':
                allBoard.append(newBoard)
                newBoard=[]
            else:
                line=file[index].strip('\n')
                line=line.split()
                newBoard.append(line)
        allBoard.append(newBoard)
        return draws,allBoard

def bingoPartTwo():
    draws, allBoard = read()
    winner=[]
    lastwinDraw=0
    index = 0

    draws = draws.split(",")
    while index <= len(draws):
        if len(allBoard)==0:
            break
        index += 1
        pointer=0
        lastwinDraw=0
        while pointer< len(allBoard):
            # print("pointer:",pointer)
            winNum, position = find(allBoard[pointer], draws[index])
            if position != None:
                flag = check(allBoard[pointer], position)
                if flag:
                    winner=allBoard.pop(pointer)
                    lastwinDraw=draws[index]
                    pointer-=1

            pointer+=1

    sumFinal(winner, lastwinDraw)
    showmeBoard(winner)

def showme(lst):
    for x in lst:
        if type(x)==list:
            for row in x:
                print(row)
            print(" ")
        else:
            print(x)
def showmeBoard(lst):
    for x in lst:
        print(x)


if __name__ == '__main__':
    bingo()
    # bingoPartTwo()
    # test=[[1,2,3,4,(4,True)],
    #       [6,79,8,9,(4,True)],
    #       [46, 7, 84, 39, (4,True)],
    #       [56, 17, 18, 29, (4,True)],
    #       [(4,True), 9, (4,True), (4,True), (4,True)]]
    # c=check(test,(4,4))
    # print(c)
