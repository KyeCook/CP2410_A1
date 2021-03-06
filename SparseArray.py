"""
Name : Kye Cook | Student # : 13165418 | Subject : CP2410

Implementation of Sparse Arrays and Linked Lists
"""
from ArrayNode import Node  # Import functionality of Node Class

## Functionality of Sparse Array class ##

class SparseArray(object):
    def __init__(self, n, r=None):

        # Initial empty node pointers for start and end
        self.root = Node()
        self.last = Node()

        # set size of SparseArray, n
        self.size = n

        # initial set of non-empty element variables
        self.use = 0

    def __len__(self):
        return self.size

    def __setitem__(self, j, e):
        i = self.find_index(j)
        newNode = Node(e, i, self.root)
        self.root = newNode
        self.use += 1

    def find_index(self, j):
        if -1*self.size < j < 0:
            return self.size - abs(j)
        elif 0  <= j < self.size:
            return j
        else:
            print("IndexError: Index out of range")
            raise SystemExit

    def __getitem__(self, j):
        i = self.find_index(j)
        currentNode = self.root
        while currentNode is not None:
            if currentNode.get_index() == i:
                return currentNode.element
            else:
                currentNode = currentNode.get_next()
        return None

    def fill(self, seq):
        if len(seq) < self.size:
            print(len(seq))
            for x in range(len(seq)):
                self[x] = seq[x]




        else:
            print ("ValueError: Sequence longer than sparse array")
            raise SystemExit

    def get_usage(self):
        return self.use

    def print_list(self):
        print("Sparse Array:")
        currentNode = self.root
        while currentNode.has_next():
            print(currentNode.to_string())
            currentNode = currentNode.get_next()



# ## ******* Testing for sample output ********* ##
#
# # Set Array Length/Size
# array = SparseArray(1000000)
#
# # Show size
# print(len(array))
#
# # Show number of elements in use
# print(array.get_usage())
#
# # Assign value to an element within the array
# array[999999] = 42
#
# # Show this elements value
# print(array[999999])
#
# # Ensure size of array by checking element position against known array size
# print(array[-1])
#
# # Show that array now has 1 element in use
# print(array.get_usage())
#
# # Show status of first Array Element. Make sure its none
# print(array[0])
#
# # Ensure value is actually none/null using boolean
# print(array[0] is None)
#
# # Test Exception with IndexError
# print(array[1000000])
