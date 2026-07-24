
class TODO():
    def __init__(self):
        self.list=[]
    def add(self):
        self.list.append(input("Enter Task="))
    def view(self):
        print("="*40)
        if not self.list:
            print("No Task")
        else:
            for i,task in enumerate(self.list,start=1):
                print(f"{i}:{task}")
        print("="*40)
    def remove(self):
        rem=int(input("Enter Number to remove Task="))
        if 1<=rem<=len(self.list):
            removed=self.list.pop(rem-1)
            print(f"Removed:{removed}")
        else:
            print("Invalid Task Number")

t=TODO()
x=1
while x!=4:
    print("1.Add Task")
    print("2.View Task")
    print("3.Complete Task")
    print("4.Exit")
    x=int(input("Enter Your Choice:"))
    match x:
        case 1:
            t.add()
        case 2:
            t.view()
        case 3:
            t.remove()
        case 4:
            x=4
        case _:
            print("Invalid Choice,Try Again")



