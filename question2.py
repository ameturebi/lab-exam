class Stack(object): 
    def inil_ (self, Limit=10): 
        self.stk=[] 
        self.limit =Limit
    def isEmpty(self): 
        return len(self.stk) <=0 
    def push(self, item): 
        if len(self.stk) >= self.Limit: 
            print ('Stack Overflow!') 
        else: 
            self.stk.append(item) 
    def pop(self): 
        if len(self.stk) <= 0:
            print ('Stack Underflow!')
            return 0 
        else: 
            print ('Stack Underflow!') 
            return 0  
ourstack = Stack() 
ourstack.push("9") 
ourstack.push("2") 
ourstack.push("14") 
ourstack.push("3") 
ourstack. push("19") 
ourstack.push("3") 
ourstack. push("99") 
ourstack.push("9") 
print(ourstack.peek()) 
print (ourstack.pop()) 
print (ourstack.peek()) 
print (ourstack.pop())