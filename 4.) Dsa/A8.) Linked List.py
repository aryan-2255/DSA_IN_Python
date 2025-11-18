class node:
    def __init__(self,val):
        self.data = val
        self.next = None


node1 = node(5)
node2 = node(1)
node3 = node(4)

node1.next = node2
node2.next = node3

print(node2.next.data)
print(node1.next.next.data)


# userunput linkedlist

# ---------------------------------------------------------
# TOPIC: LINKED LIST (Singly Linked List)
# ---------------------------------------------------------
# A linked list is a data structure made of nodes.
# Each node stores:
#    1. data (value)
#    2. next (address of next node)
# ---------------------------------------------------------


# -------------------------------
# Step 1: Create a Node class
# -------------------------------
class Node:
    def __init__(self, val):
        self.data = val       # stores value
        self.next = None      # stores next node's address


# -------------------------------
# Step 2: Create LinkedList class
# -------------------------------
class LinkedList:

    # constructor
    def __init__(self):
        self.head = None      # first node of list (initially empty)

    # ---------------------------------------
    # Insert a node at the END of the list
    # ---------------------------------------
    def insertAtEnd(self, val):

        new_node = Node(val)   # create a new node

        # Case 1: List is empty → new node becomes head
        if self.head is None:
            self.head = new_node
            return

        # Case 2: List already has nodes → go to the last node
        temp = self.head
        while temp.next is not None:   # move until last node
            temp = temp.next

        # attach new node at end
        temp.next = new_node

    # ---------------------------------------
    # Display the linked list
    # ---------------------------------------
    def display(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")    # end of list


# ---------------------------------------
# Step 3: Take user input
# ---------------------------------------

ll = LinkedList()

n = int(input("How many nodes do you want to enter? "))

# loop to take values from user
for i in range(n):
    val = int(input(f"Enter value for node {i+1}: "))
    ll.insertAtEnd(val)


# ---------------------------------------
# Step 4: Display the final linked list
# ---------------------------------------
print("\nYour Linked List is:")
ll.display()
