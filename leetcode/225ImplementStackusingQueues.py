from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Adiciona o elemento e depois rotaciona a fila
        para colocar o novo elemento na frente
        """
        self.q.append(x)
        # Rotaciona a fila: move todos os elementos anteriores para depois do novo
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())    # Retorna 2
print(myStack)
print(myStack.pop())    # Retorna 2
print(myStack.empty())  # Retorna False