import sys
import math

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printLinkedList(self,head):
        ptr = head
        if not ptr:
            return
        while(ptr):
            print(ptr.data)
            ptr = ptr.next

    def insertNodeAtTail(self,node_data):
        """
        Given the item, add node at the tail of the linked list
        """
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node    
        return self.head

    def insertNodeAtHead(self,node_data):
        """
        Given the item, add node at the head of the linked list
        """
        node = SinglyLinkedListNode(node_data)
        
        if not self.head:
            self.head = node
            return self.head
        
        node.next = self.head
        self.head = node
        return self.head

    def removeDuplicatesFromSortedLinkedList(self,head):
        """
        Remove duplicate elements from a sorted linked list
        """
        if not head:
            return
        ptr = head
        next_node = ptr.next
        while(next_node):
            if (next_node.data - ptr.head)==0:
                ptr.next = next_node.next
                next_node = next_node.next
            else:
                ptr = ptr.next 
                next_node = next_node.next

        return head

    def hasCycle(self,head):
        """
        Given head to a linked list, check if the linked list has a cycle
        """
        l = set()
        if not head : return

        ptr = head
        while(ptr):
            if ptr not in l:
                l.add(ptr)
            else:
                return 1    
        return 0        

    def reverseLinkedList(self,head):
        """
        Given the head of a singly linked list, reverse the list and return the head of the reversed list
        """

        prev = None
        cur = head

        while(cur):
            next_node = cur.next
            cur.next = prev
            prev = cur 
            cur = next_node

        return prev

    def hasCycle_v2(self, head):
        """
        Given head to a linked list, check if the linked list has a cycle
        """

        if not head:
            return

        walk,run = head,head

        while(run.next and run.next.next):
            walk = walk.next
            run = run.next.next

            if walk == run:
                return True
        
        return False