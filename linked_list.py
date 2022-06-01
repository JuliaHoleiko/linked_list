import math
class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.previous = None


class Queue(object):
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def addelement(self, x,y):
        newNode = Node(x,y)
        newNode.next = None
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.length += 1

    def delete_element(self):

        x = self.head.x
        y = self.head.y
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.tail = None
        return x, y

    def distance_between_first_and_last(self):
        if self.length == 0:
            return "list is empty"
        else:
            a = (self.head.x - self.tail.x)**2
            b = (self.head.y - self.tail.y)**2
            return math.sqrt(a + b)

    def search(self, x, y):
        if self.head is not None:
            current = self.head
            position = 0
            all_position = ""
            while current is not None:
                if (current.x == x) & (current.y == y):
                    position += 1
                    all_position += str(position) + " "
                    current = current.next
                else:
                    current = current.next
                    position +=1
            return all_position

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = '[ ' + "(" + str(current.x) + ", " + str(current.y) + ") "
            while current.next is not None:
                current = current.next
                out +=  "(" +str(current.x) + ", " + str(current.y) +  ") "
            return out + ']'
        return "List is empty"

    def get_length(self):
        return self.length
