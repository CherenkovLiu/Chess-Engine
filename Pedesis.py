import random

#Useless chess value
Pawn_value = 100
Knight_value = 280
Bishop_value = 320
Rook_value = 479
Queen_value = 929
King_value = 60000

#Some dictionaries
PIECE = {'Pawn':Pawn_value,'Knight':Knight_value,'Bishop':Bishop_value,'Rook':Rook_value,'Queen':Queen_value,'King':King_value}
KIND = {'1':"Pawn",'2':"Knight",'3':"Bishop",'4':"Rook",'5':"Queen",'6':"King"}

#Chess table
TABLE = [0]*10+([0]+[-10]*8+[0])*8+[0]*10

#Possible moves
global F,B,L,R
F,B,L,R = -10,10,-1,1
MOVE = {'Pawn':[F,F+F,F+L,F+R],
         'Knight':[F+F+L,F+F+R,L+L+F,L+L+B,R+R+F,R+R+B,B+B+L,B+B+R],
         'Bishop':[F+L,F+R,B+L,B+R],
         'Rook':[F,B,L,R],
         'Queen':[F,B,L,R,F+L,F+R,B+L,B+R],
         'King':[F,B,L,R,F+L,F+R,B+L,B+R]}

#Initialize the piece table
def open():
    global turn 
    turn = 1
    #Place Pawn
    
    for i in range(1,9):
        TABLE[i+20] = -1
        TABLE[i+70] = 1
        
    #Place Rook
    TABLE[11] = -4
    TABLE[18] = -4
    TABLE[81] = 4
    TABLE[88] = 4
    
    #Place Knight
    TABLE[12] = -2
    TABLE[17] = -2
    TABLE[82] = 2
    TABLE[87] = 2
    
    #Place Bishop
    TABLE[13] = -3
    TABLE[16] = -3
    TABLE[83] = 3
    TABLE[86] = 3
    
    #Place Queen and King
    TABLE[14] = -5
    TABLE[15] = -6
    TABLE[84] = 5
    TABLE[85] = 6
    
#Detect valid moves
def validmove(turn):
    if(turn % 2 == 1):
        pawnlist = [71,72,73,74,75,76,77,78]
    else:
        pawnlist = [21,22,23,24,25,26,27,28]
    move = []
    POSSIBLE_MOVE = []
    i = 0
    for k,a in enumerate(TABLE):
        POSSIBLE_MOVE = []
        if(a > 0):
            #Other kinds
            if(a != 1):
                if(a != 2 and a != 6):
                    #Several Moves
                    for gamma in MOVE[KIND[str(a)]]:
                        for y in range (1,8):
                            if(TABLE[k + y*gamma] == -10):
                                POSSIBLE_MOVE.append(gamma*y)
                            elif(-10< TABLE[k + y*gamma] < 0):
                                POSSIBLE_MOVE.append(gamma*y)
                                break
                            elif(TABLE[k + y*gamma] >= 0):
                                break
                else:
                    POSSIBLE_MOVE = MOVE[KIND[str(a)]]
            #Pawn
            elif(a == 1):
                POSSIBLE_MOVE = [F]
                if(k in pawnlist):
                    POSSIBLE_MOVE.append(F+F)
                if(0 > k + F + L > -10):
                    POSSIBLE_MOVE.append(F+L)
                if(0 > k + F + R > -10):
                    POSSIBLE_MOVE.append(F+R)
            for i in POSSIBLE_MOVE:
                if(k + i <= 99 and TABLE[k + i] < 0):
                    move.append([k,k+i])
    return move

#Move a piece
def movepiece(first,second):
    piece = TABLE[first]
    TABLE[second] = piece
    TABLE[first] = -10
    #Flip the table
    for k,i in enumerate(TABLE):
        if(i != -10 and i != 0 ):
            TABLE[k] = -i
    global F,B,turn
    F = -F
    B = -F
    turn = turn + 1

#Start the game
open()

#Useless AI that bases on some useless value to move
i = True
while(i == True):
    i = 6 in TABLE
    VALIDMOVE = validmove(turn)
    VALIDMOVE_SCORE = []
    for index,item in enumerate(VALIDMOVE):
        if(TABLE[item[1]] == -10):
            score = PIECE[KIND[str(TABLE[item[0]])]] + (-1**turn)*(item[0]-item[1])*PIECE[KIND[str(TABLE[item[0]])]]
        else:
            score = PIECE[KIND[str(TABLE[item[0]])]] + PIECE[KIND[str(abs(TABLE[item[1]]))]]
        VALIDMOVE_SCORE.append(score)
    
    best = VALIDMOVE_SCORE.index(max(VALIDMOVE_SCORE))
    move = VALIDMOVE[best]
    a = int(move[0])
    b = int(move[1])
    movepiece(a,b)

    #Stardard expression of the move
    print(chr(a - (a//10)*10 + 96)+str(9 - a//10)+chr(b - (b//10)*10 + 96)+str(9 - b//10))
if(turn%2 == 0):
    print("White win")
else:
    print("Black win")
