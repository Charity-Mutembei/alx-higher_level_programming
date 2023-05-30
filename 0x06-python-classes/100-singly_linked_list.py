#!/usr/bin/python3
"""
a class Node that defines a node of a singly linked list by:
Private instance attribute: data, Private instance attribute:
next_node,
"""


class Node:
    """This class represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and next_node.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the linked list.
            Defaults to None.

        Raises:
            TypeError: If the data is not an integer.
            TypeError: If next_node is not None or a Node object.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data value of the node.

        Returns:
            int: The data value of the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node.

        Args:
            value (int): The data value of the node.

        Raises:
            TypeError: If the data is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If next_node is not None or a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list with a head."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value of the new node.

        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                   value > current.next_node.data):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.

        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
