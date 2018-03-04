'''
Update Information
2018/3/4 Add castle
'''

#Piece Value
Pawn_value = 100
Knight_value = 280
Bishop_value = 320
Rook_value = 479
Queen_value = 929
King_value = 60000

#Define pieces
piece = {'P':Pawn_value,'N':Knight_value,'B':Bishop_value,'R':Rook_value,'Q':Queen_value,'K':King_value}
white = "PNBRQK"
black = "pnbrqk"

#Chessboard open-board
turn = 1
chessboard = ""
king_castle = [True,True]
queen_castle = [True,True]
def openboard():
    global chessboard
    global turn
    global king_castle
    global queen_castle
    king_castle = [True,True]
    queen_castle = [True,True]
    chessboard = "##########"+"#rnbqkbnr#"+"#pppppppp#"+"#        #"*4+"#PPPPPPPP#"+"#RNBQKBNR#"+"##########"
    turn = 1

#Moves for pieces
F,B,L,R = -10,10,-1,1
move = {'P':[F,F+F,F+L,F+R],
        'N':[F+F+L,F+F+R,L+L+F,L+L+B,R+R+F,R+R+B,B+B+L,B+B+R],
        'B':[F+L,F+R,B+L,B+R],
        'R':[F,B,L,R],
        'Q':[F,B,L,R,F+L,F+R,B+L,B+R],
        'K':[F,B,L,R,F+L,F+R,B+L,B+R]}

#Valid moves
def validmove(turn,board):
    #Decide how to move
    global F,B
    F = 10*((-1)**turn)
    B = -10*((-1)**turn)
    term = int(0.5 + 0.5*(-1**turn))
    #Decide if the pawn could move two steps
    if(turn % 2 == 1):
        pawnlist = [71,72,73,74,75,76,77,78]
    else:
        pawnlist = [21,22,23,24,25,26,27,28]
    finalmove = []
    for coordinate,piece in enumerate(board):
        possiblemove = []
        #Pawn move
        if(piece == "P"):
            possiblemove = [F]
            if(coordinate in pawnlist):possiblemove.append(F+F)
            elif(board[coordinate + F + R].islower()):possiblemove.append(F+R)
            elif(board[coordinate + F + L].isupper()):possiblemove.append(F+L)
        #Knight and King
        elif(piece == "N" or piece == "K"):
            possiblemove = move[piece]
            #Castle
            if(piece == "K"):
                if(queen_castle[term] == True and board[coordinate + L] == " " and board[coordinate + L*2] == " " and board[coordinate + L*3] == " "):
                    possiblemove.append(-2)
                if(king_castle[term] == True and board[coordinate + R] == " " and board[coordinate + R*2] == " "):
                    possiblemove.append(2)
        #Bishop,Queen and Rook for several steps
        elif(piece != "#" and piece != " " and piece.isupper()):
            for newmove in move[piece]:
                for step in range (1,8):
                    if(coordinate + step*newmove <= len(board)-1):
                        if(board[coordinate + step*newmove] == " "):
                            possiblemove.append(newmove*step)
                        elif(board[coordinate + step*newmove].islower()):
                            possiblemove.append(newmove*step)
                            break
                        elif(board[coordinate + step*newmove].isupper()):
                            break
        for possible in possiblemove:
            if(0<= coordinate + possible <=99 and board[coordinate + possible] != "#" and not(board[coordinate + possible].isupper())):
                finalmove.append([coordinate,coordinate+possible])
    return finalmove

#Move piece
def movepiece(start,end):
    term = int(0.5 + 0.5*(-1**turn))
    global chessboard
    board = chessboard
    piece = board[start]
    chessboard1 = list(board)
    if(piece == "R" and start - (start//10)*10 == 1 and queen_castle[term] == True):queen_castle[term] = False
    elif(piece == "R" and start - (start//10)*10 == 8 and king_castle[term] == True):king_castle[term] = False
    elif(piece == "K"):
        if(start - (start//10)*10 == 5):
            if(end - start == 2):
                chessboard1[start + 1] = "R"
                chessboard1[start + 3] = " "
            elif(end - start == -2):
                chessboard1[start - 1] = "R"
                chessboard1[start - 4] = " "
        queen_castle[term] = False
        king_castle[term] = False       
    chessboard1[end] = piece
    chessboard1[start] = " "
    board = ''.join(chessboard1)
    board = board.swapcase()
    return board

'''
def treegeneration(board,turn,depth):
    totalmoves = []
    currentmoves = []
    futuremoves = []
    for i in range(0,depth):  
def checkdetection(start,end):
    global turn
    global chessboard
    board = chessboard
    check = False
    kingcoordinate = chessboard.index("K")
    #See if you are checkmated
    mymove = validmove(turn)
    incheckmove = []
    faketurn = turn
    for moves in mymove:
        faketurn = turn
        check = False
        chessboard = movepiece(moves[0],moves[1])
        faketurn = faketurn + 1
        shiftturn()
        enemymove = validmove(faketurn)
        for enemymoves in enemymove:
            if(kingcoordinate == enemymoves[1]):
                check = True
                break
        if(check == False):incheckmove.append(moves)
    print(incheckmove)
    chessboard = board
    if(len(incheckmove)!=0):checkmate = False
    else:return "Checkmate"
    if([start,end] not in incheckmove):return "Invalid"
    else:return "Valid"
'''
openboard()

#How to move?
#1.generate validmove
#2.detect checkmate
#3.detect validmove
#4.movepiece()
#5.turn +1

'''
for i in range (0,1):
    nextmove = validmove(turn,chessboard)
    chessboard = movepiece(74,54)
    turn = turn + 1

    nextmove = validmove(turn,chessboard)
    chessboard = movepiece(25,45)
    turn = turn + 1

    nextmove = validmove(turn,chessboard)
    chessboard = movepiece(82,61)
    turn = turn + 1

    nextmove = validmove(turn,chessboard)
    chessboard = movepiece(45,55)
    turn = turn + 1

    nextmove = validmove(turn,chessboard)
    chessboard = movepiece(83,56)
    turn = turn + 1

    nextmove = validmove(turn,chessboard)
    chessboard = movepiece(55,65)
    turn = turn + 1

    nextmove = validmove(turn,chessboard)
    chessboard = movepiece(84,74)
    turn = turn + 1

    chessboard = movepiece(21,31)
    turn = turn + 1

    nextmove = validmove(turn,chessboard)
    print(nextmove)
    chessboard = movepiece(85,83)
    turn = turn + 1
    for i in range(0,91,10):
        print(chessboard[i:i+10])
        i = i + 10
    print(king_castle,queen_castle,turn)
    '''