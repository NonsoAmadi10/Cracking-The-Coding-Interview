

class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        return 'data - {} \nnext - {}'.format(self.data, self.next)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):

        counter = 0
        curr = self.head
        while curr is not None:
            counter += 1
            curr = curr.next

        return counter

    def get_length(self):
        length = len(self)

        return length

    def traverse_list(self, data):
        if self.head is None:
            self.head = Node(data)
        curr = self.head
        while curr is not None:
            print(curr)
            curr = curr.next

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
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

    def kth_to_last(self, k):
        """ constraints- You can assume its a singly linked list \n
                        Empty list -> none \n
                        k >= list length -> none \n
                        if there is a single element in the list return the element
                        General case k < list length
        """
        if self.head is None:
            return None

        fast = self.head
        slow = self.head

        # Give fast a headstart
        for _ in range(k):
            fast = fast.next

            if fast is None:
                return None

        # Increment both pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data

    def del_k_to_last(self, k):
        """ constraints- You can assume its a singly linked list \n
                        Empty list -> none \n
                        k >= list length -> none \n
                        if there is a single element in the list return the element
                        General case k < list length
        """

        if self.head is None:
            return None

        curr = self.head
        first = curr
        for _ in range(k):
            first = first.next
        second = curr
        while first.next:
            first, second = first.next, second.next
        # second points to the (k + l)-th last node, deletes jts successor
        second.next = second.next.next
        return curr.next

    def del_middle_node(self):
        """ constraints - a singly linked list is assumed\n
        empty list returns none \n
        list less than one shoud return the element
        """
        if self.head is None:
            return None

        curr = self.head
        middle = len(self) / 2
        first = curr
        for _ in range(middle):
            first = first.next
        second = curr

        while first.next:
            first, second = first.next, second.next
        # second points to the (k + l)-th last node, deletes jts successor
        second.data = second.next.data
        second.next = second.next.next
        return curr.next

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def reverse_list(self):
        """ constraints --> singly linked list \n
        returns nonce on empty list -> reverses list
        """
        if self.head is None:
            return None

        curr = self.head
        reversed_list = SinglyLinkedList()
        while curr:
            reversed_list.insert_to_front(curr.data)
            curr = curr.next

        return reversed_list.get_all_data()

    def isPalindrome(self):
        if self.head is None and self.head.next is None:
            return False

        reverse_list = self.reverse_list()
        my_list = self.get_all_data()

        return reverse_list == my_list

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

    def parition_list(self, data):
        """
        constraints -- Empty list -> None\n
                        Data is valid\n
                        Returns one element list
        """
        left = SinglyLinkedList(None)
        right = SinglyLinkedList(None)

        if self.head is None:
            return None

        curr = self.head

        while curr is not None:
            if curr.data < data:
                left.append_to_list(curr.data)
            elif curr.data == data:
                right.insert_to_front(curr.data)
            else:
                right.append_to_list(curr.data)

            curr = curr.next

        cur_left = left.head
        if cur_left is None:
            return right

        # Merge both list together
        while cur_left.next:
            cur_left = cur_left.next

        cur_left.next = right.head
        return left.get_all_data()

    def find(self, data):
        """
        constraints -- Should return none on empty list\n
                        Assume it is a singlylinked list\n
                        Return None is data does not  exist\n
                        Returns the node and the index 
        """
        if self.head is None:
            return

        curr_node = self.head
        index = 0

        while curr_node:
            if curr_node.data == data:
                return curr_node.data, index
            curr_node = curr_node.next
            index += 1

        return None

    def delete(self, data):
        """ 
        constraints -- should return None on empty list\n
                        Assume it is a singly linkedlist\n
                        Return None if the data does not exist in the list\n
                        Deletes the node
        """
        if data is None:
            return None
        if self.head is None:
            return

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

        return None

    def sort_list(self):
        return sorted(self.get_all_data())

    def find_loop_start(self):
        """ Constraints:

        Empty list -> None
        Cyclic linkedlist -> None
        Return: the start of a loop
        """
        if self.head is None or self.head.next is None:
            return None

        slow = self.head
        fast = self.head

        # Give fast a head start ahead of slow

        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # if fast.next is none we do not have a circular list
            if fast is None:
                return None
            # When slow and fast meet, move slow to the head of the list
            if slow == fast:
                break

        slow = self.head
        # Increment slow and fast one node at a time until they meet
        while slow != fast:
            slow = slow.next
            fast = fast.next

            if fast is None:
                return None
        # Where they meet is the start of the loop
        return slow


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self, data):
        self.head = Node(data)

        while self.head != None:
            self.head.data = self.head.next
            self.head.next = self.head


newlist = SinglyLinkedList(None)

# newlist.head = Node('mon')

# print(newlist.traverse_list('new'))
newlist.append_to_list(16)
newlist.append_to_list(18)
newlist.append_to_list(10)
newlist.append_to_list(15)
newlist.append_to_list(11)

# print(newlist.reverse_list())
# print(newlist.kth_to_last(1))
# print(newlist.del_k_to_last(2))
# print(newlist.del_middle_node())


print(newlist.get_all_data())
print(newlist.isPalindrome())
# print(newlist.parition_list(18))
print(newlist.sort_list())
newlist.delete(16)
print(newlist.get_all_data())
