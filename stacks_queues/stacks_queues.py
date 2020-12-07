import sys


class Stack(object):

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


class MyStack(object):
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
                return data
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


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)
        return

    def dequeue(self):
        if not self.data:
            raise KeyError('dequeue(): no data in the queue')
        else:
            return self.data.pop(0)

    def peek(self):
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

    def max(self):
        return max(self.data)


my_queue = Queue()

my_queue.enqueue(3)
my_queue.enqueue(5)
my_queue.enqueue(6)

print(my_queue.max())
print(my_queue.peek())
print(my_queue.isEmpty())
print(my_queue.dequeue())


class Stacks(object):

    """
    Absolute Index
    return stack size * stack index + stack pointer
    Complexity:

    Time: O(1)
    Space: O(1)
        Push
    If stack is full, throw exception
    Else
    Increment stack pointer
    Get the absolute array index
    Insert the value to this index
    Complexity:

    Time: O(1)
    Space: O(1)
        Pop
    If stack is empty, throw exception
    Else
    Store the value contained in the absolute array index
    Set the value in the absolute array index to None
    Decrement stack pointer
    return value
    Complexity:

    Time: O(1)
    Space: O(1)
    """

    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stacks
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]

    def push(self, stack_index, data):
        if self.stack_pointers[stack_index] == self.stack_size - 1:
            raise Exception('Stack is full')
        self.stack_pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data

    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise Exception('Stack is empty')
        array_index = self.abs_index(stack_index)
        data = self.stack_array[array_index]
        self.stack_array[array_index] = None
        self.stack_pointers[stack_index] -= 1
        return data


class StackMin(MyStack):

    """                 
    We'll use a second stack to keep track of the minimum values.

    Min
    If the second stack is empty, return an error code (max int value)
    Else, return the top of the stack, without popping it
    Complexity:

    Time: O(1)
    Space: O(1)
    PUSH
    Push the data
    If the data is less than min
    Push data to second stack
    Complexity:

    Time: O(1)
    Space: O(1)
    Pop
    Pop the data
    If the data is equal to min
    Pop the top of the second stack
    Return the data
    Complexity:

    Time: O(1)
    Space: O(1)
    """

    def __init__(self, head=None):
        super(StackMin, self).__init__(head)
        self.stack_of_mins = MyStack()

    def minimum(self):
        if self.stack_of_mins.head is None:
            return sys.maxsize
        else:
            return self.stack_of_mins.peek()

    def push(self, data):
        super(StackMin, self).push(data)
        if data < self.minimum():
            self.stack_of_mins.push(data)

    def pop(self):
        data = super(StackMin, self).pop()
        if data == self.minimum():
            self.stack_of_mins.pop()
        return data


mymin = StackMin()

mymin.push(5)
mymin.push(3)
mymin.push(6)

print(mymin.minimum())
