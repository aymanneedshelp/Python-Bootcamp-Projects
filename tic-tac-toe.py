import sys
from time import sleep

def delete_last_line():
    for i in range(4):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

def display(row1,row2,row3):
    print(row1,row2,row3,sep='\n')


x_win = False
o_win = False
win = " "
turn = 0
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

print("REFER TO THIS FOR TABLE POSITIONS")
print()
print([1,2,3],[4,5,6],[7,8,9],sep='\n')
print()
print("-----------")
print()

def win_O():
    global win
    if row1 == ["O","O","O"] or row2 == ["O","O","O"] or row3 == ["O","O","O"]: #checking horizontals
        win = "O"
    elif row1[0] == "O" and row2[0] == "O" and row3[0] == "O": #checking vertical 1
        win = "O"
    elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O": #checking vertical 2
        win = "O"
    elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O": #checking vertical 3
        win = "O"
    elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O": #diagonal 1
        win = "O"
    elif row1[2] == "O" and row2[1] == "O" and row3[0] == "O": #diagonal 2
        win = "O"

def win_x():
    global win
    if row1 == ["X","X","X"] or row2 == ["X","X","X"] or row3 == ["X","X","X"]: #checking horizontals
        win = "X"
    elif row1[0] == "X" and row2[0] == "X" and row3[0] == "X": #checking vertical 1
        win = "X"
    elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X": #checking vertical 2
        win = "X"
    elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X": #checking vertical 3
        win = "X"
    elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X": #diagonal 1
        win = "X"
    elif row1[2] == "X" and row2[1] == "X" and row3[0] == "X": #diagonal 2
        win = "X"

def check_win():
    win_O()
    win_x()

def check_full():
    global win
    if " " not in row1 and " " not in row2 and " " not in row3:
        win = "Draw"

    
while win == " ":
    display(row1,row2,row3)
    if turn % 2 == 0:
        choice = int(input("Enter the position to mark X: "))
        if choice == 1 and row1[0] == " ":
            row1[0] = "X"
            check_win()
        elif choice == 2 and row1[1] == " ":
            row1[1] = "X"
            check_win()
        elif choice == 3 and row1[2] == " ":
            row1[2] = "X"
            check_win()
        elif choice == 4 and row2[0] == " ":
            row2[0] = "X"
            check_win()
        elif choice == 5 and row2[1] == " ":
            row2[1] = "X"
            check_win()
        elif choice == 6 and row2[2] == " ":
            row2[2] = "X"
            check_win()
        elif choice == 7 and row3[0] == " ":
            row3[0] = "X"
            check_win()
        elif choice == 8 and row3[1] == " ":
            row3[1] = "X"
            check_win()
        elif choice == 9 and row3[2] == " ":
            row3[2] = "X"
            check_win()
        else:
            print("Can't make a move there")
            sleep(1)
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            delete_last_line()
            continue
    else:
        choice = int(input("Enter the position to mark O: "))
        if choice == 1 and row1[0] == " ":
            row1[0] = "O"
            check_win()
        elif choice == 2 and row1[1] == " ":
            row1[1] = "O"
            check_win()
        elif choice == 3 and row1[2] == " ":
            row1[2] = "O"
            check_win()
        elif choice == 4 and row2[0] == " ":
            row2[0] = "O"
            check_win()
        elif choice == 5 and row2[1] == " ":
            row2[1] = "O"
            check_win()
        elif choice == 6 and row2[2] == " ":
            row2[2] = "O"
            check_win()
        elif choice == 7 and row3[0] == " ":
            row3[0] = "O"
            check_win()
        elif choice == 8 and row3[1] == " ":
            row3[1] = "O"
            check_win()
        elif choice == 9 and row3[2] == " ":
            row3[2] = "O"
            check_win()
        else:
            print("Can't make a move there")
            sleep(1)
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            delete_last_line()
            continue
    sleep(2)
    delete_last_line()
    turn+=1
    check_full()

display(row1,row2,row3)
print()
print("Winner is: ",win)