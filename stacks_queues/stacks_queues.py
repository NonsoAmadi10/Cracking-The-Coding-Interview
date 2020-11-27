class Stack:

    """
    A stack uses LIFO (last-in first-out) ordering. That is, as in a stack of dinner plates, the most recent item
    added to the stack is the first item to be removed.
    It uses the following operations:
    pop() : Remove the top item from the stack.
    push(item) : Add an item to the top of the stack.
    peek(): Return the top of the stack.
    isEmpty() : Return true if and only if the stack is empty.
    """

    def __init__(self):
        self.element = []
        self.size = len(self.element)

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty:
            raise ValueError("pop(): Stack has no element")
        else:
            return self.element.pop()

    def push(self, data):
        self.element.append(data)
        return

    def peek(self):
        return self.element[-1]


my_stack = Stack()

my_stack.push(33)
my_stack.push(2)
print(my_stack.is_empty())
print(my_stack.peek())


# Implement a stack using a linkedlist

class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        return 'data - {} \nnext - {}'.format(self.data, self.next)


class MyStack:
    def __init__(self, data=None):
        self.head = data

    def size(self):
        size = 0
        curr_node = self.head
        if self.head is None:
            return size

        while curr_node is not None:
            size += 1
            curr_node = curr_node.next

        return size

    def peek(self):
        if not self.head:
            raise ValueError("peek(): stack has not element")
        curr_node = self.head
        top = None

        while curr_node is not None:
            top = curr_node.data
            print(top)
            if curr_node.next is None:
                return top
            curr_node = curr_node.next

    def push(self, data):
        if data is None:
            raise ValueError("push(): data not specified")
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        return node

    def pop(self, data):
        if data is None:
            raise ValueError("pop(): data not specified")
        if self.head is None:
            raise ValueError("pop(): stack has not element")

        if self.head.data == data:
            self.head = self.head.next
            return

        curr_node = self.head
        next_node = self.head.next
        while next_node is not None:
            if curr_node.data == data:
                curr_node.next = next_node.next
                return 'ok'
            curr_node = next_node
            next_node = next_node.next

        return

    def isEmpty(self):
        return self.size() == 0


list_stack = MyStack()

list_stack.push(3)
list_stack.push(5)
list_stack.push(7)
list_stack.pop(3)
print(list_stack.peek())
print(list_stack.isEmpty())
