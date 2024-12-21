#single inheritance
class Parent:
    name = 'john'
    
    def __init__(self):
        print('Parent')
        self.parent_attribute = "I am a Parent attribute"
        
    def give_advice(Self):
        return "Do what I tell you"
    
class Child(Parent):
    #Explicity call parent constructor
    def __init__(self):
        print('Child')
        super().__init__()
        
    def get_parent_attribute(self):
        self.give_advice()
        return self.parent_attribute
    
    def give_advice(self):
        return "I will do what I want"
    
child = Child()
child.name
print(child.give_advice())
#print(child.get_parent_attribute()) # Access parent attribute