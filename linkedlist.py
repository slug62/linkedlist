"""
    Program:        linkedlist.py
    Author:         Peter Southwick
    Date:           06/19/16
    Description:    A program that has two classes, one Node class to store an airports code, a priority
                    of the airport, and a link to the following node.  The next class is a linkedlist class
                    that is responsible for maintaining a list of airport 'nodes'.  In the main portion of the code
                    provides a way for the user to interact with the two classes and their functions.
"""


class Node:
    def __init__(self, airportCode=None, priority=None):
        """
        Node class to be used in a linked list to represent the stops for user defined stops.
        :param airportCode: Code of the airport where the flight will stop
        :param priority: If used, defines the priority of the stop
        """
        self.__airportCode = airportCode
        self.__priority = priority
        self.__next = None

    def strnode(self):
        print(self.__airportCode)

    def setLink(self, link):
        self.__next = link

    def setData(self, data):
        self.__airportCode = data

    def setPriority(self, priority):
        self.__priority = priority

    def getData(self):
        return self.__airportCode

    def getLink(self):
        return self.__next

    def getPriority(self):
        return self.__priority


class LinkedList:
    def __init__(self):
        self.__numnodes = 0
        self.__head = None

    def insertFirst(self, data, priority=None):
        newnode = Node(data, priority)
        newnode.next = self.__head
        self.__head = newnode
        self.__numnodes += 1

    def insertLast(self, data, priority=None):
        newnode = Node(data, priority)
        newnode.next = None
        lnode = self.__head
        while lnode.next is not None:
            lnode = lnode.next
        lnode.next = newnode
        self.__numnodes += 1

    def insertPos(self, pos, data, priority=None):
        newnode = Node(data, priority)
        newnode.next = None
        lnode = self.__head
        lpos = 1
        while lnode.next is not None and lpos == pos:
            lnode = lnode.next
            lpos += 1
        lref = lnode.next
        lnode.next = newnode
        newnode.next = lref
        self.__numnodes += 1

    def remFirst(self):
        cnode = self.__head
        self.__head = cnode.next
        cnode.next = None
        del cnode
        self.__numnodes -= 1

    def remLast(self):
        lnode = self.__head
        while lnode.next is not None:
            pnode = lnode
            lnode = lnode.next
        pnode.next = None
        del lnode
        self.__numnodes -= 1

    def remPos(self, pos):
        lnode = self.__head
        lpos = 1
        pnode = lnode
        while lnode.next is not None and lpos < float(pos):
            pnode = lnode
            lnode = lnode.next
            lpos += 1
        lref = lnode.next
        pnode.next = lref
        del lnode
        self.__numnodes -= 1

    def getFirst(self):
        lnode = self.__head
        return lnode.data

    def getLast(self):
        lnode = self.__head
        while lnode.next is not None:
            lnode = lnode.next
            return lnode.data

    def getPos(self, pos):
        lnode = self.__head
        lpos = 1
        while lnode.next is not None and lpos < pos:
            lnode = lnode.next
            lpos += 1
        return lnode.data

    def print_list(self):
        lnode = self.__head
        while lnode:
            lnode.strnode()
            lnode = lnode.next

    def getNumStops(self):
        return self.__numnodes

if __name__ == '__main__':

    def doWork():
        trip = LinkedList()
        trip.insertFirst(input("Please input the airport code of your originating airport: "))
        trip.insertLast(input("Please input the airport code of your desired destination airport: "))
        result = ''
        while result != '99':
            result = input("(0): Change the starting airport code\n"
                           "(1): Change the destination airport code\n"
                           "(2): Add a stop\n"
                           "(3): Remove a stop\n"
                           "(4): Display your current flight plan\n"
                           "(5): Display the number of stops\n"
                           "(99): Quit this program\n")
            if result == '0':
                trip.remFirst()
                trip.insertFirst(input("Please enter the airport code of your originating airport: "))
            elif result == '1':
                trip.remLast()
                trip.insertLast(input("Please enter the airport code of your desired destination airport: "))
            elif result == '2':
                if trip.getNumStops() == 2:
                    trip.insertPos(2, input("Please input the airport code of your desired stop: "))
                else:
                    print("This is your current flight plan: ")
                    trip.print_list()
                    trip.insertPos(input("Where would you like your stop to be inserted, please enter (1-{}): ".format(str(trip.getNumStops()))),
                                   input("What is the airport code of your desired stop: "))
            elif result == '3':
                print("This is your current flight plan: ")
                trip.print_list()
                trip.remPos(input("Which stop would you like to remove, please enter 1-{}): ".format(str(trip.getNumStops()))))
            elif result == '4':
                trip.print_list()
            elif result == '5':
                print(trip.getNumStops())

    print("Welcome to my flight stop program.")
    doWork()


