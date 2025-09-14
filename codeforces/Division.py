vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for i in range(vezes):
    rating = int(input(""))
    if rating<-5000 and rating>5000:
        continue
    division=4
    if rating>=1900:
        division=1
    elif rating>=1600 and rating<=1899:
        division=2
    elif rating>=1400 and rating<=1599:
        division=3
    else:
        division=4
    print('Division ',division)
