dic = { "vertebrado": { "ave": { "carnivoro": "aguia", "onivoro": "pomba"},
                       "mamifero": { "onivoro": "homem", "herbivoro": "vaca"}
                        },
        "invertebrado": { "inseto": { "hematofago": "pulga", "herbivoro": "laguarta"},
                         "anelideo":  { "hematofogo": "sanguessuga", "onivoro": "minhoca"}
                          }
    }
a = input()
b = input()
c = input()
try:
    print(dic[a][b][c])
except KeyError:
    print("A combinação que você digitou não existe, tente novamente.")

