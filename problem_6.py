class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    
    def to_list(self):
        out_list = []

        node = self.head

        while node:
            out_list.append(node.value)
            node = node.next

        return out_list

def union(llist_1, llist_2):

    new_llist = LinkedList()
    list1 = llist_1.to_list() 
    list2 = llist_2.to_list()
    union_list = list(set(list1 + list2))

    if len(union_list) == 0:
        return None

    for i in union_list:
        new_llist.append(i)
    
    return new_llist

def intersection(llist_1, llist_2):
    
    new_llist = LinkedList()
    list1 = llist_1.to_list() 
    list2 = llist_2.to_list()

    intersection_list = list(set([i for i in list1 if i in list2]))

    if len(intersection_list) == 0:
        return None

    for i in intersection_list:
        new_llist.append(i)
    
    return new_llist

##################################################### Test ######################################################

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # return 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2)) # return 4 -> 21 -> 6 -> 


# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))  # return 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
print (intersection(linked_list_3,linked_list_4)) # return None

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1, 2, 3, 4]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # return 1 -> 2 -> 3 -> 4 -> 
print(intersection(linked_list_5, linked_list_6))  # return None

# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))  # return None
print(intersection(linked_list_7, linked_list_8))  # return None
