'''
You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles.
Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.



Example 1:


Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
Example 2:


Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.


Constraints:

1 <= numBottles <= 100
1 <= numExchange <= 100
'''
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        empty_bottles = 0
        current_exchange = numExchange

        # Enquanto tivermos garrafas cheias ou pudermos trocar
        while numBottles > 0 or empty_bottles >= current_exchange:
            # Beber todas as garrafas cheias
            if numBottles > 0:
                total_drunk += numBottles
                empty_bottles += numBottles
                numBottles = 0

            # Tentar trocar garrafas vazias
            if empty_bottles >= current_exchange:
                # Calcular quantas trocas podemos fazer
                # Como numExchange aumenta a cada troca, só podemos fazer uma troca por vez
                numBottles += 1
                empty_bottles -= current_exchange
                current_exchange += 1

        return total_drunk

objeto = Solution()
numBottles = 13
numExchange = 6

numBottles = 10
numExchange = 3
print(objeto.maxBottlesDrunk(numBottles, numExchange))