hospede = input("")
anfitriao = input("")
embaralhado = input("")
uniao = hospede + anfitriao
s = set(uniao)
if s != set(embaralhado):
    print('NO')
    exit(0)
for i in s:
    if uniao.count(i) != embaralhado.count(i):
        print('NO')
        exit(0)
print('YES')