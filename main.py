class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        cur = self.head
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        while cur.next:
            cur = cur.next
        cur.next = newNode

    def printll(self):
        cur = self.head
        while cur:
            print(cur.value, end='')
            cur = cur.next

    def convtonum(self):
        ans = ''
        cur = self.head
        while cur:
            ans += str(cur.value)
            cur = cur.next
        return int(ans)


def addition(ll1, ll2):
    number1 = ll1.convtonum()
    number2 = ll2.convtonum()
    return number1 + number2

def subtraction(ll1, ll2):
    number1 = ll1.convtonum()
    number2 = ll2.convtonum()
    return number1 - number2

def multiplication(ll1, ll2):
    number1 = ll1.convtonum()
    number2 = ll2.convtonum()
    return number1 * number2

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)


ll2 = LinkedList()
ll2.append(5)
ll2.append(6)


ll1.printll()

print(multiplication(ll1, ll2))