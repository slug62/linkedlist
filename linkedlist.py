# A simple class for Linked List

class Node:
    def __init__(self, data=None):
        self.__airportCode = data
        self.__next = None

    def strnode(self):
        print(self.__airportCode)

    def setLink(self, link):
        self.__next = link

    def setData(self, data):
        self.__airportCode = data

    def getData(self):
        return self.__airportCode

    def getLink(self):
        return self.__next


class LinkedList:
    def __init__(self):
        self.__numnodes = 0
        self.__head = None

    def insertFirst(self, data):
        newnode = Node(data)
        newnode.next = self.__head
        self.__head = newnode
        self.__numnodes += 1

    def insertLast(self, data):
        newnode = Node(data)
        newnode.next = None
        lnode = self.__head
        while lnode.next is not None:
            lnode = lnode.next
        lnode.next = newnode  # new node is now the last node
        self.__numnodes += 1

    def insertPos(self, data, pos):
        newnode = Node(data)
        newnode.next = None
        lnode = self.__head
        lpos = 1
        while lnode.next is not None and lpos == pos:
            lnode = lnode.next
            lpos += 1
        lref = lnode.next
        lnode.next = newnode  # new node is now inserted
        newnode.next = lref

    def remFirst(self):
        cnode = self.__head
        self.__head = cnode.next  # new head is second node
        cnode.next = None
        del cnode

    def remLast(self):
        lnode = self.__head
        while lnode.next is not None:  # traversing list
            pnode = lnode
            lnode = lnode.next
        pnode.next = None
        del lnode

    def remPos(self, pos):
        lnode = self.__head
        lpos = 1
        pnode = lnode
        while lnode.next is not None and lpos < pos:  # traversing list
            pnode = lnode
            lnode = lnode.next
            lpos += 1
        lref = lnode.next
        pnode.next = lref
        del lnode

    def getFirst(self):
        lnode = self.__head  # first node
        return lnode.data

    def getLast(self):
        lnode = self.__head
        while lnode.next is not None:  # traversing list
            lnode = lnode.next
            return lnode.data

    def getPos(self, pos):
        lnode = self.__head
        lpos = 1
        while lnode.next is not None and lpos < pos:  # traversing list
            lnode = lnode.next
            lpos += 1
        return lnode.data

    def print_list(self):
        lnode = self.__head
        while lnode:
            lnode.strnode()  # print lnode.data
            lnode = lnode.next

ll = LinkedList()
ll.insertFirst(12345)
ll.insertFirst(23456)

ll.print_list()