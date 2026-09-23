class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        

def remove_duplicates(head):
    cur = head
    while cur and cur.next:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
            
    return head

head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)



head = remove_duplicates(head)
cur = head

while cur:
    print(cur.value, end=" → ")
    cur = cur.next