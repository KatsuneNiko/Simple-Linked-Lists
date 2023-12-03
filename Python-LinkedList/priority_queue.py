class PriorityQueue:

    # A node class to act as the internals of the linked list based
    # priority queue.
    class Node:

        # Constructor for the Node class, each node has a
        # __data variable to store the data, a __priority
        # variable to determine where to put it in the list
        # and a __next_node variable that points at the next Node.
        def __init__(self, data, priority, next_node=None):
            self.__data = data
            self.__priority = priority
            self.__next_node = next_node

        # Returns the value of __data.
        def data(self):
            return self.__data

        # Returns the value of __priority.
        def priority(self):
            return self.__priority

        # Returns the next Node (the value of __next_node).
        def get_next(self):
            return self.__next_node

        # Change the value of __next_node.
        def set_next(self, next_node):
            self.__next_node = next_node

    # Set up the priority queue. It should start
    # empty, with a size of 0.
    def __init__(self):
        self.__size = 0
        self.__head = None

    # Add a new element to the queue with the
    # given priority.
    def offer(self, data, priority):
        if (self.__size == 0):
            self.__head = self.Node(data, priority)
            self.__size += 1
            return
        elif (self.__size > 0):
            if (priority >= self.__head.priority()):
                self.__head = self.Node(data, priority, self.__head)
                self.__size += 1
                return
            elif (priority < self.__head.priority()):
                current_node = self.__head
                while (current_node.get_next() != None):
                    if (priority >= current_node.get_next().priority()):
                        current_node.set_next(self.Node(data, priority, current_node.get_next()))
                        self.__size += 1
                        return
                    current_node = current_node.get_next()
                if (priority < current_node.priority()):
                    current_node.set_next(self.Node(data, priority, None))
                    self.__size = self.__size + 1
                    return

    # Remove the Node at the front of the PriorityQueue
    # and return the value it contains.
    def poll(self):
        temp = self.__head
        self.__head = temp.get_next()
        self.__size -= 1
        return temp.data()

    # Return the number of Nodes in the queue.
    def size(self):
        return self.__size

    # Return True if the list is empty, False otherwise.
    def is_empty(self):
        return (self.__size == 0)

    # The __str__ method returns a string representation of
    # the object. It is not part of the test, but you may
    # like to use it for your own purposes.
    def __str__(self):
        return "This is a list"

# The main section is not part of the assignment, but you
# may use it to do your own testing.
if __name__ == '__main__':
    pass
