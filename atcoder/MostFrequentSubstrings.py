'''
Problem Statement
You are given a string
S of length
N consisting of lowercase English letters.

Define the number of occurrences of a string
t of length
K as the number of integers
i that satisfy the following condition:

1≤i≤N−K+1
The substring of
S from the
i-th character to the
(i+K−1)-th character matches
t.
Find the maximum value
x of the number of occurrences of a string of length
K. Also, output all strings of length
K with
x occurrences in ascending lexicographical order.

Constraints
N,K are integers.
S is a string of length
N consisting of lowercase English letters.
1≤K≤N≤100
Input
The input is given from Standard Input in the following format:

N
K
S
Output
Output two lines.

The first line should contain the maximum value
x of the number of occurrences of a string of length
K.

The second line should contain all strings of length
K with
x occurrences in ascending lexicographical order, separated by spaces.

Sample Input 1
Copy
9 3
ovowowovo
Sample Output 1
Copy
2
ovo owo
The following strings have two occurrences:

For the string ovo,
i=1,7 satisfy the condition, so the number of occurrences of ovo is
2.
For the string owo,
i=3,5 satisfy the condition, so the number of occurrences of owo is
2.
There is no string of length
3 with more than two occurrences, so the maximum value is
2.

On the other hand, the following are examples of strings with fewer than two occurrences:

For the string vow,
i=2 satisfies the condition, so the number of occurrences of vow is
1.
For the string ooo, there is no
i that satisfies the condition, so the number of occurrences of ooo is
0.
Sample Input 2
Copy
9 1
ovowowovo
Sample Output 2
Copy
5
o
Sample Input 3
Copy
35 3
thequickbrownfoxjumpsoverthelazydog
Sample Output 3
Copy
2
the
'''
n, k = map(int, input().split())
s = input()

# Dicionário para contar ocorrências de cada substring
count_dict = {}

# Gerar todas as substrings de comprimento K
for i in range(n - k + 1):
    substring = s[i:i + k]
    count_dict[substring] = count_dict.get(substring, 0) + 1

# Encontrar a contagem máxima
max_count = max(count_dict.values())

# Coletar todas as substrings com contagem máxima
max_substrings = [substring for substring, count in count_dict.items() if count == max_count]

# Ordenar lexicograficamente
max_substrings.sort()

# Saída
print(max_count)
print(" ".join(max_substrings))
