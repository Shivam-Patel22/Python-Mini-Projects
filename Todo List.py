list=[]
class TODO():
    def add(self):
        add=input("Enter Today's Task:")
        list.append(add)
    def view(self):
        print("="*40)
        print("Today's Task:")
        print(list)
        print("="*40)
    def remove(self):
        rem=input("Enter Number of Finished Task:")
        list.remove(rem)
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



