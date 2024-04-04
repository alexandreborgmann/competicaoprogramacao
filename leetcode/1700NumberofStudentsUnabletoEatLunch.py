from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for i in range(len(sandwiches)):
            conta = 0
            pegou = 0
            while conta < len(students) and not pegou:
                #print('for j i=',i,'pegou=',pegou,'sandwiches=',sandwiches,'students=',students)
                if sandwiches[i] == students[0]:
                    pegou = 1
                    students.pop(0)
                    break
                else:
                    students.append(students[0])
                    students.pop(0)
                conta += 1
            if pegou == 0:
                break
            #print('for i i=',i,'pegou=',pegou,'sandwiches[i]=',sandwiches[i],'students=',students,)
        return(len(students))
objeto = Solution()
students = [1,1,0,0]
sandwiches = [0,1,0,1]
#students = [1,1,1,0,0,1]
#sandwiches = [1,0,0,0,1,1]
print(objeto.countStudents(students, sandwiches))