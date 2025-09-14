"""
Problem Statement
You are given two s: N and K. Lun the dog is interested in strings that satisfy the following conditions:
    The string has exactly N characters, each of which is either 'A' or 'B'.
    The string s has exactly K pairs (i, j) (0 <= i < j <= N-1) such that s[i] = 'A' and s[j] = 'B'.
If there exists a string that satisfies the conditions, find and return any such string. Otherwise, return an empty string.
Definition
Class: AB
Method: createString
Parameters: integer, integer
Returns: string
Method signature: def createString(self, N, K):
"""

class AB:

    def createString(self, N, K):
        """
        This works by creating a string of A's,\
        then inserting B's and moving them from\
        left to right until the required pairs are met
        """
        places_max = int(N / 2)

        if N % 2:
            places_max += 1

        places_list = (N - i for i in range(places_max))
        letters = list('A' * N)
        pairs = 0

        for places in places_list:
            for i in range(1, places):  # B starts from index 1 (AB...)
                if pairs == K:
                    return ''.join(letters)

                letters[i - 1] = 'A'  # Put the A back in its place
                letters[i] = 'B'  # Put the B one place further
                pairs += 1

            if pairs == K:
                return ''.join(letters)

            pairs -= 1  # - the place taken by the B

        return ''

c=AB()
for i in range(1,50):
    print('n=8, k= {} result {}'.format(i,c.createString(8,i)))