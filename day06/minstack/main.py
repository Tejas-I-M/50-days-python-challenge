""" Day-06 -Minstack (Interactive Program)"""

class MinStack:
    def __init__(self):
        self.stack =[]
        self.min_stack =[]
    def push(self,x:int):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return None
        val = self.stack.pop()
        if val ==self.min_stack[-1]:
            self.min_stack.pop()
        return val
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    
    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
if __name__=='__main__':
    ms = MinStack()

    print("===Minstack Interactive Program===")
    print("commansds:")
    print("1.push")
    print("2.pop")
    print("3.top")
    print("4.min")
    print("5.exit")

    while True:
        cmd = input("Enter command:").strip().lower()

        if cmd.startswith('push'):
            try:
                value = int(cmd.split()[1])
                ms.push(value)
                print(f'Pushed {value} onto stack.')
            except :
                print("Invalid push command!, Use:push 5")
        
        elif cmd =='pop':
            val = ms.pop()
            if val is not None:
                print(f'Popped {val} from stack.')
        elif cmd =='top':
            print(f"Top",ms.top())

        elif cmd =='min':
            print(f'Min',ms.get_min())
        
        elif cmd=='exit':
            print('Exiting..')
            break

        else:
            print("Invalid command!Please try again.")