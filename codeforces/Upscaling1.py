vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    rowSize = n*2
    colSize = n*2
    row = 0
    col = 0

    arr = [[" "]*colSize for _ in range(rowSize)]

    turn = '#'

    #print('tamanho arr =',len(arr), len(arr[0]))

    while(row<rowSize):
        start = turn;
        while(col<colSize):
            if(start=='#'):
                arr[row][col] = '#'
                arr[row][col+1] = '#'
                arr[row+1][col] = '#'
                arr[row+1][col+1] = '#'
                start = '.'
            else:
                arr[row][col] = '.'
                arr[row][col+1] = '.'
                arr[row+1][col] = '.'
                arr[row+1][col+1] = '.'

                start = '#'
            col+=2
        if(turn == '#'):
            turn = '.'
        else:
            turn = '#'

        row += 2
        col = 0

    #print(arr)
    for i in range(n*2):
        for j in range(len(arr[0])):
            print(arr[i][j],end='')
        print('',sep='')



