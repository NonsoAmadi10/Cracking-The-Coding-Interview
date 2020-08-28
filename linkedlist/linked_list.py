class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'data - {} \nnext - {}'.format(self.data, self.next)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self, data):
        self.head = Node(data)

        while self.head.data != None:
            print(self.head)
            self.head.data = self.head.next


newlist = SinglyLinkedList()

#newlist.head = Node('mon')

print(newlist.traverse_list('new'))
