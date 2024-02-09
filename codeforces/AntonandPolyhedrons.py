vezes = int(input(""))
if vezes > 200000 or vezes < 1:
    exit(1)
figuras = {'Tetrahedron':4, 'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20}
objetos = []
soma = 0
for i in range(vezes):
    objetos.append(input(""))
for i in objetos:
    soma = soma + figuras.get(i)
print(soma)