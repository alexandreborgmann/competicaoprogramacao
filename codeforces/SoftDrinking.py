namigos, kgarrafa, lmililitros, climao, dpedacos, psal, nlmilipessoa, npsalpessoa = map(int,input("").split())
bebidas = int((kgarrafa*lmililitros)/nlmilipessoa)
limoes = climao*dpedacos
sal = psal/npsalpessoa
#print(bebidas, limoes, sal)
menor = min(bebidas, limoes, sal)
drinks = int(menor / namigos)
print(drinks)