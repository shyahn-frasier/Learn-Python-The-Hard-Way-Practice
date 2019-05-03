class Parent(object): #Makes the class Parent that is-a object

    def override(self): #Creates the override function that takes param self
        print("PARENT override()") #Prints a statement saying PARENT override()

    def implicit(self): #Creates the implicit function that takes param self
        print("PARENT implicit()") #Prints a statement saying PARENT implicit()
    
    def altered(self): #Creates the altered function that takes param self
        print("PARENT altered()") #Prints a statement saying PARENT altered()

class Child(Parent): #Makes the class child that inherits from Parent

    def override(self): #Creates the override function that takes param self
        print("CHILD override()") #Prints a statement saying CHILD override() -this is an override of Parent-

    def altered(self): #Creates the altered function that takes param self -this is an override of Parent-
        print("CHILD, BEFORE PARENT altered()") #Prints a statement saying CHILD, BEFORE PARENT altered()
        super(Child, self).altered() #Calls super with arguments Child and self, then calls the function altered on whatever it returns and also runs the Parent.altered version of the function
        print("CHILD, AFTER PARENT altered()") #Prints a statement saying CHILD, AFTER PARENT altered()

dad = Parent() #Sets dad to an instance of Parent
son = Child() #Sets son to an instance of child

dad.implicit() #Calls the implicit function for dad
son.implicit() #Calls the implicit function for son

dad.override() #Calls the override function for dad
son.override() #Calls the override function for son

dad.altered() #Calls the altered function for dad
son.altered() #Calls the altered function for son