import os
from termcolor import colored
os.system('color')
colors = {"0": "white", "1": "blue", "2": "green", "3": "red", " ": "white"}
board = [[["0u ", "0p 0", "   ", "   ", "1p 0", "1k "], ["0r ", "0p 0", "   ", "   ", "1p 0" ,"1b "], ["0Q ", "0p 0", "   ", "   ", "1p 0" ,"1K "], ["0K ", "0p 0", "   ", "   ", "1p 0" ,"1Q "] ,["0b ", "0p 0", "   ", "   ", "1p 0" ,"1r "], ["0k ", "0p 0", "   ", "   ", "1p 0" ,"1u "]],[["0p 1", "0p 2", "   ", "   ", "1p 2", "1p 1"], ["0p 1", "0p 2", "   ", "   ", "1p 2", "1p 1"], ["0p 1", "0p 2", "   ", "   ", "1p 2", "1p 1"], ["0p 1", "0p 2", "   ", "   ", "1p 2", "1p 1"], ["0p 1", "0p 2", "   ", "   ", "1p 2", "1p 1"], ["0p 1", "0p 2", "   ", "   ", "1p 2", "1p 1"]],[["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "]], [["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   "]], [["2p 1", "2p 2", "   ", "   ", "3p 2", "3p 1"], ["2p 1", "2p 2", "   ", "   ", "3p 2", "3p 1"], ["2p 1", "2p 2", "   ", "   ", "3p 2", "3p 1"], ["2p 1", "2p 2", "   ", "   ", "3p 2", "3p 1"], ["2p 1", "2p 2", "   ", "   ", "3p 2", "3p 1"], ["2p 1", "2p 2", "   ", "   ", "3p 2", "3p 1"]], [["2u ", "2p 0", "   ", "   ", "3p 0", "3k "], ["2r ", "2p 0", "   ", "   ", "3p 0" ,"3b "], ["2Q ", "2p 0", "   ", "   ", "3p 0" ,"3K "], ["2K ", "2p 0", "   ", "   ", "3p 0" ,"3Q "] ,["2b ", "2p 0", "   ", "   ", "3p 0" ,"3r "], ["2k ", "2p 0", "   ", "   ", "3p 0" ,"3u "]]]
def getMoveVectors(accepted_zeros):
    zeros = 0
    move_lines = []
    for dx in [0, -1, 1]:
        if dx == 0: zeros += 1
        elif dx == -1: zeros -= 1
        for dy in [0, -1, 1]:
            if dy == 0: zeros += 1
            elif dy == -1: zeros -= 1
            for dz in [0, -1, 1]:
                if dz == 0: zeros += 1
                elif dz == -1: zeros -= 1
                if zeros in accepted_zeros:
                    move_lines.append([dx, dy, dz])
    return move_lines
def getFigureMoves(x, y, z):
    #x, y, z = z, y, x
    figureChar = board[x][y][z]
    if figureChar[1] == "u":
        moves = []
        for i in getMoveVectors([0]):
            #print(i)
            j = 1
            while True:
                if not (x + i[0]*j > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):
                    if board[x + i[0]*j][y + i[1]*j][z + i[2]*j] == "   ":
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = figureChar[0]+"# "
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        #print(x + i[0]*j, y + i[1]*j, z + i[2]*j)
                        j += 1
                    else:
                        p = board[x + i[0]*j][y + i[1]*j][z + i[2]*j]
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                        if len(p) == 4:
                            board[x + i[0]*j][y + i[1]*j][z + i[2]*j] += p[3]
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        break
                else:
                    break
    elif figureChar[1] == "b":
        moves = []
        for i in getMoveVectors([1]):
            #print(i)
            j = 1
            while True:
                if not (x + i[0]*j > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):
                    if board[x + i[0]*j][y + i[1]*j][z + i[2]*j] == "   ":
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = figureChar[0]+"# "
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        #print(x + i[0]*j, y + i[1]*j, z + i[2]*j)
                        j += 1
                    else:
                        p = board[x + i[0]*j][y + i[1]*j][z + i[2]*j]
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                        if len(p) == 4:
                            board[x + i[0]*j][y + i[1]*j][z + i[2]*j] += p[3]
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        break
                else:
                    break
    elif figureChar[1] == "r":
        moves = []
        for i in getMoveVectors([2]):
            #print(i)
            j = 1
            while True:
                if not (x + i[0]*j > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):
                    if board[x + i[0]*j][y + i[1]*j][z + i[2]*j] == "   ":
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = figureChar[0]+"# "
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        #print(x + i[0]*j, y + i[1]*j, z + i[2]*j)
                        j += 1
                    else:
                        p = board[x + i[0]*j][y + i[1]*j][z + i[2]*j]
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                        if len(p) == 4:
                            board[x + i[0]*j][y + i[1]*j][z + i[2]*j] += p[3]
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        break
                else:
                    break
    elif figureChar[1] == "Q":
        moves = []
        for i in getMoveVectors([0, 1, 2]):
            #print(i)
            j = 1
            while True:
                if not (x + i[0]*j > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):
                    if board[x + i[0]*j][y + i[1]*j][z + i[2]*j] == "   ":
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = figureChar[0]+"# "
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        #print(x + i[0]*j, y + i[1]*j, z + i[2]*j)
                        j += 1
                    else:
                        p = board[x + i[0]*j][y + i[1]*j][z + i[2]*j]
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                        if len(p) == 4:
                            board[x + i[0]*j][y + i[1]*j][z + i[2]*j] += p[3]
                        moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                        break
                else:
                    break
    elif figureChar[1] == "K":
        moves = []
        for i in getMoveVectors([0, 1, 2]):
            #print(i)
            j = 1 # i'm too lazy to remove the j's.
            if not (x + i[0]*j > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):
                if board[x + i[0]*j][y + i[1]*j][z + i[2]*j] == "   ":
                    board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = figureChar[0]+"# "
                    moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
                else:
                    p = board[x + i[0]*j][y + i[1]*j][z + i[2]*j]
                    board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                    if len(p) == 4:
                        board[x + i[0]*j][y + i[1]*j][z + i[2]*j] += p[3]
                    moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
    elif figureChar[1] == "k":
        moves = []
        for i in getMoveVectors([1]):
            x_was_not_zero = False
            j = [] # knight goes 1 move in one dimension and 2 in other dimension. It's like being a bishop that can only move 1 step but moves in 1 dim are multipled by 2, and this for each dim.
            if i[0] != 0: j.append(1); j.append(2); x_was_not_zero = True
            else: j.append(0); j.append(0)
            if i[1] != 0:
                if x_was_not_zero: j.append(2); j.append(1);
                else: j.append(1); j.append(2);
            else: j.append(0); j.append(0)
            if i[2] != 0: j.append(2); j.append(1)
            else: j.append(0); j.append(0)
            if not (x + i[0]*j[0] > 5 or y + i[1]*j[2] > 5 or z + i[2]*j[4] > 5 or x + i[0]*j[1] < 0 or y + i[1]*j[2] < 0 or z + i[2]*j[4] < 0):
                if board[x + i[0]*j[0]][y + i[1]*j[2]][z + i[2]*j[4]] == "   ":
                    board[x + i[0]*j[0]][y + i[1]*j[2]][z + i[2]*j[4]] = figureChar[0]+"# "
                    moves.append([x + i[0]*j[0], y + i[1]*j[2], z + i[2]*j[4]])
                else:
                    p = board[x + i[0]*j[0]][y + i[1]*j[2]][z + i[2]*j[4]]
                    board[x + i[0]*j[0]][y + i[1]*j[2]][z + i[2]*j[4]] = p[0]+p[1]+"!"
                    if len(p) == 4:
                        board[x + i[0]*j[0]][y + i[1]*j[2]][z + i[2]*j[4]] += p[3]
                    moves.append([x + i[0]*j[0], y + i[1]*j[2], z + i[2]*j[4]])
            if not (x + i[0]*j[1] > 5 or y + i[1]*j[3] > 5 or z + i[2]*j[5] > 5 or x + i[0]*j[1] < 0 or y + i[1]*j[2] < 0 or z + i[2]*j[4] < 0):
                if board[x + i[0]*j[1]][y + i[1]*j[3]][z + i[2]*j[5]] == "   ":
                    board[x + i[0]*j[1]][y + i[1]*j[3]][z + i[2]*j[5]] = figureChar[0]+"# "
                    moves.append([x + i[0]*j[1], y + i[1]*j[3], z + i[2]*j[5]])
                else:
                    p = board[x + i[0]*j[1]][y + i[1]*j[3]][z + i[2]*j[5]]
                    board[x + i[0]*j[1]][y + i[1]*j[3]][z + i[2]*j[5]] = p[0]+p[1]+"!"
                    if len(p) == 4:
                        board[x + i[0]*j[1]][y + i[1]*j[3]][z + i[2]*j[5]] += p[3]
                    moves.append([x + i[0]*j[1], y + i[1]*j[3], z + i[2]*j[5]])
    elif figureChar[1] == "p":
        moves = []
        if figureChar[3] == "0":
            if figureChar[0] in "02": i = [0, 0, 1]
            else: i = [0, 0, -1]
            j = 1 # i'm too lazy to remove the j's.
            if not (x + i[0]*j > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):
                if board[x + i[0]*j][y + i[1]*j][z + i[2]*j] == "   ":
                    board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = figureChar[0]+"# "
                    moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
            if not (x + i[0]*j+1 > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):    
                if board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j] != "   ":
                    p = board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j]
                    board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                    if len(p) == 4:
                        board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j] += p[3]
                    moves.append([x + i[0]*j+1, y + i[1]*j, z + i[2]*j])
            
            if not (x + i[0]*j-1 > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):    
                if board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j] != "   ":
                    p = board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j]
                    board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                    if len(p) == 4:
                        board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j] += p[3]
                    moves.append([x + i[0]*j-1, y + i[1]*j, z + i[2]*j])
        elif figureChar[3] == "1":
            if figureChar[0] in "01": i = [1, 0, 0]
            else: i = [-1, 0, 0]
            j = 1 # i'm too lazy to remove the j's.
            if not (x + i[0]*j > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):
                if board[x + i[0]*j][y + i[1]*j][z + i[2]*j] == "   ":
                    board[x + i[0]*j][y + i[1]*j][z + i[2]*j] = figureChar[0]+"# "
                    moves.append([x + i[0]*j, y + i[1]*j, z + i[2]*j])
            if not (x + i[0]*j+1 > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):    
                if board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j] != "   ":
                    p = board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j]
                    board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                    if len(p) == 4:
                        board[x + i[0]*j+1][y + i[1]*j][z + i[2]*j] += p[3]
                    moves.append([x + i[0]*j+1, y + i[1]*j, z + i[2]*j])
            
            if not (x + i[0]*j-1 > 5 or y + i[1]*j > 5 or z + i[2]*j > 5 or x + i[0]*j < 0 or y + i[1]*j < 0 or z + i[2]*j < 0):    
                if board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j] != "   ":
                    p = board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j]
                    board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j] = p[0]+p[1]+"!"
                    if len(p) == 4:
                        board[x + i[0]*j-1][y + i[1]*j][z + i[2]*j] += p[3]
                    moves.append([x + i[0]*j-1, y + i[1]*j, z + i[2]*j])
def printBoard():
    title = "=====3D CHESS FOR 4 PLAYERS.EXE | PRESS CTRL+C TO EXIT | TYPE 'help' FOR HELP=====\n"
    boardnums = "        0                  1                  2                  3                  4                  5"
    outputString = [" ┌─0─1─2─3─4─5─┐    ┌─0─1─2─3─4─5─┐    ┌─0─1─2─3─4─5─┐    ┌─0─1─2─3─4─5─┐    ┌─0─1─2─3─4─5─┐    ┌─0─1─2─3─4─5─┐", "", "", "", "", "", "", " └─0─1─2─3─4─5─┘    └─0─1─2─3─4─5─┘    └─0─1─2─3─4─5─┘    └─0─1─2─3─4─5─┘    └─0─1─2─3─4─5─┘    └─0─1─2─3─4─5─┘"]
    for z in board:
        i = 0
        for y in z:
            i += 1
            outputString[i] += str(i-1)+"│"
            for x in y:
                if x[0] == " ": outputString[i] += x[2]+x[1]
                else: outputString[i] += colored(x[2]+x[1], colors[x[0]])
            outputString[i] += " │"+str(i-1)+"  "
        #outputString += " └123456┘ \n ┌123456┐ \n"
    os.system('cls')
    print(title+"\n"+boardnums+"\n"+outputString[0]+"\n"+outputString[1]+"\n"+outputString[2]+"\n"+outputString[3]+"\n"+outputString[4]+"\n"+outputString[5]+"\n"+outputString[6]+"\n"+outputString[7]+"\n"+boardnums)

while True:
    printBoard()
    pos = input()
    if pos == "help":
        print("1 - select your pawn by typing a 3-digit number. For exapmle: 254 will select a pawn from the 4th column of the 5th row of the 2nd board\n2 - a) deselect your pawn by pressing ENTER or b) type a 3-digit number to specify where do you want to move your pawn\n\npress ENTER to continue")
        input()
    else:
        try:
            getFigureMoves(int(pos[0]), int(pos[1]), int(pos[2]))
        except Exception as e:
            print(e)
            input()
            break
