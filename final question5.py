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


  

def length_list(ll):
        current = ll
        total_length = 1
        while current.next:
            total_length += 1
            current = current.next
        return total_length
        
  
def question5(ll, m):
        counter = 1
        current = ll
        total_length = length_list(ll)
        print ('total_length', total_length)
        position = total_length + 1 - m
        print ('position', position)
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current.data
            current = current.next
            counter += 1
        return None             
                
               
                
# Test cases
# Set up some Elements
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
#n6 = Node(6)

# Start setting up a LinkedList
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Test cases:

print('Data value of node at 3rd position from end: ', question5(n1, 3))
print('Data value after the end of linked list:', question5(n1, 0))
print('Data value before the first element of linked list:', question5(n1, 6))

