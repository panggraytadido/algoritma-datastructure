#https://geekflare.com/tic-tac-toe-python-code/ 

board=[]
for i in range(3):
    row = []
    for j in range(3):
        row.append('-')
    board.append(row)

def check_board(r,c,huruf):
    if board[r][c]!='-':
        return 0
    else:
        board[r][c]=huruf
        return check_menang(board,huruf)
    
def check_menang(board,huruf):
    #check horizontal 0 
    check=0
    for i in range(3):
        if board[i][0]==huruf:
            check+=1
            if check>=3:
                hasil='menang'
            else:
                hasil = '-'
    
    #check horizontal 1    
    for i in range(3):
        if board[i][1]==huruf:
            check+=1
            if check>=3:
                hasil='menang'
            else:
                hasil = '-'
                
    #check horizontal 2
    for i in range(3):
        if board[i][2]==huruf:
            check+=1
            if check>=3:
                hasil='menang'
            else:
                hasil = '-'
                
    #check vertical 0
    for i in range(3):
        for j in range(3):
            if board[i][j]==huruf:
                check+=1
                if check>=3:
                    hasil='menang'
                else:
                    hasil = '-'
                    
    #check diagonal 1 (kiri ke kanan)
    for i in range(3):
        if board[i][i]==huruf:
            check+=1
            if check>=3:
                hasil='menang'
            else:
                hasil = '-'
                
    column_1=2            
    for i in range(3):
        if board[i][column_1]==huruf:
            check+=1
            if check>=3:
                hasil='menang'
            else:
                hasil = '-'
        column_1=+1 
        
        
        
    return hasil
    
    
        
check = check_board(0,0,'o')
#print(board)

check = check_board(1,1,'o')
#print(board

check = check_board(2,2,'x')
print(check)
        
#print(check_menang(board,'x'))

#for i in range(3):
    #print(board[i][0])
    
#print(board)


