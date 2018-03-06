#Piece Value
Pawn_value = 100
Knight_value = 280
Bishop_value = 320
Rook_value = 479
Queen_value = 929
King_value = 60000

#Table value
piecewhite = {'P':Pawn_value,'N':Knight_value,'B':Bishop_value,'R':Rook_value,'Q':Queen_value,'K':King_value}
pieceblack = {'p':Pawn_value,'n':Knight_value,'b':Bishop_value,'r':Rook_value,'q':Queen_value,'k':King_value}
pstwhite = {'P':[],'N':[],'B':[],'R':[],'Q':[],'K':[]}
pstblack = {'p':[],'n':[],'b':[],'r':[],'q':[],'k':[]}
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
    padrow = lambda row: [0] + list(x+piecewhite[k] for x in row) + [0]
    temp = []
    for i in range(8):
        temp = temp + padrow(table[i*8:i*8+8])
    pstwhite[k] = [0]*10 + temp + [0]*10
    pstblack[k.lower()] = [0]*10 + temp + [0]*10
for k,table in enumerate(pstblack):
    pstblack[table] = [-j for j in pstblack[table]]

#Open-board variables
color = "white"
chessboard = ""
king_castle = [True,True]
queen_castle = [True,True]
validplace = []
enpassant = False
previous_move = []
searchnum = 0

#Move of the piece
F,B,L,R = -10,10,-1,1
move = {'P':[F,F+F,F+L,F+R],
        'N':[F+F+L,F+F+R,L+L+F,L+L+B,R+R+F,R+R+B,B+B+L,B+B+R],
        'B':[F+L,F+R,B+L,B+R],
        'R':[F,B,L,R],
        'Q':[F,B,L,R,F+L,F+R,B+L,B+R],
        'K':[F,B,L,R,F+L,F+R,B+L,B+R],
        'p':[F,F+F,F+L,F+R],
        'n':[F+F+L,F+F+R,L+L+F,L+L+B,R+R+F,R+R+B,B+B+L,B+B+R],
        'b':[F+L,F+R,B+L,B+R],
        'r':[F,B,L,R],
        'q':[F,B,L,R,F+L,F+R,B+L,B+R],
        'k':[F,B,L,R,F+L,F+R,B+L,B+R]}

#Openboard
def openboard():
    print("==Welcome to use the Chess-Engine 'Pedesis-New generation'==")
    print("==Developed by CherenkovLiu and Tiansmart==")
    global validplace
    global chessboard
    global king_castle
    global queen_castle
    global enpassant
    enpassant = False
    king_castle = [True,True]
    queen_castle = [True,True]
    chessboard = "##########"+"#rnbqkbnr#"+"#pppppppp#"+"#        #"*4+"#PPPPPPPP#"+"#RNBQKBNR#"+"##########"
    for i in range(0,91,10):
        print(chessboard[i:i+10])
        i = i + 10
    for k,i in enumerate(chessboard):
        if(i != "#"):
            validplace.append(k)

#Generate valid moves
def validmove(board,color):
    #Decide how to move
    global F,B
    global enpassant
    if(color == "white"):
          F,B,L,R,term = -10,10,-1,1,0
          pawnlist = [71,72,73,74,75,76,77,78]
    elif(color == "black"):
          F,B,L,R,term = 10,-10,1,-1,1
          pawnlist = [21,22,23,24,25,26,27,28]
    finalmove = []
    for coordinate,piece in enumerate(board):
        possiblemove = []
        #Pawn move
        if((piece == "P" and color == "white") or (piece == "p" and color == "black")):
            if(board[coordinate + F] == " "):
                possiblemove.append(F)
                if(coordinate in pawnlist and board[coordinate + F + F] == " "):
                    possiblemove.append(F+F)
            if(board[coordinate + F + R].islower() or (enpassant == True and board[coordinate + F + R].islower())):possiblemove.append(F + R)
            if(board[coordinate + F + L].islower() or (enpassant == True and board[coordinate + F + L].islower())):possiblemove.append(F + L)
        #Knight and King
        elif(((piece == "N" or piece == "K") and color == "white") or ((piece == "n" or piece == "k") and color == "black")):
            possiblemove = move[piece]
            #Castle
            if((piece == "K" and color == "white") or (piece == "k" and color == "black")):
                if(queen_castle[term] == True and board[coordinate + L] == " " and board[coordinate + L*2] == " " and board[coordinate + L*3] == " "):
                    possiblemove.append(-2)
                if(king_castle[term] == True and board[coordinate + R] == " " and board[coordinate + R*2] == " "):
                    possiblemove.append(2)
        #Bishop,Queen and Rook for several steps
        elif((piece != "#" and piece != " " and piece.isupper() and color == "white") or (piece != "#" and piece != " " and piece.islower() and color == "black")):
            for newmove in move[piece]:
                for step in range (1,8):
                    if(coordinate + step*newmove in validplace):
                        if(board[coordinate + step*newmove] == " "):
                            possiblemove.append(newmove*step)
                        elif((board[coordinate + step*newmove].islower() and color == "white") or (board[coordinate + step*newmove].isupper() and color == "black")):
                            possiblemove.append(newmove*step)
                            break
                        elif((board[coordinate + step*newmove].isupper() and color == "white") or (board[coordinate + step*newmove].islower() and color == "black")):
                            break
                    else:break
        for possible in possiblemove:
            if(0<= coordinate + possible <=99 and board[coordinate + possible] != "#" and ((not(board[coordinate + possible].isupper()) and color == "white") or (not(board[coordinate + possible].islower()) and color == "black"))):
                finalmove.append([coordinate,coordinate+possible])
    return finalmove

#Move a piece
def movepiece(board,color,start,end):
    if(color == "white"):
        pawnlist = [11,12,13,14,15,16,17,18]
        term = 0
    else:
        pawnlist = [81,82,83,84,85,86,87,88]
        term = 1
    piece = board[start]
    tempboard = list(board)
    #Promotion
    if(piece in "pP" and end in pawnlist):
        if(color == "white"):piece = "Q"
        elif(color == "black"):piece = "q"
    #Castle
    if(piece in "Rr" and start - (start//10)*10 == 1 and queen_castle[term] == True):queen_castle[term] = False
    elif(piece in "Rr" and start - (start//10)*10 == 8 and king_castle[term] == True):king_castle[term] = False
    elif(piece in "kK"):
        if(start - (start//10)*10 == 5):
            if(end - start == 2):
                if(color == "white"):tempboard[start + 1] = "R"
                elif(color == "black"):tempboard[start + 1] = "r"
                tempboard[start + 3] = " "
            elif(end - start == -2):
                if(color == "white"):tempboard[start - 1] = "R"
                elif(color == "black"):tempboard[start - 1] = "r"
                tempboard[start - 4] = " "
        queen_castle[term] = False
        king_castle[term] = False
    #Now move
    tempboard[end] = piece
    tempboard[start] = " "
    return ''.join(tempboard)

#Caluate the current value of the table
def evaluate(board):
    value = 0
    for coordinate,item in enumerate(board):
        if(item.islower()):value = value + pstblack[item][99 - coordinate]
        elif(item.isupper()):value = value + pstwhite[item][coordinate]
    return value

#Find Current bestmove
def findmove(board,color,depth):
    avaliablemove = validmove(board,color)
    nextboard = []
    score = []
    for pmove in avaliablemove:
        nextboard = movepiece(board,color,pmove[0],pmove[1])
        if(color == "white"):nextcolor = "black"
        else:nextcolor = "white"
        score.append(searchmove(nextboard,nextcolor,depth,-9999,9999))
        print("Move:",pmove,"Score:",score[-1])
    if(color == "white"):return avaliablemove[score.index(max(score))]
    elif(color == "black"):return avaliablemove[score.index(min(score))]

#Deep search
def searchmove(board,color,depth,alpha,beta):
    global searchnum
    searchnum = searchnum + 1
    nextboard = board
    currentcolor = color
    if(depth == 0):
        return evaluate(nextboard)
    elif(currentcolor == "white"):
        bestmove = -999999
        for pmove in validmove(nextboard,currentcolor):
            nextboard = movepiece(nextboard,currentcolor,pmove[0],pmove[1])
            currentcolor = "black"
            bestmove = max(bestmove,searchmove(nextboard,currentcolor,depth - 1,alpha,beta))
            nextboard = board
            currentcolor = "white"
            alpha = max(alpha,bestmove)
            if(beta <= alpha):
                return bestmove
        return bestmove
    elif(currentcolor == "black"):
        bestmove = 999999
        for pmove in validmove(nextboard,currentcolor):
            nextboard = movepiece(nextboard,currentcolor,pmove[0],pmove[1])
            currentcolor = "white"
            bestmove = min(bestmove,searchmove(nextboard,currentcolor,depth - 1,alpha,beta))
            nextboard = board
            currentcolor = "black"
            beta = min(beta,bestmove)
            if(beta <= alpha):
                return bestmove
        return bestmove

#Ok this is the main program
openboard()
for turn in range(0,10):
    searchnum = 0
    if(len(validmove(chessboard,color))>=25):
        searchdepth = 3
        print(">Too many moves,searching fast now")
    else:
        searchdepth = 4
        print(">Use more layers")
    makemove = findmove(chessboard,color,searchdepth)
    chessboard = movepiece(chessboard,color,makemove[0],makemove[1])
    print(evaluate(chessboard))
    if(color == "white"):color = "black"
    elif(color == "black"):color = "white"
    for i in range(0,91,10):
        print(chessboard[i:i+10])
        i = i + 10

