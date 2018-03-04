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
def openboard():
    global chessboard
    global turn
    chessboard = "##########"+"#rnbqkbnr#"+"#pppppppp#"+"          "*4+"#PPPPPPPP#"+"#RNBQKBNR#"+"##########"
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
    if(turn % 2 == 1):
        pawnlist = [71,72,73,74,75,76,77,78]
    else:
        pawnlist = [21,22,23,24,25,26,27,28]
    finalmove = []
    for coordinate,piece in enumerate(board):
        possiblemove = []
        if(piece == "P"):
            possiblemove = [F]
            if(coordinate in pawnlist):possiblemove.append(F+F)
            elif(board[coordinate + F + R].islower()):possiblemove.append(F+R)
            elif(board[coordinate + F + L].isupper()):possiblemove.append(F+L)
        elif(piece == "N" or piece == "K"):
            possiblemove = move[piece]
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
    global chessboard
    board = chessboard
    piece = board[start]
    chessboard1 = list(board)
    chessboard1[end] = piece
    chessboard1[start] = " "
    board = ''.join(chessboard1)
    board = board.swapcase()
    return board

def shiftturn():
    global F,B
    F = 10*((-1)**turn)
    B = -10*((-1)**turn)

def treegeneration(board,turn,depth):
    totalmoves = []
    currentmoves = []
    futuremoves = []
    for i in range(0,depth):
        



#See if you are checked
'''Experiment Function
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
#6.shiftturn()

nextmove = validmove(turn,chessboard)
chessboard = movepiece(74,54)
turn = turn + 1
shiftturn()

nextmove = validmove(turn,chessboard)
chessboard = movepiece(25,45)
turn = turn + 1
shiftturn()

nextmove = validmove(turn,chessboard)
print(nextmove)

