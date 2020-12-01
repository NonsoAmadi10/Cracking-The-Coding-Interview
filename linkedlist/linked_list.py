class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        return 'data - {} \nnext - {}'.format(self.data, self.next)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse_list(self, data):
        self.head = Node(data)

        while self.head.data != None:
            print(self.head)
            self.head.data = self.head.next

    def append_to_list(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        return node

    def remove_duplicates(self):
        """constraints - Its a singly linked list
                   - You can't insert None Values
                   You can assume it fits in memory
        """
        if self.head is None:
            return

        node = self.head
        seen_data = set()
        while node is not None:
            if node.data is not None:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

    def get_all_data(self):
        """ returns all data in a linked list

        Keyword arguments:
        argument -- None
        Return: list
        """
        all_nodes = []
        curr = self.head

        while curr is not None:
            all_nodes.append(curr.data)
            curr = curr.next
        return all_nodes


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self, data):
        self.head = Node(data)

        while self.head != None:
            self.head.data = self.head.next
            self.head.next = self.head


newlist = SinglyLinkedList()

#newlist.head = Node('mon')

# print(newlist.traverse_list('new'))
newlist.append_to_list(12)
newlist.append_to_list(13)
print(newlist.get_all_data())
