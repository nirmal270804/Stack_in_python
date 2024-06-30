stk = []
c_size = 0
max_size = 10
def stack():
    global c_size, max_size  
    print("Choose Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    ch = int(input("Enter your choice: ")) 
    if ch == 1:
        if c_size == max_size:
            print("Stack is full!")
            y_n_ch = str(input("Do you want to continue? (Y/N): "))
            if y_n_ch.lower() == 'y':
                stack()
            else:
                return
        else:
            ele = input("Enter element to push into stack: ")
            stk.append(ele)
            c_size += 1
            y_n_ch = input("Do you want to continue? (Y/N): ")
            if y_n_ch.lower() == 'y':
                stack()
            else:
                return
    elif ch == 2:
        if c_size == 0:
            print("Stack is empty!")
            y_n_ch = input("Do you want to continue? (Y/N): ")
            if y_n_ch.lower() == 'y':
                stack()
            else:
                return
        else:
            le = stk[-1]
            print("The popped element is", le)
            stk.pop()
            c_size -= 1
            y_n_ch = input("Do you want to continue? (Y/N): ")
            if y_n_ch.lower() == 'y':
                stack()
            else:
                return
    elif ch == 3:
        print("Current stack:", stk)
        y_n_ch = input("Do you want to continue? (Y/N): ")
        if y_n_ch.lower() == 'y':
            stack()
        else:
            return
stack()
