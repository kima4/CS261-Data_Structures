# Course: CS261 - Data Structures
# Assignment: Programming Assignment 5 - Min Heap Implementation
# Student: Alexander Kim
# Description: This is an implementation of a MinHeap class using a dynamic array
#              in Python 3. The implementation includes the methods: add, get_min,
#              remove_min, and build_heap.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        index = self.heap.length() #get array index for initial insertion and append element 
        self.heap.append(node)
        
        while True:
            if index == 0: #if the element has reached the root of the heap, terminate
                return

            parent = (index - 1) // 2 #calculate index of parent
            if node < self.heap.get_at_index(parent): #if value of new element is less than parent value, swap elements
                self.heap.swap(index, parent)
                index = parent
            else: #if no swap needed, terminate
                return
        

    def get_min(self) -> object:
        if self.heap.length() == 0: #if trying to get value from empty heap, raise exception
            raise MinHeapException
        return self.heap.get_at_index(0) #return value of root


    def remove_min(self) -> object:
        index = self.heap.length() - 1 #get index of last element
        if index < 0: #if trying to remove element from empty heap, raise exception
            raise MinHeapException
        
        self.heap.swap(0, index) #swap first and last elements
        removed = self.heap.pop() #remove and store minimum value

        index = 0
        self.move_down(index) #move root replacement down the heap until placed correctly
        
        return removed #return stored minimum value


    def build_heap(self, da: DynamicArray) -> None:
        self.heap = DynamicArray() #delete previous content
        for i in range(da.length()): #make shallow copy of provided array
            self.heap.append(da.get_at_index(i)) #append if index does not exist
        index = self.heap.length() // 2 - 1 #find index of last interior node
        while index > -1: #move all interior nodes down to their correct locations
            self.move_down(index)
            index -= 1


    def move_down(self, index:int) -> None: #helper function to move nodes down for remove_min and build_heap
        end = self.heap.length() - 1 #get index of last element
        
        while True: #repeat until node is in correct position
            left = 2 * index + 1 #get index of left child
            if left > end: #if left child index is greater than last element index, the current index is a leaf, so return
                return
            right = 2 * index + 2 #get index of right child
            if right > end or self.heap.get_at_index(left) <= self.heap.get_at_index(right): #if right child does not exist or is greater than left child
                child_index = left #set child to be inspected to left child
                child = self.heap.get_at_index(left)
            else:
                child_index = right #otherwise, set child to be inspected to right child
                child = self.heap.get_at_index(right)
        
            if self.heap.get_at_index(index) > child: #if current index value is greater than child value, swap nodes
                self.heap.swap(index, child_index)
                index = child_index #update index of node for next loop
            else:
                return 

                

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
