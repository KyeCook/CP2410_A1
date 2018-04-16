class Node(object):
    def __init__(self, d=None, i=None, n=None):
        self.element = d #element characteristic for node type
        self.index = i #node index characteristic for node type
        self.next_node = n #linkedlist pointer for node

    def get_next(self):
       return self.next_node

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

#     todo possibly make ^ into a seperate py file


class SparseArray(object):

    def __init__(self, n, r=None):
        self.root = Node() #initial empty node pointer for start
        self.last = Node() #initial empty node pointer for end
        self.size = n #set size of SparseArray, n
        self.use = 0 #initial set of non-empty element variable

    def __len__(self):
        return self.size

    def __setitem__(self, j, e):
        i = self.find_index(j)
        new_node = Node(e, i, self.root)
        self.root = new_node
        self.use += 1

    def __getitem__(self, j):
        i = self.find_index(j)
        this_node = self.root
        while this_node is not None:
            if this_node.get_index() == i:
                return this_node.element
            else:
                this_node = this_node.get_next()
        return None

    def fill(self, seq):
        if len(seq) < self.size:
            print(len(seq))
            for x in range(len(seq)):
                self[x] = seq[x]
        else:
            print ("ValueError: sequence longer than sparse array")
            raise SystemExit

    def get_usage(self):
        return self.use

    def find_index(self, j):
        if -1*self.size < j < 0:
            return self.size - abs(j)
        elif 0  <= j < self.size:
            return j
        else:
            print("IndexError: index out of range")
            raise SystemExit


    def print_list(self):
        print("Sparse Array:")
        this_node = self.root
        while this_node.has_next():
            print(this_node.to_string())
            this_node = this_node.get_next()

array = SparseArray(1000000)
print(len(array))
print(array.get_usage())
array[999999] = 42
print(array[999999])
print(array[-1])
print(array.get_usage())
print(array[0])
print(array[0] is None)
print(array[1000000])
