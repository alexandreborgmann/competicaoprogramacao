from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}

        while tasks:
            letra = tasks[0]
            d[letra] = tasks.count(letra)
            while tasks and letra in tasks:
                tasks.remove(letra)
        #print(d, tasks)
        total = 0
        while d:
            conta = 0
            for i in sorted(d, key=d.get):
                conta += 1
                d[i] -= 1
                print('i=', i, 'd[i]=', d[i],'conta=', conta)
                if d[i] == 0:
                    d.pop(i)
            if conta <= n and d:
                total += n+1
            else:
                total += conta
            print(d, conta, total)
        return total

objeto = Solution()
#tasks = ["A","A","A","B","B","B"]
#n = 2
#tasks = ["A","C","A","B","D","B"]
#n = 1
tasks = ["A","A","A", "B","B","B"]
n = 3
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 1
#tasks = ["A","A"]
#n = 2
print(objeto.leastInterval(tasks, n))