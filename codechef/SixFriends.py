vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
   x, y = map(int, input("").split())
   vx=int(6/2*x)
   vy=int(6/3*y)
   if vx < vy:
       print(vx)
   else:
       print(vy)