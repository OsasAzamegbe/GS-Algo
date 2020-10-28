class Node:
    def __init__(self, data=0, nextNode=None):
        self.data = data
        self.next = nextNode

    def __repr__(self):
        return f'Node<{self.data}>'


class LL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def append(self, x: int) -> None:
        newNode = Node(x)

        if self.tail is not None:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.tail = newNode
            self.head = self.tail



def printLL(node):
    linkedList = []
    curr = node

    while curr:
        # print(curr.data, "\n")
        linkedList.append(curr.data)
        curr = curr.next

    return (" -> ").join(map(str, linkedList))


def condense(head):
    memo = set()
    curr = head

    while curr.next:
        memo.add(curr.data)
        if curr.next.data in memo:
            curr.next = curr.next.next
            continue

        curr = curr.next

    return head



if __name__ == "__main__":
    linkedList = LL()

    n = int(input())

    for _ in range(n):
        linkedList.append(int(input()))

    print(printLL(linkedList.head),"\n")

    result = condense(linkedList.head)

    print("This is the new head:", printLL(result))
