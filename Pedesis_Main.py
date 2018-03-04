'''
>Update Information
2018/3/4 Add castle,add promotion,fixed some bugs,add the play function
2018/3/4 Fixed some bugs,add evaluation in one steps
>Incoming feature
Deep search
En passant move
Check detection
'''
'''
chessboard is the main board in string form
validplace is the valid coordinate in list form
'''
import random
#Piece Value
Pawn_value = 100
Knight_value = 280
Bishop_value = 320
Rook_value = 479
Queen_value = 929
King_value = 60000

#Define pieces and PST
piece = {'P':Pawn_value,'N':Knight_value,'B':Bishop_value,'R':Rook_value,'Q':Queen_value,'K':King_value}
pst = {
    'P': [   0,   0,   0,   0,   0,   0,   0,   0,
            78,  83,  86,  73, 102,  82,  85,  90,
             7,  29,  21,  44,  40,  31,  44,   7,
           -17,  16,  -2,  15,  14,   0,  15, -13,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -31,   8,  -7, -37, -36, -14,   3, -31,
             0,   0,   0,   0,   0,   0,   0,   0],
    'N': [ -66, -53, -75, -75, -10, -55, -58, -70,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
            10,  67,   1,  74,  73,  27,  62,  -2,
            24,  24,  45,  37,  33,  41,  25,  17,
            -1,   5,  31,  21,  22,  35,   2,   0,
           -18,  10,  13,  22,  18,  15,  11, -14,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -74, -23, -26, -24, -19, -35, -22, -69],
    'B': [ -59, -78, -82, -76, -23,-107, -37, -50,
           -11,  20,  35, -42, -39,  31,   2, -22,
            -9,  39, -32,  41,  52, -10,  28, -14,
            25,  17,  20,  34,  26,  25,  15,  10,
            13,  10,  17,  23,  17,  16,   0,   7,
            14,  25,  24,  15,   8,  25,  20,  15,
            19,  20,  11,   6,   7,   6,  20,  16,
            -7,   2, -15, -12, -14, -15, -10, -10],
    'R': [  35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
             0,   5,  16,  13,  18,  -4,  -9,  -6,
           -28, -35, -16, -21, -13, -29, -46, -30,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,   5,  -2, -18, -31, -32],
    'Q': [   6,   1,  -8,-104,  69,  24,  88,  26,
            14,  32,  60, -10,  20,  76,  57,  24,
            -2,  43,  32,  60,  72,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
           -14, -15,  -2,  -5,  -1, -10, -20, -22,
           -30,  -6, -13, -11, -16, -11, -16, -27,
           -36, -18,   0, -19, -15, -15, -21, -38,
           -39, -30, -31, -13, -31, -36, -34, -42],
    'K': [   4,  54,  47, -99, -99,  60,  83, -62,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,  -4, -19,  13,   0, -49,
           -55, -43, -52, -28, -51, -47,  -8, -50,
           -47, -42, -43, -79, -64, -32, -29, -32,
            -4,   3, -14, -50, -57, -18,  13,   4,
            17,  30,  -3, -14,   6,  -1,  40,  18]}
for k, table in pst.items():
    padrow = lambda row: [0] + list(x+piece[k] for x in row) + [0]
    pst[k] = sum([padrow(table[i*8:i*8+8]) for i in range(8)],[])
    pst[k] = [0]*10 + pst[k] + [0]*10

#Chessboard open-board
turn = 1
chessboard = ""
king_castle = [True,True]
queen_castle = [True,True]
validplace = []
enpassant = False
def openboard():
    global validplace
    global chessboard
    global turn
    global king_castle
    global queen_castle
    global enpassant
    enpassant = False
    king_castle = [True,True]
    queen_castle = [True,True]
    chessboard = "##########"+"#rnbqkbnr#"+"#pppppppp#"+"#        #"*4+"#PPPPPPPP#"+"#RNBQKBNR#"+"##########"
    turn = 1
    '''
    for i in range(0,91,10):
        print(chessboard[i:i+10])
        i = i + 10
    '''
    for k,i in enumerate(chessboard):
        if(i != "#"):
            validplace.append(k)

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
    global enpassant
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
            if(board[coordinate + F] == " "):
                possiblemove.append(F)
                if(coordinate in pawnlist and board[coordinate + F + F] == " "):
                    possiblemove.append(F+F)
            if(board[coordinate + F + R].islower() or (enpassant == True and board[coordinate + F + R].islower())):possiblemove.append(F + R)
            if(board[coordinate + F + L].islower() or (enpassant == True and board[coordinate + F + L].islower())):possiblemove.append(F + L)
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
                    if(coordinate + step*newmove in validplace):
                        if(board[coordinate + step*newmove] == " "):
                            possiblemove.append(newmove*step)
                        elif(board[coordinate + step*newmove].islower()):
                            possiblemove.append(newmove*step)
                            break
                        elif(board[coordinate + step*newmove].isupper()):break
                    else:break
        for possible in possiblemove:
            if(0<= coordinate + possible <=99 and board[coordinate + possible] != "#" and not(board[coordinate + possible].isupper())):
                finalmove.append([coordinate,coordinate+possible])
    return finalmove

#Move piece
def movepiece(start,end):
    if(turn % 2 == 1):
        pawnlist = [11,12,13,14,15,16,17,18]
    else:
        pawnlist = [81,82,83,84,85,86,87,88]
    term = int(0.5 + 0.5*(-1**turn))
    global chessboard
    board = chessboard
    piece = board[start]
    chessboard1 = list(board)
    #Promotion
    if(piece == "P" and end in pawnlist):
        piece = "Q"
    #Castle
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

#Play a move
def play(a):
    global nextmove
    global chessboard
    global turn
    nextmove = validmove(turn,chessboard)
    start_x = int(ord(a[0])-96)
    start_y = int(a[1])
    end_x = int(ord(a[2])-96)
    end_y = int(a[3])
    start = (9-start_y)*10+start_x
    end = (9-end_y)*10+end_x
    #Just for test
    piece = []
    print("Receive move:",[start,end],"Possible moves:",len(nextmove),"turn:",turn)
    print("All moves:",nextmove)
    for i in nextmove:
        piece.append(chessboard[i[0]])
    for i in ["P","N","B","R","Q","K"]:
        print(i,":",piece.count(i))
    if([start,end] in nextmove):
        chessboard = movepiece(start,end)
        turn = turn + 1
        for i in range(0,91,10):
            print(chessboard[i:i+10])
            i = i + 10
    else:
        return "Invalid move"

#Caluate the current table
def evaluate(board):
    value = 0
    for coordinate,i in enumerate(board):
        if(i.islower()):value = value + pst[i.upper()][coordinate]
        elif(i.isupper()):value = value - pst[i.upper()][coordinate]
    return value

#Find Current best move
def bestmove(turn,board):
    possiblemove = validmove(turn,board)
    score = []
    for move in possiblemove:
        nextboard = movepiece(move[0],move[1])
        score.append(evaluate(nextboard))
        print("Analysis move:",move,"Score:",evaluate(nextboard),"turn:",turn)
    return possiblemove[score.index(max(score))]

'''  
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
for i in range(0,20):
    print("Computer suggestion:",bestmove(turn,chessboard))
    a = input("Please enter coordinate like 'e3e4':")
    play(a)
    nextmove = validmove(turn,chessboard)
    choosedmove = bestmove(turn,chessboard)
    chessboard = movepiece(choosedmove[0],choosedmove[1])
    turn = turn + 1
    for i in range(0,91,10):
        print(chessboard[i:i+10])
        i = i + 10
    print("----------------")
print("Finished")
