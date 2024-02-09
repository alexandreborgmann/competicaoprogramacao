'''
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
'''
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.dfs(nestedList)
        self.stack.reverse()

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, nested):
        print(nested)
        for n in nested:
            if n.isInteger():
                self.stack.append(n.getInteger)
            else:
                self.dfs(n.getList())

'''
nestedList = [[1,1],2,[1,1]]
nestedList = [1, [4, [6]]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    print('i=',i)
    v.append(i.next())
print('v=',v)
'''