i=0
while i<=2:
    for j in range(1,4):
        if (round(i,1)>0 and round(i,1)<1) or (round(i,1)>1 and round(i,1)<2):
            print('I={:.1f} J={:.1f}'.format(i,j+i))
        else:
            print('I={} J={}'.format(round(i), int(j + i)))
    i += 0.2