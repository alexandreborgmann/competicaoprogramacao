from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        print(f"👉 PUSH({x})")
        print(f"   Antes: q1 = {list(self.q1)}, q2 = {list(self.q2)}")

        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

        print(f"   Depois: q1 = {list(self.q1)}, q2 = {list(self.q2)}")
        print()

    def pop(self) -> int:
        valor = self.q1.popleft()
        print(f"👋 POP() = {valor}")
        print(f"   Estado atual: q1 = {list(self.q1)}")
        print()
        return valor

    def top(self) -> int:
        valor = self.q1[0]
        print(f"👀 TOP() = {valor}")
        print(f"   Estado atual: q1 = {list(self.q1)}")
        print()
        return valor

    def empty(self) -> bool:
        resultado = len(self.q1) == 0
        print(f"❓ EMPTY() = {resultado}")
        print()
        return resultado

    # Método adicional para debug
    def debug(self):
        print(f"🔍 DEBUG: q1 = {list(self.q1)}, q2 = {list(self.q2)}")
        print()


print("=== INICIANDO TESTE ===")
myStack = MyStack()

myStack.push(1)
myStack.push(2)
myStack.push(3)

myStack.debug()  # Mostra estado atual

print("=== OPERAÇÕES ===")
print("Top:", myStack.top())
print("Pop:", myStack.pop())
print("Pop:", myStack.pop())

myStack.debug()  # Estado final