s = input("")
for l in 'hello':
    #print('letra=',l,'s=',s)
    achou = 0
    while len(s)>0:
        if l==s[0]:
            achou=1
            s = s[1:]
            break;
        else:
            s=s[1:]
        #print(s,'l=',l,'s[i]=','achou=',achou)
    if achou==0:
        print('NO')
        exit(0)
print('YES')