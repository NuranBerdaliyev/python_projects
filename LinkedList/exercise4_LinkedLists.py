class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self, data):
        if self.head is None:
            self.head=Node(data)
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=Node(data)
    def insert_at_beginning(self, data):
        node=Node(data, self.head)
        self.head = node
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise ValueError("Index is out of allowed range")
        if index==0:
            self.insert_at_beginning(data)
            return
        current=self.head
        count=0
        while count!=index-1:
            current=current.next
            count+=1
        current.next=Node(data, current.next)
    def remove(self):
        if self.head is None:
            return 1
        current=self.head
        while current.next:
            current=current.next
        current=None
        return 0
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise ValueError("Index is out of allowed range")
        if index==0:
            self.head=self.head.next
            return
        count=0
        current=self.head
        while count!=index-1:
            current=current.next
            count+=1
        current.next=current.next.next
    def get_length(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    def __str__(self):
        current=self.head
        if not current:
            return "Empty"
        strr=""
        while current:
            strr+=f"{current.data}" + ("-->" if current.next else "")
            current=current.next
        return strr
    def insert_iterable(self, itr_obj):
        if not isinstance(itr_obj, (list, tuple, set)):
            raise TypeError("Wrong type")
        for el in itr_obj:
            self.insert(el)

if __name__=='__main__':
    n=LinkedList()
    while True:
        try:
            i=int(input("Choose the command:\n0.Exit\n1.Insert\n2.Remove\n3.Get length\n4.Look at the list\n"+\
                        "5.Insert some iterable object\n"))
        except (ValueError, TypeError):
            print("Not valid command")
            continue
        if i==1:
            try:
                j=int(input("Which type of inserting do you want?\n1.Insert to the end\n2.Insert to the beginning\n"\
                    +"3.Insert to the custom index\n"))
            except (ValueError, TypeError):
                print("Not valid command")
                continue
            data=input("Enter the data you want to insert: ")
            if j==1:
                n.insert(data)
                print("Inserted")
            elif j==2:
                n.insert_at_beginning(data)
                print("Inserted")
            elif j==3:
                try:
                    index=int(input("What's the custom index what's element you want to insert? "))
                except(ValueError, TypeError):
                    print("Not valid data")
                    continue
                try:
                    n.insert_at(index, data)
                    print("Inserted")
                except ValueError as e:
                    print(e)
                    continue
            else:
                print("There is no such a command")
                continue
        elif i==2:
            try:
                j=int(input("Which type of removing do you want?\n1.Remove an element at the end\n"+\
                        "2.Remove an element to the custom index\n"))
            except (ValueError, TypeError):
                print("Not valid data")
                continue
            if j==1:
                result = n.remove()
                if result==0:
                    print("The last element is removed")
                    continue
                if result==1:
                    print("There's nothing to remove")
                    continue
            elif j==2:
                try:
                    index=int(input("What's the custom index what's element you want to remove? "))
                except (ValueError, TypeError):
                    print("Not valid data")
                    continue
                try:
                    n.remove_at(index)
                    print("Removed")
                except ValueError as e:
                    print(e)
                    continue
        elif i==3:
            print("The length of this list is "+str(n.get_length()))
        elif i==4:
            print(n)
        elif i==5:
            try:
                lenth=int(input("Let's create this iterable object. How much elements does object have? "))
                l=[]
            except (ValueError, TypeError):
                print("Not valid data")
                continue
            for _ in range(lenth):
                el=input(f"Element number {_}: ")
                l.append(el)
            n.insert_iterable(l)
            print("Entire list is inserted")
        elif i==0:
            break
        else:
            print("There's no such a command")
            continue

                