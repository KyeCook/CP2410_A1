class Node(object):
    def __init__(self, d=None, i=None, n=None):
        # element value for node
        self.element = d
        # node index value for node
        self.index = i
        # Linked List pointer value for node
        self.nextNode = n

    def get_next(self):
       return self.nextNode

    def get_data(self):
        return self.element

    def set_data(self, d):
        self.element = d

    def get_index(self):
        return self.index

    def to_string(self):
        return "Element: " + str(self.element)

    def has_next(self):
        if self.get_next() is None:
            return False
        return True