n=int(input())
p=[int(x) for x in input().split()]
q=[int(x) for x in input().split()]
total=0
p.pop(0)
q.pop(0)
print(p,q)
for i in range(1,n+1):
    num=p.count(i)+q.count(i)
    print(num,i)
    if num>0:
        total+=1
    else:
        total+=0
if total==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')