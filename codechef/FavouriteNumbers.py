'''
Favourite Numbers
Alice likes numbers which are even, and are a multiple of 7.
Bob likes numbers which are odd, and are a multiple of 9.
Alice, Bob, and Charlie find a number
A
A.

If Alice likes
A
A, Alice takes home the number.
If Bob likes
A
A, Bob takes home the number.
If both Alice and Bob don't like the number, Charlie takes it home.
Given
A
A, find who takes it home.

Note: You can prove that there is no integer
A
A such that both Alice and Bob like it.

Input Format
The first line of input will contain a single integer
T
T, denoting the number of test cases.
Each test case consists of a single integer,
A
A.
Output Format
For each test case, output on a new line who takes the number home - "Alice", "Bob", or "Charlie".

You may print each character in uppercase or lowercase. For example, Alice, alice, aLiCe, and ALICE are all considered identical.

Constraints
1
≤
T
≤
100
1≤T≤100
1
≤
A
≤
1000
1≤A≤1000
'''
t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 == 0 and n % 7 == 0:
        print('alice')
    elif n%2 != 0 and n % 9 == 0:
        print('bob')
    else:
        print('charlie')