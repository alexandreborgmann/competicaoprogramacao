vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    s = list(input(""))
    for i in range(0,len(s)-1,2):
        aux = s[i]
        s[i] = s[i+1]
        s[i+1] = aux
    #print(s)
    alfabeto = { 'a': 'z',
           'b': 'y',
           'c': 'x',
           'd': 'w',
           'e': 'v',
           'f': 'u',
           'g': 't',
           'h': 's',
           'i': 'r',
           'j': 'q',
           'k': 'p',
           'l': 'o',
           'm': 'n',
           'n': 'm',
           'o': 'l',
           'p': 'k',
           'q': 'j',
           'r': 'i',
           's': 'h',
           't': 'g',
           'u': 'f',
           'v': 'e',
           'w': 'd',
           'x': 'c',
           'y': 'b',
           'z': 'a'
    }
    #abcdefghijklmnopqrstuvwxyz
    #zyxwvutsrqponmlkjihgfedcba
    for i in range(len(s)):
        aux = alfabeto.get(s[i])
        s[i] = aux
    s1=''.join(s)
    print(s1)

