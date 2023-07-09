class SList:
    class SNode:
        def __init__(self,data=0.0,n=None):
            self.Data=data
            self.Next=n
            #print('snode')
            
    def __init__(self):
        self.head=None
        self.Size=0
        #print('slist')
        
    def is_empty(self):
        return self.head==None
        #return self.Size==0
        
    def __len__(self):
        return self.Size
    
    
    def add_node_2_first(self, x):
        tmp=self.SNode(x,None)      
        if self.is_empty():
            self.head=tmp
        else:
            tmp.Next=self.head
            self.head=tmp             
        self.Size+=1   

    def add_node_2_first_by_ref(self, node):
        if self.is_empty():
            self.head=node
        else:
            node.Next=self.head
            self.head=node             
        self.Size+=1   
        
    def show(self):
        tmp=self.head
        while(tmp):
            print(tmp.Data,end='->')
            tmp=tmp.Next
        print()
    
    def SearchValue(self,x):
        if self.head==None:
            return 0,None
        else:
            tmp=self.head
            while tmp!=None:
                if tmp.Data==x:
                    return 1,tmp
                else:
                    tmp=tmp.Next
            return 0,None
        
    def FindLastNodeAddress(self):
        if self.head==None:
            return None
        else:
            tmp=self.head
            while tmp!=None:
                if tmp.Next==None:
                    return tmp
                else:
                    tmp=tmp.Next
                    
    def Add2LastByValue(self,x):
        if self.is_empty():
            self.add_node_2_first(x)
        else:
            last_node=self.FindLastNodeAddress()
            tmp=self.SNode(x,None)  
            last_node.Next=tmp
            self.Size+=1
            
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.Data

    
    def DeleteFirstNode(self):
        if self.is_empty()==True:
            return 0,None
        else:
            tmp=self.head
            self.head=self.head.Next
            self.Size-=1 
            #del tmp
            return 1,tmp
        
    def DeleteLastNode(self):
        if self.is_empty()==True:
            return 0,None
        else:
            tmp=self.head
            if tmp.Next==None:
                self.head=None
                node=tmp
                self.Size-=1
            else:
                while tmp.Next.Next!=None:
                    tmp=tmp.Next
                node=tmp.Next    
                tmp.Next=None
                self.Size-=1
            return 1,node
        
    def DeleteNodeAfterNodeByValue(self,x):
        flag,node=self.SearchValue(x)
        if flag==0:
            return 0,None
        else:
            if node.Next==None:
                return 0,None
            else:
                tmp=node.Next
                node.Next=tmp.Next
            
class Bread:
    def __init__(self, bread_type):
        self.bread_type = bread_type

class Customer:
    def __init__(self, ID, barbari_bread_count, lavash_bread_count):
        self.ID = ID
        self.barbari_bread_count = barbari_bread_count
        self.lavash_bread_count = lavash_bread_count

class Stack:
    def __init__(self):
        self.stack = SList()
        self.max_size = 15

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.add_node_2_first(item)
            return True
        else:
            return False

    def pop(self):
        if not self.stack.is_empty():
            _, item = self.stack.DeleteFirstNode()
            return item
        else:
            return None

    def peek(self):
        return self.stack.peek()

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.queue = SList()
        self.max_size = 10

    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            self.queue.Add2LastByValue(item)
            return True
        else:
            return False

    def dequeue(self):
        if not self.queue.is_empty():
            _, node = self.queue.DeleteFirstNode()
            return node.Data
        else:
            return None

    def size(self):
        return len(self.queue)

class Bakery:
    def __init__(self):
        self.barbari_stack = Stack()
        self.lavash_stack = Stack()
        self.customers_queue = Queue()

    def add_bread(self, bread_type, count):
        for _ in range(count):
            if bread_type == 'barbari':
                self.barbari_stack.push(Bread(bread_type))
            elif bread_type == 'lavash':
                self.lavash_stack.push(Bread(bread_type))

    def add_customer(self, ID, barbari_bread_count, lavash_bread_count):
        customer = Customer(ID, barbari_bread_count, lavash_bread_count)
        self.customers_queue.enqueue(customer)

    def serve_customers(self):
        while not self.customers_queue.queue.is_empty():
            customer = self.customers_queue.dequeue()
            while customer.barbari_bread_count > 0 and not self.barbari_stack.stack.is_empty():
                bread = self.barbari_stack.pop()
                customer.barbari_bread_count -= 1
            while customer.lavash_bread_count > 0 and not self.lavash_stack.stack.is_empty():
                bread = self.lavash_stack.pop()
                customer.lavash_bread_count -= 1
            if customer.barbari_bread_count > 0 or customer.lavash_bread_count > 0:
                # Customer still needs more bread
                # Add them back to the queue
                self.customers_queue.enqueue(customer)
                break
    def display_status(self):
        print('Barbari stack:')
        stack = []
        tmp = self.barbari_stack.stack.head
        while tmp:
            stack.append(tmp.Data.bread_type)
            tmp = tmp.Next
        if stack:
            print('->'.join(stack[::-1]))
        else:
            print()

        print('Lavash stack:')
        stack = []
        tmp = self.lavash_stack.stack.head
        while tmp:
            stack.append(tmp.Data.bread_type)
            tmp = tmp.Next
        if stack:
            print('->'.join(stack[::-1]))
        else:
            print()

        print('Customer queue:')
        tmp = self.customers_queue.queue.head
        while tmp:
            customer = tmp.Data
            if customer.barbari_bread_count > 0 or customer.lavash_bread_count > 0:
                print(f'Customer {customer.ID}: {customer.barbari_bread_count} barbari, {customer.lavash_bread_count} lavash')
            tmp = tmp.Next

bakery = Bakery()
bakery.add_customer(1, 15, 1)
bakery.add_customer(2, 2, 4)
bakery.add_customer(3, 10, 1)
bakery.add_bread('barbari', 25)
bakery.add_bread('lavash', 15)
bakery.serve_customers()
bakery.display_status()



