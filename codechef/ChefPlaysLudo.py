vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
for i in range(vezes):
    tempo = int(input(""))
    print(int(tempo*60/20))
