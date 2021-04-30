from data_structures import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        temp = Node(newNode)
        temp.next = self.head
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def printList(self):
        node = self.head
        while node is not None:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    def middlePosition(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("the middle element is", slow.data)

        return slow.data


if __name__ == '__main__':

    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
    middle_value = llist.middlePosition()
    llist.remove(middle_value)
    llist.printList()
