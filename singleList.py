class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class singleList:
    def __init__(self, val):
        self.head = Node(val)
        self.reversedListArray = []

    def insertLast(self, val):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(val)

    def showList(self):
        current = self.head
        while current is not None:
            print('{} => '.format(current.value), end = '')
            current = current.next

    def insertAfterVal(self, val, newVal):
        current = self.head
        newNode = Node(newVal)
        while current.next is not None:
            if current.value == val:
                newNode.next = current.next
                current.next = newNode
                break
            current = current.next
        current.next = newNode

    def insertBeforeVal(self, val, newVal):
        current = self.head
        newNode = Node(newVal)

        if current.value == self.head.value:
            newNode.next = self.head
            self.head = newNode
        else:
            while current.next is not None:
                if current.next.value == val:
                    newNode.next = current.next
                    current.next = newNode
                    break
                current = current.next
            current.next = newNode

    def reverseList(self):
        listArray = []
        current = self.head
        while current is not None:
            listArray.append(current.value)
            current = current.next

        index = len(listArray) - 1
        while (index >= 0):
            self.reversedListArray.append(listArray[index])
            index = index - 1

    def insertFirst(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode




myList = singleList(10)

for i in range(11, 21):
    myList.insertLast(i)
myList.showList()

print("\n")

myList.insertBeforeVal(10, 27)
myList.insertFirst(100)
myList.showList()

print("\n")

myList.reverseList()
newList = singleList(myList.reversedListArray[0])
for i in range(1, len(myList.reversedListArray)):
    newList.insertLast(myList.reversedListArray[i])
myList = newList
myList.showList()


# myList.showList()
# print("\n")
# myList.insertAfterVal(11, 21)

# myList.showList()

# print("\n")
# myList.insertAfterVal(20, 29)
# myList.showList()
