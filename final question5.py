# -*- coding: utf-8 -*-
"""
Created on Fri May 18 22:25:49 2018
Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements,
the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class 
below to use as a representation of a node in the linked list. Return the value of the node at that position.
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

@author: nidhi
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
  

    def length_list_till_m(self, position):
        current = self.head
        total_length = 0
        counter = 1
        if position < 1:
            return None
        while current.next and counter < position:
            total_length += 1
            counter += 1
            current = current.next
        print('total_length_till {} is {}, counter{}'.format(position, total_length, counter))
        return total_length, counter
    
  
                
                
                
                
# Test cases
# Set up some Elements
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Start setting up a LinkedList
ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n3)
ll.append(n4)
ll.append(n5)

print (ll.get_position(1).value)

#ll.length_list_till_m(4)
