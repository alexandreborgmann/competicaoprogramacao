a=input()
def words(valuestring):
    spacepos=valuestring.index(' ')
    return([valuestring[:spacepos],valuestring[(spacepos+1):]])

values=words(a)
wdrw=float(values[0])
balance=float(values[1])
if (wdrw%5 != 0 or wdrw + 0.5>balance):
    print("{:.2f}".format(balance))
else:
    print("{:.2f}".format(balance-wdrw-0.5))