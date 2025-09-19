# spiral matrix

a=list(map(int,input().split()))
b=[]
for x in range(a[0]):
    c=list(map(int,input(f'enter {a[1]} values').split()))
    b.append(c)

res=[]
s_row=0
e_row=a[0]-1

s_col=0
e_col=a[1]-1


while (s_row<=e_row and s_col<=e_col):

    #top row
    for x in range(s_col,e_col+1):
        res.append(b[s_row][x])


    #right row
    for y in range(s_row+1,e_row+1):
        res.append(b[y][e_col])     


    #bottom row
    for c in range(e_col-1,s_col-1,-1):
        if s_row==e_row:
            break

        else:
            res.append(b[e_row][c])


    #left row
    for d in range(e_row-1,s_col,-1):
        if s_col==e_col:
            break
        else:
            res.append(b[d][s_col])

    s_col+=1
    e_col-=1

    s_row+=1
    e_row-=1
print(res)