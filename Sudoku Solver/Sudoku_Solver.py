a = [] # to store sudoku board

def intro():
    size = {1:"4x4",2:"6x6",3:"9x9",4:"12x12",5:"16x16",6:"20x20",7:"25x25"} # size of sudoku
    r_c = {1:4,2:6,3:9,4:12,5:16,6:20,7:25} # to define row and column
    border = {4:[2,2],6:[2,3],9:[3,3],12:[3,4],16:[4,4],20:[4,5],25:[5,5]} # to define border for printing
    print("Select the size of your sudoku:")
    for i in size:
        print("{}. {}".format(i,size[i]))
    ans = int(input())
    global row
    global col
    global x
    global y

    if ans in r_c:
        row = col = r_c[ans]

    if row in border:
        z = border[row]
        x , y = z[0] , z[1]
    
    entry()
    print("\n Board is : \n")
    puzzle(a)
    solve(a)
    print("\nSolution is : \n")
    puzzle(a)

def entry():
    for i in range(row):
        print("Enter row {} elements with space. Enter 0 if unknown".format(i+1))
        numbers = input().strip().split()
        a.append([])
        for b in numbers:
            a[i].append(int(b))

def solve(a):
    find = position(a)
    if not find: # means puzzle is solved
        return True
    else:
        e_row, e_col = find
    
    for i in range(1,row+1): # filling numbers from 1 to row+1
        if check(a,i,(e_row,e_col)): # check if position is ok to add number
            a[e_row][e_col] = i # number added
            if solve(a): # again Checking if this was the last position and all added values are correct
                return True
            a[e_row][e_col] = 0 # if not correct then set this value to zero and backtrack by returning false
    return False

def check(a,num,pos):
    # check row
    for i in range(row):
        if a[pos[0]][i] == num and pos[1] != i:
            return False

    # check col
    for j in range(col):
        if a[j][pos[1]] == num and pos[0] != j:
            return False

    # check box
    box_row = pos[0]//x
    box_col = pos[1]//y
    for i in range(box_row*x,box_row*x+x): # check row-wise
        for j in range(box_col*y,box_col*y+y): # check col-wise
            if a[i][j] == num and (i,j) != pos:
                return False
    return True

def puzzle(a):
    for i in range(row):
        if i % x == 0 and i != 0:
            print("-"*(row*2))
        for j in range(col):
            if j % y == 0 and j != 0:
                print("|", end="")
            if j == row-1:
                print(a[i][j])
            else:
                print(str(a[i][j]) + " ",end="")

def position(a):
    for i in range(row):
        for j in range(col):
            if a[i][j] == 0:
                return (i,j) # return empty row and col position as a tuple
    return None

intro()
