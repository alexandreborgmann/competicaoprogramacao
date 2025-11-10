class Solution:
    def findLatestTime(self, s: str) -> str:
        hora = s[0:2]
        minuto = s[3:5]
        if hora.count('?') == 2:
            hora = '11'
        elif hora[0] == '?':
            if int(hora[1])>1:
                hora = '0'+hora[1]
            else:
                hora = '1'+hora[1]
        elif hora[1] == '?':
            if int(hora[0]) == 0:
                hora = hora[0]+'9'
            else:
                hora = hora[0]+'1'
        if minuto.count('?') == 2:
            minuto = '59'
        elif minuto[0] == '?':
            minuto = '5'+minuto[1]
        elif minuto[1] == '?':
            minuto = minuto[0]+'9'

        #print(s, hora, minuto)
        return hora+':'+minuto

objeto = Solution()
#s = "1?:?4"
#s = "0?:5?"
#s = "??:1?"
#s = "?1:?6"
s = "1?:30"
print(objeto.findLatestTime(s))