
def row_check(sol):
    #row condition checking
    for i in range(len(sol)):
        if len(set(sol[i]))==1 and sol[i][0]!=0: 
            x = sol[i][0]
            print(f'---Winner is Player{x}')
            return True
    return False

def diagonal_check(sol):
    s = 0
    d = 0
    #diagonal condition checking
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            if i==j:
                s+=sol[i][j]
            if i+j==2:
                d+=sol[i][j]
    if s==3 or s==6 or d==3 or d==6:
        if s==3 or d==3:
            print('---Winner is Player1')
        else:
            print('---Winner is Player2')
        return True
    return False

def column_check(sol):
    #column condition checking
    col1 = set()
    col2 = set()
    col3 = set()
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            if sol[i][j]!=0:
                if j==0:
                    col1.add(sol[i][j])
                elif j==1:
                    col2.add(sol[i][j])
                else:
                    col2.add(sol[i][j])
    if len(col1)==1 or len(col2)==1 or len(col3)==1:
        pass
    else:
        print('---draw')
        
#-----main funtion
sol = [[1,1,0],[0,2,1],[2,0,0]]
for i in range(len(sol)):
    for j in range(len(sol[i])):
        print(sol[i][j],end=' ')
    print()
if not row_check(sol):
    if not diagonal_check(sol):
        column_check(sol)